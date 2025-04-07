import secrets_config

# Database configuration
SQLALCHEMY_DATABASE_URI = f'mysql://{secrets_config.username}:{secrets_config.password}@{secrets_config.host}/{secrets_config.db}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = secrets_config.secret_key
