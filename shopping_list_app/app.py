from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping_list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class ShoppingItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.String(50), default='1')
    category = db.Column(db.String(50), default='Прочее')
    is_completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ShoppingItem {self.name}>'

@app.route('/')
def index():
    items = ShoppingItem.query.order_by(ShoppingItem.is_completed, ShoppingItem.created_at.desc()).all()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    name = request.form.get('name')
    quantity = request.form.get('quantity', '1')
    category = request.form.get('category', 'Прочее')
    
    if name:
        new_item = ShoppingItem(
            name=name.strip(),
            quantity=quantity.strip(),
            category=category
        )
        db.session.add(new_item)
        db.session.commit()
        flash('Товар добавлен в список!', 'success')
    else:
        flash('Название товара не может быть пустым!', 'error')
    
    return redirect(url_for('index'))

@app.route('/toggle/<int:item_id>')
def toggle_item(item_id):
    item = ShoppingItem.query.get_or_404(item_id)
    item.is_completed = not item.is_completed
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    item = ShoppingItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('Товар удален из списка!', 'info')
    return redirect(url_for('index'))

@app.route('/clear_completed')
def clear_completed():
    ShoppingItem.query.filter_by(is_completed=True).delete()
    db.session.commit()
    flash('Все выполненные покупки удалены!', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5018, debug=True)
