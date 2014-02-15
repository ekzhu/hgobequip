import sqlite3
import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from werkzeug import secure_filename
from flask import send_from_directory
from contextlib import closing

##### APPLICATION SETTINGS ######
app = Flask(__name__)
app.config.from_pyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings.py"), silent=False)

##### /APPLICATION SETTINGS ######

# The columns in the data base table "entries" excluding photo
columns = ["equip_id", "group_name", "category", "case_id", "model", "manufacturer", "nick", "status", "borrower", "check_out_date", "note"]

##### HELPER FUNCTIONS #####
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql') as f:
			db.cursor().executescript(f.read())
		db.commit()

def get_group_names():
	cur = g.db.execute('SELECT group_name FROM equip_group')
	group_names = [row[0] for row in cur.fetchall()]
	return group_names

def get_all_entries():
	cur = g.db.execute('select * from entries order by id desc')
	# row[0] is the database primary id
	entries = [dict(equip_id=row[1], group_name=row[2], category=row[3], case_id=row[4], model=row[5], manufacturer=row[6], nick=row[7], status=row[8], borrower=row[9], check_out_date=row[10], note=row[11], photo=row[12]) for row in cur.fetchall()]
	return entries

def get_entry(equip_id):
	cur = g.db.execute('SELECT * FROM entries WHERE equip_id=?', (equip_id,))
	entries = [dict(equip_id=row[1], group_name=row[2], category=row[3], case_id=row[4], model=row[5], manufacturer=row[6], nick=row[7], status=row[8], borrower=row[9], check_out_date=row[10], note=row[11], photo=row[12]) for row in cur.fetchall()]
	return entries[0]

def get_entries_with_group_name(group_name):
	cur = g.db.execute('SELECT * FROM entries WHERE group_name=?', (group_name,))
	entries = [dict(equip_id=row[1], group_name=row[2], category=row[3], case_id=row[4], model=row[5], manufacturer=row[6], nick=row[7], status=row[8], borrower=row[9], check_out_date=row[10], note=row[11], photo=row[12]) for row in cur.fetchall()]
	return entries

def get_equip_ids_with_group_name(group_name):
	# Get all equip_id for this group
	cur = g.db.execute('SELECT equip_id FROM entries WHERE group_name=?', (group_name,))
	equip_ids = [row[0] for row in cur.fetchall()]
	return equip_ids

def update_entry_with_equip_id(equip_id, request_names, request_changes):
	request_changes.append(equip_id)
	g.db.execute('UPDATE entries SET ' + ', '.join([item+'=?' for item in request_names]) + ' WHERE equip_id=?', request_changes)
	g.db.commit()

def update_entries_with_equip_ids(equip_ids, request_names, request_changes):
	# Trick to change the last item of request_changes
	request_changes.append('')
	for equip_id in equip_ids:
		request_changes[-1] = equip_id
		g.db.execute('UPDATE entries SET '+','.join([name+'=?' for name in request_names])+' WHERE equip_id=?', request_changes)
	g.db.commit()

def update_entries_with_group_name(group_name, request_names, request_changes):
	request_changes.append(group_name)
	g.db.execute('UPDATE entries SET '+','.join([name+'=?' for name in request_names])+' WHERE group_name=?', request_changes)
	g.db.commit()

def add_entry_with_request(request_names, request_changes):
	g.db.execute('INSERT INTO entries (' + ','.join(request_names) + ') values ('+ ','.join(['?' for i in range(len(request_names))]) +')', request_changes)
	g.db.commit()

def add_group_with_group_name(group_name):
	g.db.execute('INSERT INTO equip_group (group_name) values (?)', (group_name,))
	g.db.commit()

def delete_entry_with_equip_id(equip_id):
	# Delete this entry
	g.db.execute('DELETE FROM entries where equip_id=?', (equip_id,))
	g.db.commit()

def delete_entries_with_group_name(group_name):
	g.db.execute('DELETE FROM entries where group_name=?', (group_name,))
	g.db.commit()

