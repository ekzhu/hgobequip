DATABASE = 'hgobequip.db'
DEBUG = True
SECRET_KEY = 'SECRET_KEY'
USERNAME = 'admin'
PASSWORD = 'default'

SITE_URL = 'http://localhost:5000'

UPLOAD_FOLDER_EQUIP = './photos/equips'
UPLOAD_FOLDER_GROUP = './photos/groups'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'JPG'])
MAX_CONTENT_LENGTH = 1 * 1024 * 1024