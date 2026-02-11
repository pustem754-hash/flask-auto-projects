from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-books-key-12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class BookNote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100))
    genre = db.Column(db.String(100))
    rating = db.Column(db.Integer)
    notes = db.Column(db.Text)
    date_read = db.Column(db.DateTime, default=datetime.utcnow)

class BookForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    author = StringField('Автор')
    genre = StringField('Жанр')
    rating = IntegerField('Оценка (1-10)')
    notes = TextAreaField('Заметки')

@app.route('/')
def index():
    books = BookNote.query.order_by(BookNote.date_read.desc()).all()
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        book = BookNote(
            title=form.title.data,
            author=form.author.data,
            genre=form.genre.data,
            rating=form.rating.data,
            notes=form.notes.data
        )
        db.session.add(book)
        db.session.commit()
        flash('Книга добавлена!', 'success')
        return redirect(url_for('index'))
    return render_template('add_book.html', form=form)

@app.route('/view/<int:id>')
def view_book(id):
    book = BookNote.query.get_or_404(id)
    return render_template('view_book.html', book=book)

@app.route('/delete/<int:id>')
def delete_book(id):
    book = BookNote.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    flash('Книга удалена!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5021, debug=True)
