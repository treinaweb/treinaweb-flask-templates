DEBUG = True

USERNAME = 'root'
PASSWORD = 'rootmysql'
SERVER = 'localhost'
DB = 'flask_templates'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "minha-chave-secreta"