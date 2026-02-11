from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Таблица связи many-to-many
note_tags = db.Table('note_tags',
    db.Column('note_id', db.Integer, db.ForeignKey('note.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<Tag {self.name}>'

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    tags = db.relationship('Tag', secondary=note_tags, backref=db.backref('notes', lazy='dynamic'))
    
    def __repr__(self):
        return f'<Note {self.title}>'

@app.route('/')
def index():
    search = request.args.get('search', '')
    tag_filter = request.args.get('tag', '')
    
    query = Note.query
    
    if search:
        query = query.filter(Note.title.contains(search) | Note.content.contains(search))
    
    if tag_filter:
        tag = Tag.query.filter_by(name=tag_filter).first()
        if tag:
            query = query.filter(Note.tags.contains(tag))
    
    notes = query.order_by(Note.updated_at.desc()).all()
    tags = Tag.query.all()
    
    return render_template('index.html', notes=notes, tags=tags)

@app.route('/note/new', methods=['GET', 'POST'])
def new_note():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        tag_names = request.form.get('tags', '').split(',')
        
        if title and content:
            note = Note(title=title.strip(), content=content.strip())
            
            for tag_name in tag_names:
                tag_name = tag_name.strip()
                if tag_name:
                    tag = Tag.query.filter_by(name=tag_name).first()
                    if not tag:
                        tag = Tag(name=tag_name)
                        db.session.add(tag)
                    note.tags.append(tag)
            
            db.session.add(note)
            db.session.commit()
            flash('Заметка создана!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Заполните все поля!', 'error')
    
    return render_template('note_form.html', note=None)

@app.route('/note/<int:id>')
def view_note(id):
    note = Note.query.get_or_404(id)
    return render_template('view_note.html', note=note)

@app.route('/note/<int:id>/edit', methods=['GET', 'POST'])
def edit_note(id):
    note = Note.query.get_or_404(id)
    
    if request.method == 'POST':
        note.title = request.form.get('title', '').strip()
        note.content = request.form.get('content', '').strip()
        tag_names = request.form.get('tags', '').split(',')
        
        note.tags = []
        for tag_name in tag_names:
            tag_name = tag_name.strip()
            if tag_name:
                tag = Tag.query.filter_by(name=tag_name).first()
                if not tag:
                    tag = Tag(name=tag_name)
                    db.session.add(tag)
                note.tags.append(tag)
        
        db.session.commit()
        flash('Заметка обновлена!', 'success')
        return redirect(url_for('view_note', id=note.id))
    
    return render_template('note_form.html', note=note)

@app.route('/note/<int:id>/delete', methods=['POST'])
def delete_note(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    flash('Заметка удалена!', 'info')
    return redirect(url_for('index'))

@app.route('/tags')
def manage_tags():
    tags = Tag.query.all()
    return render_template('tags.html', tags=tags)

@app.route('/tag/<int:id>/delete', methods=['POST'])
def delete_tag(id):
    tag = Tag.query.get_or_404(id)
    db.session.delete(tag)
    db.session.commit()
    flash(f'Тег "{tag.name}" удален!', 'info')
    return redirect(url_for('manage_tags'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5016, debug=True)
