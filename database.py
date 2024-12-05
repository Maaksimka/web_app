from pymongo import MongoClient

# Подключение к MongoDB
def get_database():
    """Возвращает подключение к базе данных auto_com."""
    uri = "mongodb+srv://maxpanasenia30:zPQNwI9a7B7QY5Vz@somth.z5510.mongodb.net/?retryWrites=true&w=majority"  # Замените на ваш URI
    client = MongoClient(uri)  # Просто передаем URI без ssl=False
    return client['auto_comis']

# Экспортируем объект базы данных
db = get_database()


def get_database_login():
    """Возвращает подключение к базе данных auto_com."""
    uri = "mongodb+srv://maxpanasenia30:zPQNwI9a7B7QY5Vz@somth.z5510.mongodb.net/?retryWrites=true&w=majority"  # Замените на ваш URI
    client = MongoClient(uri)  # Просто передаем URI без ssl=False
    return client['auto_comis_login']

# Экспортируем объект базы данных


login_db = get_database_login()
