import pandas as pd
import streamlit as st
from bson import ObjectId
from database import db


def find_primary_column(collection_name):
    """
    Определяет второй столбец, содержащий `_id`, после MongoDB `_id`.
    """
    sample_document = db[collection_name].find_one()
    if not sample_document:
        return None

    columns = list(sample_document.keys())
    # Поиск первого столбца после MongoDB `_id`, содержащего `_id` в названии
    for i in range(1, len(columns)):
        if "_id" in columns[i]:
            return columns[i]
    return None


def create_id_mapping(selected_table, primary_column):
    """
    Создание словаря {primary_column: уникальный номер}.
    """
    data = list(db[selected_table].find())
    if data:
        return {row[primary_column]: idx + 1 for idx, row in enumerate(data)}
    return {}


def refresh_id_mapping(selected_table, primary_column):
    """
    Обновление словаря id_mapping после операций.
    """
    st.session_state["id_mapping"] = create_id_mapping(selected_table, primary_column)


def get_collection_structure(collection_name):
    """
    Получение структуры коллекции MongoDB.
    """
    sample_document = db[collection_name].find_one()
    if sample_document:
        return {k: type(v) for k, v in sample_document.items()}
    return {}


def render_form(fields, initial_values=None, prefix="form"):
    """
    Рендеринг формы для работы с документами.
    """
    data = {}
    for field, field_type in fields.items():
        if field == "_id":
            continue  # Игнорируем MongoDB _id
        initial_value = initial_values.get(field, "") if initial_values else None

        if field_type == int:
            data[field] = st.number_input(f"{field} (целое число)", value=initial_value, step=1, key=f"{prefix}_{field}")
        elif field_type == float:
            data[field] = st.number_input(f"{field} (дробное число)", value=initial_value, key=f"{prefix}_{field}")
        elif field_type == str:
            data[field] = st.text_input(f"{field} (текст)", value=str(initial_value), key=f"{prefix}_{field}")
        elif field_type == bool:
            data[field] = st.checkbox(f"{field} (логическое значение)", value=bool(initial_value), key=f"{prefix}_{field}")
        elif pd.api.types.is_datetime64_any_dtype(field_type):
            data[field] = st.date_input(f"{field} (дата)", value=initial_value, key=f"{prefix}_{field}")
    return data


def add_new_record(selected_table, primary_column):
    """
    Добавление новой записи.
    """
    fields = get_collection_structure(selected_table)

    with st.form(key="add_form"):
        new_record = render_form(fields, prefix="add")
        submit = st.form_submit_button("Добавить запись")

        if submit:
            if new_record[primary_column] in st.session_state["id_mapping"]:
                st.error(f"Запись с ключом {new_record[primary_column]} уже существует.")
                return

            try:
                db[selected_table].insert_one(new_record)
                st.success("Запись успешно добавлена.")
                refresh_id_mapping(selected_table, primary_column)
                st.rerun()
            except Exception as e:
                st.error(f"Ошибка добавления записи: {e}")


# Функция для получения второго столбца коллекции
def get_second_column_name(collection_name):
    """
    Получает второй столбец коллекции MongoDB (который идет после _id).
    """
    sample_document = db[collection_name].find_one()
    if sample_document:
        columns = list(sample_document.keys())
        # Возвращаем второй столбец после '_id'
        return columns[1] if len(columns) > 1 else None
    return None

# В функции для редактирования записи
def edit_form(selected_table, primary_column, selected_row):
    """
    Редактирование записи по второму столбцу (после _id).
    """
    # Получаем второй столбец
    second_column = get_second_column_name(selected_table)

    if not second_column:
        st.error("Не удалось получить второй столбец коллекции.")
        return

    fields = get_collection_structure(selected_table)
    real_id = None
    for key, value in st.session_state["id_mapping"].items():
        if value == selected_row:
            real_id = int(key)
            break


    if not real_id:
        st.error(f"Запись {real_id} не найдена.")
        return

    # Ищем запись по второму столбцу (second_column)
    document = db[selected_table].find_one({second_column: real_id})
    if not document:
        st.error(f"Запись с ключом {real_id, type(real_id)} не найдена. Искали {selected_row} в {second_column}")
        return
    st.write("**Диагностическая информация**")
    st.write(f"Выбранная таблица: `{selected_table}`")
    st.write(f"Первичный столбец: `{primary_column}`")
    st.write(f"Выбранная строка: `{selected_row}`")
    st.write(f"Второй столбец: `{second_column}`")
    st.write(f"Соответствующий real_id: `{real_id}`")
    st.write(f"id_mapping: {st.session_state['id_mapping']}")
    with st.form(key="edit_form"):
        updated_record = render_form(fields, document, prefix="edit")
        submit = st.form_submit_button("Обновить запись")

        if submit:
            try:
                db[selected_table].update_one({second_column: real_id}, {"$set": updated_record})
                st.success("Запись успешно обновлена.")
                refresh_id_mapping(selected_table, second_column)
                st.rerun()
            except Exception as e:
                st.error(f"Ошибка обновления записи: {e}")


def del_row(selected_table, primary_column, selected_row):
    """
    Удаление записи.
    """
    real_id = None
    for key, value in st.session_state["id_mapping"].items():
        if value == selected_row:
            real_id = int(key)
            break    
    second_column = get_second_column_name(selected_table)

    if not real_id:
        st.error(f"Запись {real_id, type(real_id), selected_row, selected_table} не найдена.")
        return

    try:
        result = db[selected_table].delete_one({second_column: real_id})
        if result.deleted_count > 0:
            st.success("Запись успешно удалена.")
            refresh_id_mapping(selected_table, second_column)
            st.rerun()
        else:
            st.warning(f"Запись с ключом {real_id} не найдена.")
    except Exception as e:
        st.error(f"Ошибка удаления записи: {e}")