def delete_group_with_group_name(group_name):
	g.db.execute('DELETE FROM equip_group where group_name=?', (group_name,))
	g.db.commit()

# Find all matches between the request forms and the edit_list
# Return the matched key names and their corresponding values in request form
# edit_list: list of keys to look for in the request form
def get_request_all(request, edit_list):
	request_names = list()
	request_changes = list()
	# Find the requested changes
	for name in edit_list:
		if request.form.has_key(name):
			request_names.append(name)
			request_changes.append(request.form[name])
	return request_names, request_changes

# Find all matches between the request forms and the edit_list
# Return the matched key names and their corresponding values in request form
# edit_list: list of keys to look for in the request form
# NOTE: only non-empty form values will be returned here
def get_request_updates(request, edit_list):
	request_names = list()
	request_changes = list()
	# Find the requested changes
	for name in edit_list:
		if request.form.has_key(name):
			if request.form[name]:
				request_names.append(name)
				request_changes.append(request.form[name])
	return request_names, request_changes

def get_photo_url_with_equip_id(equip_id):
	cur = g.db.execute('SELECT photo FROM entries WHERE equip_id=?', (equip_id,))
	results = [row[0] for row in cur.fetchall()]
	return results[0]

def get_photo_url_with_group_name(group_name):
	cur = g.db.execute('SELECT photo FROM entries WHERE group_name=?', (group_name,))
	results = [row[0] for row in cur.fetchall()]
	return results[0]

def update_photo_url_with_equip_id(equip_id, url):
	g.db.execute('UPDATE entries SET photo=? WHERE equip_id=?', (url, equip_id))
	g.db.commit()

def update_photo_url_with_group_name(group_name, url):
	g.db.execute('UPDATE equip_groups SET photo=? WHERE group_name=?', (url, group_name))
	g.db.commit()

def cp_photo_url(cp_from_id, cp_to_id, table):
	if table == "equips":
		url = get_photo_url_with_equip_id(cp_from_id)
		update_photo_url_with_equip_id(cp_to_id, url)
	if table == "groups":
		url = get_photo_url_with_group_name(cp_from_id)
		update_photo_url_with_group_name(cp_to_id, url)

# Allowed file extensions in upload
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1] in app.config['ALLOWED_EXTENSIONS']

# Create the directory for the file if it does not exist
def ensure_dir(path_to_file):
	d = os.path.dirname(path_to_file)
	if not os.path.exists(d):
		os.makedirs(d)

def get_file_save_path(filename, kind):
	if kind == 'equips':
		save_path = os.path.join(app.config['UPLOAD_FOLDER_EQUIP'],filename)
	else:
		save_path = os.path.join(app.config['UPLOAD_FOLDER_GROUP'],filename)
	return save_path

def update_photo_url(filename, kind, item_id):
	if kind == 'equips':
		new_url = "".join([app.config['SITE_URL'], '/photos/equips/', filename])
		g.db.execute('UPDATE entries SET photo=? WHERE equip_id=?', (new_url, item_id))
		g.db.commit()
	if kind == 'groups':
		new_url = "".join([app.config['SITE_URL'], '/photos/groups/', filename])
		g.db.execute('UPDATE equip_groups SET photo=? WHERE group_name=?', (new_url, group_name))
		g.db.commit()

def upload_photo(file, kind, item_id):
	if file and allowed_file(file.filename) and (kind == 'equips' or kind == 'groups'):
		filename = secure_filename(file.filename)
		save_path = get_file_save_path(filename, kind)
		if os.path.exists(save_path):
			flash('File exists. Please use another file name...')
			flash('Photo was not uploaded')
			return False
		ensure_dir(save_path)
		file.save(save_path)
		update_photo_url(filename, kind, item_id)
		# flash('%s' % get_photo_url_with_equip_id(item_id))
		return True
	if not allowed_file(file.filename):
		flash('Not supported file type')
		flash('Photo was not uploaded')
	return False

