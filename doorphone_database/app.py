from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///doorphones.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Doorphone(db.Model):
 id = db.Column(db.Integer, primary_key=True)
 address = db.Column(db.String(200), nullable=False)
 entrance = db.Column(db.String(10), nullable=True)
 code = db.Column(db.String(20), nullable=False)
 notes = db.Column(db.Text, nullable=True)
 
 def __repr__(self):
 return f'<Doorphone {self.address}>'

class DoorphoneForm(FlaskForm):
 address = StringField('Адрес', validators=[DataRequired(), Length(min=5, max=200)])
 entrance = StringField('Подъезд', validators=[Length(max=10)])
 code = StringField('Код доступа', validators=[DataRequired(), Length(min=1, max=20)])
 notes = TextAreaField('Заметки', validators=[Length(max=500)])
 submit = SubmitField('Сохранить')

@app.route('/')
def index():
 doorphones = Doorphone.query.all()
 return render_template('index.html', doorphones=doorphones)

@app.route('/add', methods=['GET', 'POST'])
def add_doorphone():
 form = DoorphoneForm()
 if form.validate_on_submit():
 doorphone = Doorphone(
 address=form.address.data,
 entrance=form.entrance.data,
 code=form.code.data,
 notes=form.notes.data
 )
 db.session.add(doorphone)
 db.session.commit()
 flash('Домофон успешно добавлен!', 'success')
 return redirect(url_for('index'))
 return render_template('add_doorphone.html', form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_doorphone(id):
 doorphone = Doorphone.query.get_or_404(id)
 form = DoorphoneForm(obj=doorphone)
 if form.validate_on_submit():
 doorphone.address = form.address.data
 doorphone.entrance = form.entrance.data
 doorphone.code = form.code.data
 doorphone.notes = form.notes.data
 db.session.commit()
 flash('Информация о домофоне обновлена!', 'success')
 return redirect(url_for('index'))
 return render_template('edit_doorphone.html', form=form, doorphone=doorphone)

@app.route('/delete/<int:id>')
def delete_doorphone(id):
 doorphone = Doorphone.query.get_or_404(id)
 db.session.delete(doorphone)
 db.session.commit()
 flash('Домофон удален!', 'info')
 return redirect(url_for('index'))

@app.route('/search')
def search():
 query = request.args.get('q', '')
 if query:
 doorphones = Doorphone.query.filter(
 Doorphone.address.contains(query) | 
 Doorphone.code.contains(query)
 ).all()
 else:
 doorphones = []
 return render_template('search.html', doorphones=doorphones, query=query)

if __name__ == '__main__':
 with app.app_context():
 db.create_all()
 app.run(host="0.0.0.0", port=5016, debug=True)