from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x19\xa1!`\x1e\xe9\xeb\xee\x98;\xa6\xdf\xab\x82\xfeK'