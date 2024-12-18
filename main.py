import streamlit as st
from login import mainer
from datetime import datetime
from car_to_excel import  save_card
from top_dealers import top_dealers_by_month
from clients_info import plot_customer_transactions, dealers_month_top
from database import db
from data_conversion import load_data_from_collection
from table_utils import render_custom_table
from crud import add_new_record, edit_form, del_row, refresh_id_mapping, find_primary_column
from file_utils import export_to_pdf
from column_table_names import table_names, column_names


if "user" not in st.session_state:
    mainer()  # Показываем страницу авторизации/регистрации
else:
    st.sidebar.success(f"Вы вошли как {st.session_state['role']}.")
    # Основная функциональность
      # Загружаем основную функциональность

    if "id_mapping" not in st.session_state:
        st.session_state["id_mapping"] = {}


    # Получаем динамический список коллекций из базы данных
    table_list = db.list_collection_names()
    if st.session_state['role'] in ['Клиент', 'Покупатель']:
            table_list = [table for table in table_list if table in ['Cars', 'Dealers']]    
    
    localized_table_list = [table_names.get(table, table) for table in table_list]


    # Отображаем список таблиц для выбора
    selected_table_localized = st.selectbox("Выберите таблицу:", localized_table_list)

    # Определяем исходное название таблицы
    selected_table = table_list[localized_table_list.index(selected_table_localized)]

    if selected_table:
        # Определяем primary_column
        primary_column = find_primary_column(selected_table)

        # Обновляем маппинг ID при каждом выборе таблицы
        refresh_id_mapping(selected_table, primary_column)

    if 'edit_mode' not in st.session_state:
        st.session_state['edit_mode'] = False
    if 'add_mode' not in st.session_state:
        st.session_state['add_mode'] = False
    if 'selected_row' not in st.session_state:
        st.session_state['selected_row'] = None
    if 'show_edit_form' not in st.session_state:
        st.session_state['show_edit_form'] = False
    if 'show_add_form' not in st.session_state:
        st.session_state['show_add_form'] = False
        
    # Загружаем данные из выбранной коллекции MongoDB
    df, types = load_data_from_collection(selected_table)

    # Преобразуем названия столбцов
    localized_columns = {col: column_names[selected_table].get(col, col) for col in df.columns}
    df.rename(columns=localized_columns, inplace=True)

    # Преобразование чисел с плавающей точкой в целые, если это возможно
    # Перебираем все столбцы DataFrame
    for col in df.select_dtypes(include=['float']).columns:
        df[col] = df[col].astype('int', errors='ignore')  # Преобразуем float в int


    df = df.astype('object')


    start_idx, end_idx, sorted_df = render_custom_table(df, localized_columns)


