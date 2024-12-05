import pandas as pd
import numpy as np
from database import db


def convert_object_id_to_string(data):
    """
    Преобразует ObjectId в строку в каждом элементе списка словарей.
    :param data: Список документов из MongoDB.
    :return: Список документов с ObjectId в виде строк.
    """
    for item in data:
        if '_id' in item:
            item['_id'] = str(item['_id'])
    return data

def convert_numpy_to_python(data):
    """
    Преобразует numpy-типы в стандартные типы Python.
    :param data: Словарь с данными.
    :return: Словарь с преобразованными типами.
    """
    for key, value in data.items():
        if isinstance(value, (np.int64, np.int32)):
            data[key] = int(value)
        elif isinstance(value, (np.float64, np.float32)):
            data[key] = float(value)
        elif isinstance(value, np.bool_):
            data[key] = bool(value)
        elif isinstance(value, np.ndarray):
            data[key] = value.tolist()
    return data

def load_data_from_collection(collection_name):
    """
    Загружает данные из коллекции MongoDB и преобразует их в DataFrame.
    :param db: Объект базы данных MongoDB.
    :param collection_name: Название коллекции.
    :return: DataFrame с данными и типами колонок.
    """
    collection = db[collection_name]
    data = list(collection.find())
    data = convert_object_id_to_string(data)
    df = pd.DataFrame(data)
    if not df.empty:
        
        df = df.set_index(df.columns[0], drop=True)  # Устанавливаем первый столбец как индекс
        id_columns = [col for col in df.columns if '_id' in col]
        df = df.drop(columns=id_columns)

    # Добавляем нумерацию записей
    df.insert(0, "№", range(1, len(df) + 1))
    return df, df.dtypes

def convert_input_data(data, types):
    """
    Преобразует данные в нужные типы на основе их исходных типов.
    :param data: Словарь с вводными данными.
    :param types: Словарь типов данных колонок.
    :return: Словарь с преобразованными данными или None в случае ошибки.
    """
    try:
        for key, value in data.items():
            if pd.api.types.is_integer_dtype(types[key]):
                data[key] = int(value)
            elif pd.api.types.is_float_dtype(types[key]):
                data[key] = float(value)
            elif pd.api.types.is_datetime64_any_dtype(types[key]):
                data[key] = pd.to_datetime(value).to_pydatetime()
            elif pd.api.types.is_string_dtype(types[key]):
                data[key] = str(value)
        return data
    except Exception as e:
        return None


def load_table_data(selected_table):
    """Загружает данные из выбранной коллекции MongoDB и преобразует их типы."""
    df, types = load_data_from_collection(selected_table)
    
    # Преобразуем float в int, если возможно
    for col in df.select_dtypes(include=['float']).columns:
        df[col] = df[col].astype('int', errors='ignore')

    df = df.astype('object')  # Преобразуем все столбцы в объектный тип для унификации
    return df, types
