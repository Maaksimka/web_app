import pandas as pd
import streamlit as st
import streamlit.components.v1 as components


def sort_dataframe(df, column, ascending):
    """
    Сортирует DataFrame по указанной колонке и порядку.
    
    Args:
        df (pd.DataFrame): Таблица данных.
        column (str): Название колонки для сортировки.
        ascending (bool): Порядок сортировки (True для возрастания).
        
    Returns:
        pd.DataFrame: Отсортированная таблица.
    """
    df[column] = df[column].astype(str)
    return df.sort_values(by=column, ascending=ascending)



def render_custom_table(df, localized_columns=None, key_prefix=""):
    """
    Отображает таблицу с поддержкой пагинации, сортировки и локализации столбцов.

    Args:
        df (pd.DataFrame): Таблица данных.
        localized_columns (dict): Словарь локализованных названий столбцов {оригинал: локализация}.
        key_prefix (str): Префикс для уникальных ключей элементов Streamlit.

    Returns:
        Tuple: Индексы текущей страницы и отсортированный DataFrame.
    """
    total_rows = len(df)
    rows_per_page = 10
    total_pages = (total_rows // rows_per_page) + (1 if total_rows % rows_per_page > 0 else 0)

    # Управление пагинацией через session_state
    page = st.number_input(
        "Страница",
        min_value=1,
        max_value=total_pages if total_pages > 0 else 1,
        step=1,
        format="%i",
        key=f"{key_prefix}_page_input",
    )
    start_idx = (page - 1) * rows_per_page
    end_idx = start_idx + rows_per_page

    # Определяем названия столбцов для отображения (локализованные или оригинальные)
    if localized_columns:
        localized_column_names = list(localized_columns.values())
        sort_column_localized = st.selectbox("Сортировать по столбцу:", localized_column_names, key=f"{key_prefix}_sort_column")
        sort_column = list(localized_columns.keys())[localized_column_names.index(sort_column_localized)]
    else:
        sort_column = st.selectbox("Сортировать по столбцу:", df.columns, key=f"{key_prefix}_sort_column")

    ascending = st.checkbox("По возрастанию", value=True, key=f"{key_prefix}_ascending")

    # Сортировка данных
    sorted_df = df.sort_values(by=sort_column, ascending=ascending)

    # Отображаем текущие записи
    current_df = sorted_df.iloc[start_idx:end_idx]

    # Генерация HTML для таблицы
    table_html = "<table style='border-collapse: collapse; width: 100%;'>"
    table_html += "<thead><tr>"
    for col in current_df.columns:
        display_name = localized_columns[col] if localized_columns and col in localized_columns else col
        table_html += f"<th style='border: 1px solid black; padding: 5px; text-align: center;'>{display_name}</th>"
    table_html += "</tr></thead>"
    table_html += "<tbody>"
    for _, row in current_df.iterrows():
        table_html += "<tr>"
        for col in current_df.columns:
            if col == "Фото":  # Если это колонка с фото
                image_url = row[col]
                table_html += f"<td style='border: 1px solid black; padding: 5px; text-align: center;'>" \
                              f"<img src='{image_url}' alt='Image' style='max-width: 100px; max-height: 100px;'/></td>"
            else:
                table_html += f"<td style='border: 1px solid black; padding: 5px; text-align: center;'>{row[col]}</td>"
        table_html += "</tr>"
    table_html += "</tbody></table>"

    # Рендеринг HTML
    components.html(table_html, height=400, scrolling=True)

    return start_idx, end_idx, sorted_df