# Ваш код до данного блока остаётся без изменений.

    if df.columns[0] != '_id':
        # Определяем первый доступный столбец для выбора записи
        primary_column = sorted_df.columns[0]  # Первый столбец в отсортированном DataFrame
        remaining_columns = sorted_df.columns.tolist()  # Список всех столбцов
        selected_row_column = primary_column  # Используем первый столбец для идентификации записи

        # Интерфейс для выбора строки из отсортированного DataFrame
        if st.session_state['role'] == 'Дилер':
            if len(sorted_df.iloc[start_idx:end_idx]) > 0:  # Проверяем, что есть записи в текущем диапазоне
                selected_row = st.selectbox(
                    f"Выберите запись для редактирования/удаления по столбцу {primary_column}",
                    sorted_df.iloc[start_idx:end_idx][primary_column].values,  # Используем значения текущего диапазона
                    key="select_row"
                )
                st.session_state['selected_row'] = selected_row
            else:
                st.warning("Нет записей для отображения в текущем диапазоне.")

            # Логика для работы с выбранной строкой (только для дилеров)
            col1, col2 = st.columns(2)

            with col1:
                if st.button("Редактировать запись", key="edit_button"):
                    st.session_state['edit_mode'] = True
                    st.session_state['add_mode'] = False
                    st.session_state['show_add_form'] = False

            with col2:
                if st.button("Удалить запись", key="delete_button"):
                    del_row(selected_table, primary_column, selected_row)

                if "delete_message" in st.session_state and st.session_state["delete_message"]:
                    st.success(st.session_state["delete_message"])
                    st.session_state["delete_message"] = None  # Сбрасываем сообщение

                # Ручной перезапуск интерфейса
                if "reload" in st.session_state and st.session_state["reload"]:
                    st.session_state["reload"] = False  # Сбрасываем флаг
                    st.rerun()

        # Кнопки "Добавить запись" и "Скачать PDF" (условия зависят от роли)
        add_col, pdf_col = st.columns(2)

        with add_col:
            if st.session_state['role'] == 'Дилер' or (st.session_state['role'] == 'Клиент' and selected_table == "Cars"):
                add_button = st.button("Добавить запись", key="add_button")
                if add_button:
                    st.session_state['add_mode'] = True
                    st.session_state['edit_mode'] = False
                    st.session_state['show_edit_form'] = False

        with pdf_col:
            pdf_button = st.button("Скачать таблицу в PDF")
            if pdf_button:
                full_table_pdf = export_to_pdf(df)  # Экспорт всей таблицы
                st.download_button(
                    label="Скачать PDF",
                    data=full_table_pdf,
                    file_name=f"{selected_table}_full_table_{datetime.now().strftime('%Y-%m-%d')}.pdf",
                    mime="application/pdf",
                )


    # Форма для редактирования записи (только для дилеров)
    if st.session_state['edit_mode'] and st.session_state['role'] == 'Дилер':
        edit_form(selected_table, primary_column, selected_row)
    def find_second_column(collection_name):
        """
        Определяет название второго столбца, исключая _id, в коллекции MongoDB.
        """
        sample_document = db[collection_name].find_one()
        if not sample_document:
            return None
        
        columns = list(sample_document.keys())
        # Нам нужно взять второй столбец (кроме _id)
        for i in range(1, len(columns)):
            if columns[i] != '_id':  # Пропускаем _id
                return columns[i]
        
        return None  # Если нет второго столбца

    # Пример использования:
    second_column = find_second_column(selected_table)

    
    # Логика добавления записи
    if st.session_state['add_mode']:
        add_new_record(selected_table, second_column)

    if selected_table == "Cars":
        save_card()
    
    # Поиск по таблице
    st.markdown("---")
    st.subheader("Поиск по таблице")
    search_col, search_val = st.columns([1, 2])
    localized_column_names = list(localized_columns.values())

    with search_col:
        search_column_localized = st.selectbox("Выберите столбец для поиска:", localized_column_names, key="search_column")
        search_column = list(localized_columns.keys())[localized_column_names.index(search_column_localized)]

    with search_val:
        search_value = st.text_input("Введите значение для поиска:", key="search_value")

    if st.button("Поиск", key="search_button"):
        if search_value:
            # Ищем оригинальное имя столбца, связанное с локализованным названием
            original_column = None
            for orig, local in localized_columns.items():
                if local == search_column_localized:
                    original_column = local
                    break

            if original_column:
               
                # Проводим поиск в DataFrame по оригинальному имени столбца
                if original_column in df.columns:
                    search_results = df[df[original_column].astype(str).str.contains(search_value, na=False)]
                    st.write(f"Найдено {len(search_results)} результатов")
                    render_custom_table(search_results, localized_columns, key_prefix="search")
                else:
                    st.error(f"Столбец `{original_column}` отсутствует в DataFrame.")
            else:
                st.error("Не удалось найти оригинальное имя столбца для поиска.")
        else:
            st.warning("Пожалуйста, введите значение для поиска.")


    # Отображение функций только для дилеров
    if st.session_state['role'] == 'Дилер':
        dealers_month_top()
        top_dealers_by_month()
        plot_customer_transactions()
