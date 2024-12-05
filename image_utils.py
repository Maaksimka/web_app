import requests
from PIL import Image
from io import BytesIO
import streamlit as st

# Функция для загрузки изображения по URL
def fetch_image(url, max_width=100, max_height=100):
    """
    Загружает изображение по указанному URL и масштабирует его до заданных размеров.
    
    Args:
        url (str): Ссылка на изображение.
        max_width (int): Максимальная ширина изображения.
        max_height (int): Максимальная высота изображения.
    
    Returns:
        PIL.Image: Масштабированное изображение или None, если загрузка не удалась.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            img.thumbnail((max_width, max_height))  # Масштабируем изображение
            return img
        else:
            return None
    except Exception as e:
        return None

# Функция для отображения модального окна с изображением
def show_image_modal(image_url):
    """
    Отображает изображение в модальном окне с использованием Streamlit.
    
    Args:
        image_url (str): Ссылка на изображение.
    """
    img = fetch_image(image_url)
    if img:
        st.image(img, caption="Фотография", use_column_width=True)
    else:
        st.error("Не удалось загрузить изображение.")
