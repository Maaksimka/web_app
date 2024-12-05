
import io
import requests
import xlsxwriter
import streamlit as st
from data_conversion import load_data_from_collection


def save_car_to_excel(car_data):
    """Сохраняет данные автомобиля в Excel с изображением, скачанным по ссылке."""
    output = io.BytesIO()

    # Создаем Excel-файл
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet("Car Details")

    # Настройки стилей
    bold = workbook.add_format({'bold': True})
    wrap_text = workbook.add_format({'text_wrap': True})

    # Заголовки
    headers = ["Brand", "Model", "Year", "Mileage", "Price", "Photo"]
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header, bold)

    # Заполняем данные
    row = 1
    col = 0
    worksheet.write(row, col, car_data.get("brand", ""), wrap_text)
    worksheet.write(row, col + 1, car_data.get("model", ""), wrap_text)
    worksheet.write(row, col + 2, car_data.get("year", ""), wrap_text)
    worksheet.write(row, col + 3, car_data.get("mileage", ""), wrap_text)
    worksheet.write(row, col + 4, car_data.get("price", ""), wrap_text)

    # Добавляем изображение
    photo_url = car_data.get("photo", "")
    if photo_url:
        response = requests.get(photo_url)
        if response.status_code == 200:
            img_data = io.BytesIO(response.content)  # Сохраняем изображение в память
            worksheet.insert_image(row, col + 6, "temp_image.png", {
                'image_data': img_data,  # Используем объект изображения из памяти
                'x_scale': 0.5, 'y_scale': 0.5
            })

    workbook.close()
    output.seek(0)
    return output

def save_card():
    """Скачивание карточки выбранного автомобиля"""
    st.subheader("Карточка автомобиля")

    # Загрузка данных автомобилей
    cars_df, _ = load_data_from_collection("Cars")

    # Выбор автомобиля
    selected_car_id = st.selectbox("Выберите автомобиль", cars_df["№"].tolist())

    if selected_car_id:
        # Фильтрация данных по выбранному `car_id`
        car_data = cars_df[cars_df["№"] == selected_car_id].iloc[0].to_dict()

        # Кнопка для скачивания карточки
        if st.button("Сохранить карточку автомобиля в Excel"):
            excel_file = save_car_to_excel(car_data)
            st.download_button(
                label="Скачать карточку",
                data=excel_file,
                file_name=f"Car_{selected_car_id}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )