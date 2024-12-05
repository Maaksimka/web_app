from database import db
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from datetime import datetime


contracts_collection = db['Contracts']

def get_customer_transactions_2024():
    """
    Возвращает количество купленных и проданных авто каждым клиентом за 2024 год.
    """
    pipeline = [
        # Фильтруем данные за 2024 год
        {
            "$match": {
                "contract_date": {
                    "$gte": "2024-01-01",
                    "$lte": "2024-12-31"
                }
            }
        },
        # Группировка по продавцу
        {
            "$group": {
                "_id": "$customer_fio",
                "sold_count": {"$sum": 1},  # Считаем продажи
                "bought_count": {"$sum": 0}  # Инициализируем для покупок
            }
        },
        # Объединение с покупателями
        {
            "$unionWith": {
                "coll": "Final_contract",
                "pipeline": [
                    {
                        "$group": {
                            "_id": "$buyer_fio",
                            "sold_count": {"$sum": 0},  # Инициализируем для продаж
                            "bought_count": {"$sum": 1}  # Считаем покупки
                        }
                    }
                ]
            }
        },
        # Суммируем покупки и продажи по каждому клиенту
        {
            "$group": {
                "_id": "$_id",
                "bought_count": {"$sum": "$bought_count"},
                "sold_count": {"$sum": "$sold_count"}
            }
        },
        # Форматируем результаты
        {
            "$project": {
                "_id": 0,
                "customer_name": "$_id",
                "bought_count": 1,
                "sold_count": 1
            }
        },
        # Сортируем по имени клиента
        {
            "$sort": {"customer_name": 1}
        }
    ]

    return list(contracts_collection.aggregate(pipeline))




def plot_customer_transactions():
    """Строит диаграмму количества покупок и продаж авто клиентами."""
    st.subheader("Количество покупок и продаж авто клиентами за 2024 год")

    # Получаем данные из базы
    customer_transactions = get_customer_transactions_2024()

    if customer_transactions:
        # Преобразуем данные в DataFrame
        df = pd.DataFrame(customer_transactions)

        # Сбрасываем индекс и добавляем столбец "№" для нумерации
        df.reset_index(drop=True, inplace=True)  # Сбрасываем текущий индекс
        df.index += 1  # Сдвигаем индексацию на 1
        df = df.rename(columns={"index": "№", "customer_name": "ФИО", "bought_count": "Куплено", "sold_count": "Продано"})

        with st.container():
            # Отображение таблицы
            st.table(df)  # Просто передаём DataFrame без доп. преобразований

            # Построение диаграммы
            fig, ax = plt.subplots(figsize=(10, 6))

            x = range(len(df["ФИО"]))
            ax.bar(x, df["Куплено"], label="Покупки", color="skyblue")
            ax.bar(x, df["Продано"], label="Продажи", bottom=df["Куплено"], color="orange")
            ax.set_xticks(x)
            ax.set_xticklabels(df["ФИО"], rotation=45, ha="right")
            ax.set_title("Количество сделок по клиентам за 2024 год")
            ax.set_xlabel("Клиенты")
            ax.set_ylabel("Количество сделок")
            ax.legend()

            st.pyplot(fig)
    else:
        st.write("Данные за 2024 год отсутствуют.")





def get_top_3_dealers_for_current_month():
    today = datetime.today()
    first_day_of_current_month = datetime(today.year, today.month, 1)
    if today.month == 12:
        first_day_of_next_month = datetime(today.year + 1, 1, 1)
    else:
        first_day_of_next_month = datetime(today.year, today.month + 1, 1)

    start_date = first_day_of_current_month.strftime("%Y-%m-%d")
    end_date = first_day_of_next_month.strftime("%Y-%m-%d")

    pipeline = [
        {
            '$match': {
                'contract_date': {
                    '$gte': start_date,
                    '$lt': end_date
                }
            }
        },
        {
            '$group': {
                '_id': '$dealer_id',
                'total_sum': {'$sum': '$price'}
            }
        },
        {
            '$sort': {'total_sum': -1}
        },
        {
            '$limit': 3
        },
        {
            '$lookup': {
                'from': 'Dealers',
                'localField': '_id',
                'foreignField': 'dealer_id',
                'as': 'dealer_info'
            }
        },
        {
            '$unwind': {
                'path': '$dealer_info',
                'preserveNullAndEmptyArrays': False
            }
        },
        {
            '$group': {
                '_id': '$_id',  # Уникальный dealer_id
                'total_sum': {'$first': '$total_sum'},
                'dealer_info': {'$first': '$dealer_info'}
            }
        }
    ]

    result = list(db.Contracts.aggregate(pipeline))
    return result




def dealers_month_top():
    """
    Отображает таблицу с топ-3 дилерами по сумме контрактов за текущий месяц.
    """
    st.subheader("Топ-3 дилеров с максимальной суммой договоров за текущий месяц")

    # Получаем данные о топ-3 дилерах
    top_dealers = get_top_3_dealers_for_current_month()

    if top_dealers:
        # Преобразуем данные в удобный для отображения формат
        top_dealers_data = [
            {
                "Название": dealer["dealer_info"]["fio"],
                "Телефон": dealer["dealer_info"]["phone_number"],
                "Email": dealer["dealer_info"]["email"],
                "Рабочие часы": dealer["dealer_info"]["working_hours"],
                "Сумма договоров": dealer["total_sum"]
            }
            for dealer in top_dealers
        ]

        # Конвертируем данные в DataFrame
        df_top_dealers = pd.DataFrame(top_dealers_data)

        # Добавляем нумерацию и заменяем индекс
        df_top_dealers.index = range(1, len(df_top_dealers) + 1)
        df_top_dealers.index.name = "№"

        # Выводим таблицу
        st.table(df_top_dealers)
    else:
        st.write("Данные за текущий месяц отсутствуют.")
