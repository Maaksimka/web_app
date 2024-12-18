import io
import os
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image as PDFImage
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from image_utils import fetch_image


# Регистрация шрифтов для PDF
pdfmetrics.registerFont(TTFont('DejaVu', 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVu-Bold', 'DejaVuSans-Bold.ttf'))

def export_to_pdf(df):
    """Сохранение таблицы в PDF в стиле отображения"""
    # Создаем PDF-документ
    pdf_file_path = "temp_table.pdf"
    pdf = SimpleDocTemplate(pdf_file_path, pagesize=letter)
    
    # Заголовки и данные
    data = [df.columns.tolist()]  # Добавляем заголовки

    # Рендер данных
    for _, row in df.iterrows():
        row_data = []
        for col in df.columns:
            if col == 'photo':  # Столбец с изображением
                img = fetch_image(row[col])
                if img:
                    img_byte_arr = BytesIO()
                    img.save(img_byte_arr, format='PNG')
                    img_byte_arr.seek(0)
                    pdf_image = PDFImage(img_byte_arr, width=50, height=50)  # Меняем размер для PDF
                    row_data.append(pdf_image)
                else:
                    row_data.append("No Image")
            else:
                row_data.append(str(row[col]))
        data.append(row_data)

    # Создаем таблицу с визуальным стилем
    table = Table(data)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Цвет заголовков
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Текст в заголовке
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Выравнивание всех ячеек
        ('FONTNAME', (0, 0), (-1, 0), 'DejaVu-Bold'),  # Шрифт для заголовков
        ('FONTNAME', (0, 1), (-1, -1), 'DejaVu'),  # Шрифт для строк
        ('FONTSIZE', (0, 0), (-1, 0), 10),  # Размер шрифта заголовка
        ('FONTSIZE', (0, 1), (-1, -1), 8),  # Размер шрифта основного текста
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Внутренний отступ заголовка
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Сетка таблицы
    ])
    table.setStyle(style)

    # Генерация PDF
    pdf.build([table])

    # Читаем PDF как поток байтов
    with open(pdf_file_path, 'rb') as f:
        pdf_output = BytesIO(f.read())
    
    os.remove(pdf_file_path)  # Удаляем временный файл
    
    return pdf_output



def get_file_download_link(file_path, file_label):
    """
    Создает ссылку для скачивания файла в Streamlit.
    """
    with open(file_path, 'rb') as file:
        file_bytes = file.read()
    return io.BytesIO(file_bytes), file_label
