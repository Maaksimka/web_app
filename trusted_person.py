from pymongo import MongoClient

# Подключение к MongoDB
def get_database():
    """Возвращает подключение к базе данных auto_com."""
    uri = "mongodb+srv://maxpanasenia30:zPQNwI9a7B7QY5Vz@somth.z5510.mongodb.net/?retryWrites=true&w=majority"  # Замените на ваш URI
    client = MongoClient(uri)
    return client['auto_comis']

# Экспортируем объект базы данных
db = get_database()

# Коллекция Final_contract
collection = db['Final_contract']

# Обновляем все записи: устанавливаем trusted_person на "Автокомис"
update_result = collection.update_many({}, {"$set": {"trusted_person": "Автокомис"}})

# Выводим результат обновления
print(f"Обновлено документов: {update_result.modified_count}")
