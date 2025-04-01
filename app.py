from flask import Flask

import config
from blueprints.book_services import book_bp
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.secret_key = config.SECRET_KEY

db.init_app(app)

app.register_blueprint(book_bp)

if __name__ == "__main__":
    app.run(debug=True)
