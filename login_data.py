from database import get_database_login

def add_auth_data():
    db_login = get_database_login()

    # Данные для добавления
    buyers = [
        {"email": "trotsky@example.com", "password": "Vladislav2024"},
        {"email": "aboltin@example.com", "password": "Moisei2024"},
        {"email": "begunk@example.com", "password": "Karina2024"},
        {"email": "anisk@example.com", "password": "Denis2024"},
        {"email": "guzarv@example.com", "password": "Kirill2024"},
        {"email": "vorobey@example.com", "password": "Anton2024"},
        {"email": "kudosh@example.com", "password": "Darya2024"},
        {"email": "zagorec@example.com", "password": "Alexandra2024"},
        {"email": "klimuk@example.com", "password": "Pavel2024"},
        {"email": "zaycev@example.com", "password": "Nikita2024"}
    ]

    customers = [
        {"email": "kudrickaya@example.com", "password": "Valeria2024"},
        {"email": "matyukevich@example.com", "password": "Alexandra2024"},
        {"email": "mishp@example.com", "password": "Angelina2024"},
        {"email": "panasenya@example.com", "password": "Maxim2024"},
        {"email": "chepelevich@example.com", "password": "Arseniy2024"},
        {"email": "poskannoi@example.com", "password": "Ivan2024"},
        {"email": "malyavsky@example.com", "password": "Alexander2024"},
        {"email": "laskov@example.com", "password": "Artem2024"},
        {"email": "lyskovets@example.com", "password": "Nikita2024"},
        {"email": "terekhova@example.com", "password": "Alina2024"}
    ]

    dealers = [
        {"email": "stalin@example.com", "password": "Iosif2024"},
        {"email": "putin@example.com", "password": "Vladimir2024"},
        {"email": "kim@example.com", "password": "Kim2024"},
        {"email": "trump@example.com", "password": "Donald2024"},
        {"email": "lenin@example.com", "password": "Vladimir2024"}
    ]

    # Добавление данных в коллекции
    db_login.buyers.insert_many(buyers)
    db_login.customers.insert_many(customers)
    db_login.dealers.insert_many(dealers)
    print("Данные успешно добавлены!")

# Запуск скрипта
add_auth_data()