##### //HELPER FUNCTIONS #####

##### APPLICATION FUNCTIONS #####
@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	g.db.close()

@app.route('/')
def show_entries():
	entries = get_all_entries()
	return render_template('show_entries.html', entries=entries)

@app.route('/groups')
def show_groups():
	group_names = get_group_names()
	groups = list()
	for name in group_names:
		entries = get_entries_with_group_name(name)
		groups.append(entries)
	return render_template('show_groups.html', groups=groups)

@app.route('/groups/<group_name>', methods=['GET'])
def detail_group(group_name):
	pass

@app.route('/manage_groups/<group_name>', methods=['GET','POST'])
def manage_group(group_name):
	if not session.get('logged_in'):
		abort(401)
	if request.method == 'POST':
		if group_name == request.form['group_name']:
			edit_list = ['case_id', 'status', 'borrower', 'check_out_date']
			[request_names, request_changes] = get_request_updates(request, edit_list)
			if request_changes and request_names:
				update_entries_with_group_name(group_name, request_names, request_changes)
				flash("Equipment record was successfully updated for group %s" % group_name)
		else:
			edit_list = ['group_name', 'case_id', 'status', 'borrower', 'check_out_date']
			[request_names, request_changes] = get_request_updates(request, edit_list)
			if request_changes and request_names:
				equip_ids = get_equip_ids_with_group_name(group_name)
				update_entries_with_equip_ids(equip_ids, request_names, request_changes)
				flash("Equipment record was successfully updated for group %s" % group_name)
		return redirect(url_for('manage_group', group_name=group_name))
	else:
		# For GET request
		entries = get_entries_with_group_name(group_name)
		group_names = get_group_names()
		return render_template('manage_group.html', group=entries, group_names=group_names)

@app.route('/manage_groups')
def manage_groups():
	if not session.get('logged_in'):
		abort(401)
	group_names = get_group_names()
	return render_template('manage_groups.html', group_names=group_names)

@app.route('/add_group', methods=['POST'])
def add_group():
	if not session.get('logged_in'):
		abort(401)
	if request.method == 'POST':
		new_group = request.form['new_group_name']
		add_group_with_group_name(new_group)
		flash("New group %s was successfully added" % new_group)
		return redirect(url_for('manage_groups'))

@app.route('/delete_group', methods=['POST'])
def delete_group():
	if not session.get('logged_in'):
		abort(401)
	if request.method == 'POST':
		group_to_delete = request.form['group_to_delete']
		delete_group_with_group_name(group_to_delete)
		delete_entries_with_group_name(group_to_delete)
		flash("Group %s and its equipment were successfully deleted" % group_to_delete)
		return redirect(url_for('manage_groups'))

@app.route('/add', methods=['GET', 'POST'])
def add_entry():
	if not session.get('logged_in'):
		abort(401)
	if request.method == 'POST':
		[request_names, request_changes] = get_request_all(request, columns)
		# request_changes = [request.form['equip_id'], request.form['group_name'], request.form['category'], request.form['case_id'], request.form['model'], request.form['manufacturer'], request.form['nick'], request.form['status'], request.form['borrower'], request.form['check_out_date'], request.form['note']]
		add_entry_with_request(request_names, request_changes)
		if request.files.has_key('photo'):
			upload_photo(request.files['photo'], 'equips', request.form['equip_id'])
		flash("New entry %s was successfully added" % request.form['equip_id'])
		return redirect(url_for('show_entries'))
	else:
		group_names = get_group_names()
		return render_template('new_entry.html', group_names=group_names)

@app.route('/detail/<equip_id>')
def detail_entry(equip_id):
	if not session.get('logged_in'):
		abort(401)
	entry = get_entry(equip_id)
	return render_template('detail_entry.html', entry=entry)

