import codecs

num_item = 13

source = codecs.open('source.txt','r','utf-16')
out = codecs.open('out.sql','w','utf-8')
groups = set()
for j,line in enumerate(source.readlines()):
	items = line.rstrip().split('\t')
	groups.add(items[2])
	id_name = items[1]+u"-"+items[0]
	items = items[2:]
	items.insert(0,id_name)
	items.insert(0,str(j+1))
	if len(items) < num_item:
		items.extend([u'' for k in range(num_item-len(items))])
	command = u"insert into entries values ("
	for i,item in enumerate(items):
		if i == 0:
			command += item + u", "
		elif i < len(items)-1:
			command += u"'" + item + u"', "
		else:
			command += u"'" + item + u"'"
	command += u");\n"
	out.write(command)

for group in groups:
	out.write(u'insert into equip_group (group_name) values (\''+group+'\');\n')