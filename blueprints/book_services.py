from flask import Blueprint, render_template, request, redirect, url_for, flash

from models import db
from models.book import Book

book_bp = Blueprint('book_bp', __name__)


@book_bp.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', all_books=books)


@book_bp.route('/add/', methods=['POST'])
def insert_book():
    if request.method == 'POST':
        book = Book(
            title=request.form.get('title'),
            author=request.form.get('author'),
            price=request.form.get('price')
        )

        db.session.add(book)
        db.session.commit()

        flash("Book added successfully")
    return redirect(url_for('book_bp.index'))


@book_bp.route('/update/', methods=['POST'])
def update_book():
    if request.method == 'POST':
        data = Book.query.get(request.form.get('id'))

        data.title = request.form.get('title')
        data.author = request.form.get('author')
        data.price = request.form.get('price')

        db.session.commit()

        flash("Book is updated")
    return redirect(url_for('book_bp.index'))


@book_bp.route('/delete/<id>/', methods=['POST', 'GET'])
def delete(id):
    data = Book.query.get(id)

    db.session.delete(data)
    db.session.commit()

    flash("Book is deleted")
    return redirect(url_for('book_bp.index'))
