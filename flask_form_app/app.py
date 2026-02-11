from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

class ContactForm(FlaskForm):
 name = StringField('Имя', validators=[DataRequired(), Length(min=2, max=50)])
 email = StringField('Email', validators=[DataRequired(), Email()])
 subject = SelectField('Тема', choices=[
 ('general', 'Общие вопросы'),
 ('support', 'Техническая поддержка'),
 ('business', 'Бизнес предложения')
 ], validators=[DataRequired()])
 message = TextAreaField('Сообщение', validators=[DataRequired(), Length(min=10, max=500)])
 submit = SubmitField('Отправить')

@app.route('/', methods=['GET', 'POST'])
def index():
 form = ContactForm()
 if form.validate_on_submit():
 flash(f'Спасибо, {form.name.data}! Ваше сообщение получено.', 'success')
 return redirect(url_for('success'))
 return render_template('index.html', form=form)

@app.route('/success')
def success():
 return render_template('success.html')

if __name__ == '__main__':
 app.run(host="0.0.0.0", debug=True)