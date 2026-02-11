from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch
import os
from datetime import datetime
import tempfile

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Создаем папку для временных файлов
if not os.path.exists('temp'):
    os.makedirs('temp')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    try:
        # Получаем данные из формы
        title = request.form.get('title', 'Документ без названия')
        author = request.form.get('author', 'Автор не указан')
        content = request.form.get('content', '')
        
        if not content.strip():
            flash('Содержимое документа не может быть пустым', 'error')
            return redirect(url_for('index'))
        
        # Создаем временный файл для PDF
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'document_{timestamp}.pdf'
        filepath = os.path.join('temp', filename)
        
        # Создаем PDF документ
        doc = SimpleDocTemplate(filepath, pagesize=A4)
        styles = getSampleStyleSheet()
        story = []
        
        # Добавляем заголовок
        title_style = styles['Title']
        story.append(Paragraph(title, title_style))
        story.append(Spacer(1, 12))
        
        # Добавляем автора
        author_style = styles['Normal']
        story.append(Paragraph(f'Автор: {author}', author_style))
        story.append(Spacer(1, 12))
        
        # Добавляем дату
        date_str = datetime.now().strftime('%d.%m.%Y %H:%M')
        story.append(Paragraph(f'Дата создания: {date_str}', author_style))
        story.append(Spacer(1, 24))
        
        # Добавляем основное содержимое
        content_style = styles['Normal']
        # Разбиваем содержимое на параграфы
        paragraphs = content.split('\n')
        for paragraph in paragraphs:
            if paragraph.strip():
                story.append(Paragraph(paragraph, content_style))
                story.append(Spacer(1, 12))
        
        # Генерируем PDF
        doc.build(story)
        
        flash('PDF успешно создан!', 'success')
        return send_file(filepath, as_attachment=True, download_name=filename)
        
    except Exception as e:
        flash(f'Ошибка при создании PDF: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/simple_pdf')
def simple_pdf():
    """Альтернативный метод создания простого PDF с помощью canvas"""
    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'simple_document_{timestamp}.pdf'
        filepath = os.path.join('temp', filename)
        
        # Создаем PDF с помощью canvas
        c = canvas.Canvas(filepath, pagesize=letter)
        width, height = letter
        
        # Добавляем текст
        c.setFont('Helvetica-Bold', 16)
        c.drawString(50, height - 50, 'Пример простого PDF документа')
        
        c.setFont('Helvetica', 12)
        c.drawString(50, height - 100, f'Дата создания: {datetime.now().strftime("%d.%m.%Y %H:%M")}')
        c.drawString(50, height - 130, 'Это пример автоматически сгенерированного PDF.')
        c.drawString(50, height - 160, 'Документ создан с помощью Flask и ReportLab.')
        
        # Добавляем линию
        c.line(50, height - 200, width - 50, height - 200)
        
        # Сохраняем PDF
        c.save()
        
        return send_file(filepath, as_attachment=True, download_name=filename)
        
    except Exception as e:
        flash(f'Ошибка при создании простого PDF: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5010)