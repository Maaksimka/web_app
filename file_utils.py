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
    """Сохранение таблицы в pdf"""
    # Создаем PDF-документ
    pdf_file_path = "temp_table.pdf"
    pdf = SimpleDocTemplate(pdf_file_path, pagesize=letter)

    # Преобразуем DataFrame в список для таблицы
    data = [df.columns.tolist()]  # Заголовки колонок

    # Настройка шрифта
    pdfmetrics.registerFont(TTFont('DejaVu', 'DejaVuSans.ttf'))  # Убедитесь, что DejaVuSans.ttf доступен
    pdfmetrics.registerFont(TTFont('DejaVu-Bold', 'DejaVuSans-Bold.ttf'))

    # Перебираем строки DataFrame и заменяем ссылки на изображения
    for index, row in df.iterrows():
        row_data = []
        for col in df.columns:
            if col == 'photo':  # Столбец с изображениями
                img = fetch_image(row[col])
                if img:
                    img_byte_arr = BytesIO()
                    img.save(img_byte_arr, format='PNG')
                    img_byte_arr.seek(0)
                    pdf_image = PDFImage(img_byte_arr, width=100, height=100)  # Ограничиваем размер
                    row_data.append(pdf_image)
                else:
                    row_data.append("No Image")
            else:
                row_data.append(str(row[col]))  # Преобразуем другие данные в строку
        data.append(row_data)

    # Создаем таблицу и настраиваем стиль
    table = Table(data)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'DejaVu-Bold'),  # Заголовок с жирным шрифтом
        ('FONTNAME', (0, 1), (-1, -1), 'DejaVu'),  # Основной текст с DejaVu
        ('FONTSIZE', (0, 0), (-1, 0), 8),  # Размер шрифта заголовка
        ('FONTSIZE', (0, 1), (-1, -1), 6),  # Размер шрифта основного текста
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)

    # Сохраняем PDF-документ
    pdf.build([table])

    # Читаем PDF-файл в байтовый поток
    with open(pdf_file_path, 'rb') as f:
        pdf_output = io.BytesIO(f.read())

    # Удаляем временный файл
    os.remove(pdf_file_path)

    return pdf_output


def get_file_download_link(file_path, file_label):
    """
    Создает ссылку для скачивания файла в Streamlit.
    """
    with open(file_path, 'rb') as file:
        file_bytes = file.read()
    return io.BytesIO(file_bytes), file_label
