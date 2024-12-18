import io
import os
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image as PDFImage
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from image_utils import fetch_image
from reportlab.lib.pagesizes import landscape


# Регистрация шрифтов для PDF
pdfmetrics.registerFont(TTFont('DejaVu', 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVu-Bold', 'DejaVuSans-Bold.ttf'))

def export_to_pdf(df):
    """Экспорт таблицы в PDF с автоматической подстройкой размера страницы."""
    # Определяем размеры холста
    col_widths = [max(df[col].astype(str).map(len).max(), len(str(col))) * 7 for col in df.columns]
    table_width = sum(col_widths)
    table_height = len(df) * 20 + 50  # Высота строки примерно 20

    # Настраиваем холст под размеры таблицы
    page_size = (table_width + 20, table_height + 40)

    # Создаём документ
    pdf_file_path = "dynamic_table.pdf"
    pdf = SimpleDocTemplate(
        pdf_file_path, 
        pagesize=page_size, 
        topMargin=10, bottomMargin=10, leftMargin=10, rightMargin=10
    )

    # Подготовка данных для таблицы
    data = [df.columns.tolist()] + df.astype(str).values.tolist()

    # Создание таблицы
    table = Table(data, colWidths=col_widths)
        # Стиль для таблицы с поддержкой кириллицы
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'DejaVu-Bold'),  # Изменено на шрифт с кириллицей
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('FONTNAME', (0, 1), (-1, -1), 'DejaVu'),      # Изменено на шрифт с кириллицей
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    table.setStyle(style)

    # Сохраняем PDF
    pdf.build([table])

    # Читаем PDF как поток байтов
    with open(pdf_file_path, 'rb') as f:
        pdf_output = BytesIO(f.read())

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
