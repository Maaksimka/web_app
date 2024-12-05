from database import db
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


def get_dealer_contracts_by_month(selected_month):
    """
    Возвращает количество договоров по дилерам за выбранный месяц.
    """
    pipeline = [
        # Фильтруем контракты по выбранному месяцу
        {
            "$match": {
                "contract_date": {"$regex": f"^{selected_month}"}
            }
        },
        # Группировка по dealer_id и подсчет количества договоров
        {
            "$group": {
                "_id": "$dealer_id",           # Группируем по ID дилера
                "contract_count": {"$sum": 1}  # Считаем количество договоров
            }
        },
        # Джойн с коллекцией Dealers для получения информации о дилере
        {
            "$lookup": {
                "from": "Dealers",            # Коллекция дилеров
                "localField": "_id",          # Поле dealer_id из Contracts
                "foreignField": "dealer_id",  # Поле dealer_id из Dealers
                "as": "dealer_info"           # Название результирующего поля
            }
        },
        # Разворачиваем массив с данными дилера
        {
            "$unwind": "$dealer_info"
        },
        # Форматируем результат
        {
            "$project": {
                "_id": 0,
                "dealer_name": "$dealer_info.fio",  # Имя дилера
                "contract_count": 1                # Количество договоров
            }
        },
        # Сортируем по количеству договоров
        {
            "$sort": {"contract_count": -1}
        }
    ]

    return list(db.Contracts.aggregate(pipeline))



def top_dealers_by_month():
    """
    Отображает диаграмму по количеству договоров дилеров за выбранный месяц.
    """
    st.subheader("Диаграмма: Количество договоров по дилерам за месяц")

    # Генерация списка месяцев для выбора (2023-2024)
    years = [2023, 2024]
    months = [f"{year}-{month:02}" for year in years for month in range(1, 13)]
    selected_month = st.selectbox("Выберите месяц", months)

    if selected_month:
        # Получаем данные
        dealer_data = get_dealer_contracts_by_month(selected_month)

        if dealer_data:
            # Преобразуем данные в DataFrame
            df = pd.DataFrame(dealer_data)

            # Добавляем столбец с нумерацией
            df.index = range(1, len(df) + 1)
            df.index.name = "№"


            # Построение диаграммы
            fig, ax = plt.subplots(figsize=(12, 8))  # Увеличиваем размер графика
            ax.bar(df["dealer_name"], df["contract_count"], color="skyblue")
            ax.set_title(f"Количество договоров по дилерам за {selected_month}")
            ax.set_xlabel("Дилеры")
            ax.set_ylabel("Количество договоров")
            ax.tick_params(axis="x", rotation=45)

            st.pyplot(fig)
        else:
            st.write("Данные за выбранный месяц отсутствуют.")
