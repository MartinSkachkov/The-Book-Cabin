from models import db


class Book(db.Model):
    # class level variables (shared among all instances)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float)

    def __init__(self, title, author, price):
        # instance level variables
        self.title = title
        self.author = author
        self.price = price