@app.route('/update/<equip_id>', methods=['GET','POST'])
def update_entry(equip_id):
	if not session.get('logged_in'):
		abort(401)
	if request.method == 'POST':
		if request.form.has_key('delete_it'):
			if request.form['delete_it'] == "YesDelete":
				delete_entry_with_equip_id(equip_id)
				flash("Entry %s was successfully deleted" % equip_id)
				return redirect(url_for('show_entries'))
			else:
				flash("Entry %s was not deleted" % equip_id)
				return redirect(url_for('show_entries'))
		# Get request list
		[request_names, request_changes] = get_request_all(request, columns)
		if equip_id != request.form['equip_id']:
			# If the equip_id has been changed by the user
			# Create a new entry with the new equip_id and delete the old one
			add_entry_with_request(request_names, request_changes)
			cp_photo_url(equip_id, request.form['equip_id'], 'equips')
			delete_entry_with_equip_id(equip_id)
		else:
			update_entry_with_equip_id(equip_id, request_names, request_changes)
		if request.files.has_key('photo'):
			upload_photo(request.files['photo'], 'equips', request.form['equip_id'])
		flash("Entry %s was successfully updated" % equip_id)
		return redirect(url_for('detail_entry', equip_id=equip_id))
	else:
		entry = get_entry(equip_id)
		group_names = get_group_names()
		return render_template('modify_entry.html', entry=entry, group_names=group_names)

@app.route('/mass_edit_entries', methods=['POST'])
def mass_edit_entries():
	if not session.get('logged_in'):
		abort(401)
	if request.method == 'POST':
		if request.form.has_key('mass_edit'):
			equip_ids = request.form.getlist('mass_edit')
			group_names = get_group_names()
			entries = list()
			for equip_id in equip_ids:
				entries.append(get_entry(equip_id))
			return render_template('mass_edit_entries.html', entries=entries, group_names=group_names)
		else:
			return redirect(url_for('show_entries'))

@app.route('/mass_edit', methods=['POST'])
def mass_edit():
	if not session.get('logged_in'):
		abort(401)
	if request.method == 'POST':
		if request.form.has_key('mass_edit'):
			[request_names, request_changes] = get_request_updates(request, columns)
			equip_ids = request.form.getlist('mass_edit')
			update_entries_with_equip_ids(equip_ids, request_names, request_changes)
			flash("The selected entries was successfully updated")
			return redirect(url_for('show_entries'))
		else:
			return redirect(url_for('show_groups'))

@app.route('/photos/<kind>/<filename>')
def show_photo(kind, filename):
	if not session.get('logged_in'):
		abort(401)
	if kind == 'equips':
		return send_from_directory(app.config['UPLOAD_FOLDER_EQUIP'],filename)
	if kind == 'groups':
		return send_from_directory(app.config['UPLOAD_FOLDER_GROUP'],filename)
	return redirect(url_for('show_entries'))

@app.route('/upload/<kind>/<item_id>', methods=['POST'])
def upload_file(kind, item_id):
	if not session.get('logged_in'):
		abort(401)
	if request.method == 'POST':
		file = request.files['photo']
		# allowed_folders = app.config['UPLOAD_FOLDER_EQUIP'].split('/')[-1]
		if file and allowed_file(file.filename) and (kind == 'equips' or kind == 'groups'):
			filename = secure_filename(file.filename)
			save_path = get_file_save_path(filename, kind)
			if os.path.exists(save_path):
				flash('File exists. Please use another file name...')
				return redirect(request.url)
			ensure_dir(save_path)
			file.save(save_path)
			update_photo_url(filename, kind, item_id)
			flash('New photo was successfully uploaded.')
		if request.url:
			return redirect(request.url)
		else:
			return redirect(url_for('show_entries'))
	return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME']:
			error = 'Invalid username'
		elif request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid password'
		else:
			session['logged_in'] = True
			flash('You were logged in')
			return redirect(url_for('show_entries'))
	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('show_entries'))

##### // APPLICATION FUNCTIONS #####

if __name__ == '__main__':
	# init_db()
	app.run()
