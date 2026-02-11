from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from datetime import datetime
import os
import io

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Создаем папку для временных PDF файлов
UPLOAD_FOLDER = 'temp_pdfs'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

class PDFGenerator:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self.title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=18,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=colors.darkblue
        )
        self.normal_style = ParagraphStyle(
            'CustomNormal',
            parent=self.styles['Normal'],
            fontSize=12,
            spaceAfter=12,
            alignment=TA_LEFT
        )
        
    def generate_pdf(self, data, filename):
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18
        )
        
        story = []
        
        # Заголовок документа
        title = Paragraph(data.get('title', 'Документ'), self.title_style)
        story.append(title)
        story.append(Spacer(1, 12))
        
        # Информация о создании
        created_date = datetime.now().strftime('%d.%m.%Y %H:%M')
        date_info = Paragraph(f'<b>Дата создания:</b> {created_date}', self.normal_style)
        story.append(date_info)
        story.append(Spacer(1, 12))
        
        # Основные поля
        fields = [
            ('author', 'Автор'),
            ('subject', 'Тема'),
            ('content', 'Содержание'),
            ('notes', 'Примечания')
        ]
        
        for field_key, field_name in fields:
            if data.get(field_key):
                field_title = Paragraph(f'<b>{field_name}:</b>', self.normal_style)
                story.append(field_title)
                
                field_content = Paragraph(data[field_key], self.normal_style)
                story.append(field_content)
                story.append(Spacer(1, 12))
        
        # Таблица с дополнительными данными
        if any(data.get(f'table_field_{i}') for i in range(1, 4)):
            story.append(Spacer(1, 12))
            table_title = Paragraph('<b>Дополнительная информация:</b>', self.normal_style)
            story.append(table_title)
            
            table_data = [['Параметр', 'Значение']]
            for i in range(1, 4):
                field_value = data.get(f'table_field_{i}')
                if field_value:
                    table_data.append([f'Поле {i}', field_value])
            
            if len(table_data) > 1:
                table = Table(table_data, colWidths=[2*inch, 3*inch])
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 12),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)
                ]))
                story.append(table)
        
        # Подпись
        if data.get('signature'):
            story.append(Spacer(1, 24))
            signature = Paragraph(f'<b>Подпись:</b> {data["signature"]}', self.normal_style)
            story.append(signature)
        
        doc.build(story)
        
        # Сохраняем в файл
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        with open(filepath, 'wb') as f:
            f.write(buffer.getvalue())
        
        buffer.close()
        return filepath

pdf_gen = PDFGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_pdf():
    try:
        # Получаем данные из формы
        form_data = {
            'title': request.form.get('title', '').strip(),
            'author': request.form.get('author', '').strip(),
            'subject': request.form.get('subject', '').strip(),
            'content': request.form.get('content', '').strip(),
            'notes': request.form.get('notes', '').strip(),
            'table_field_1': request.form.get('table_field_1', '').strip(),
            'table_field_2': request.form.get('table_field_2', '').strip(),
            'table_field_3': request.form.get('table_field_3', '').strip(),
            'signature': request.form.get('signature', '').strip()
        }
        
        # Проверяем, что хотя бы один из основных полей заполнен
        required_fields = ['title', 'content']
        if not any(form_data.get(field) for field in required_fields):
            flash('Пожалуйста, заполните хотя бы заголовок и содержание документа.', 'error')
            return redirect(url_for('index'))
        
        # Генерируем имя файла
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'document_{timestamp}.pdf'
        
        # Создаем PDF
        filepath = pdf_gen.generate_pdf(form_data, filename)
        
        flash('PDF документ успешно создан!', 'success')
        return send_file(
            filepath,
            as_attachment=True,
            download_name=filename,
            mimetype='application/pdf'
        )
        
    except Exception as e:
        flash(f'Ошибка при создании PDF: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/preview')
def preview():
    return render_template('preview.html')

# Очистка временных файлов при завершении
@app.teardown_appcontext
def cleanup_temp_files(error):
    try:
        for file in os.listdir(UPLOAD_FOLDER):
            filepath = os.path.join(UPLOAD_FOLDER, file)
            # Удаляем файлы старше 1 часа
            if os.path.getctime(filepath) < (datetime.now().timestamp() - 3600):
                os.remove(filepath)
    except:
        pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5009)