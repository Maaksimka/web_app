import streamlit as st
from datetime import datetime
from database import db, login_db

# Сопоставление ролей с коллекциями в базе данных
ROLE_TO_COLLECTION = {
    "Дилер": {"db": "Dealers", "login_db": "dealers"},
    "Клиент": {"db": "Customers", "login_db": "customers"},
    "Покупатель": {"db": "Buyers", "login_db": "buyers"}
}

# Словарь для замены названий полей
FIELD_LABELS = {
    "fio": "ФИО",
    "email": "Почта",
    "phone_number": "Номер телефона",
    "date_of_birth": "Дата рождения",
    "registration_date": None  # Поле не отображается
}

# Генерация уникального customer_id или buyer_id
def generate_unique_id(collection, id_field):
    last_doc = db[collection].find_one({}, sort=[(id_field, -1)])
    new_id = 1 if not last_doc else int(last_doc[id_field]) + 1
    while db[collection].find_one({id_field: new_id}):  # ID теперь int
        new_id += 1
    return new_id


# Отрисовка формы для ввода данных
def render_form(fields, prefix="form"):
    """
    Поля рендерятся динамически на основе структуры коллекции.
    """
    data = {}
    for field in fields:
        if field in {"_id", "customer_id", "buyer_id", "registration_date"}:  # Пропускаем служебные поля
            continue

        label = FIELD_LABELS.get(field, field)  # Получаем название из словаря или используем исходное
        if label:  # Отображаем только те поля, которые имеют метку
            data[field] = st.text_input(f"{label}:", key=f"{prefix}_{field}")
    return data


# Авторизация
def login(role):
    st.subheader(f"Авторизация для роли: {role}")
    email = st.text_input("Email")
    password = st.text_input("Пароль", type="password")

    if st.button("Войти"):
        collection = ROLE_TO_COLLECTION.get(role)["login_db"]
        if not collection:
            st.error("Роль не распознана.")
            return

        user = login_db[collection].find_one({"email": email, "password": password})
        if user:
            st.success(f"Добро пожаловать, {role}!")
            st.session_state["user"] = user
            st.session_state["role"] = role
            st.experimental_rerun()
        else:
            st.error("Неверные данные для входа.")


# Регистрация
def register(role):
    st.subheader(f"Регистрация для роли: {role}")
    email = st.text_input("Email", key="register_email_input")
    password = st.text_input("Пароль", type="password", key="register_password_input")
    login_collection = ROLE_TO_COLLECTION.get(role)["login_db"]
    main_collection = ROLE_TO_COLLECTION.get(role)["db"]

    if "form_visible" not in st.session_state:
        st.session_state["form_visible"] = False

    if st.button("Проверить"):
        if login_db[login_collection].find_one({"email": email}):
            st.error("Пользователь с таким email уже зарегистрирован.")
        else:
            st.success("Email доступен для регистрации.")
            st.session_state["register_email"] = email
            st.session_state["register_password"] = password
            st.session_state["form_visible"] = True

    if st.session_state.get("form_visible", False):
        st.subheader("Заполните данные для завершения регистрации")
        id_field = "customer_id" if role == "Клиент" else "buyer_id"
        unique_id = generate_unique_id(main_collection, id_field)

        collection_structure = db[main_collection].find_one()
        if not collection_structure:
            st.error("Структура коллекции пуста. Обратитесь к администратору.")
            return

        fields = list(collection_structure.keys())[2:]  # Начинаем с третьего поля
        user_data = render_form(fields, prefix="register")

        # Автоматическое заполнение даты регистрации
        user_data["registration_date"] = datetime.now().strftime("%Y-%m-%d")

        if st.button("Завершить регистрацию"):
            user_data["email"] = st.session_state["register_email"]
            user_data["password"] = st.session_state["register_password"]
            user_data[id_field] = unique_id

            db[main_collection].insert_one(user_data)
            login_db[login_collection].insert_one({"email": user_data["email"], "password": user_data["password"]})

            st.success("Регистрация завершена! Теперь вы можете войти.")
            st.session_state["form_visible"] = False
            st.experimental_rerun()


# Основная логика
def mainer():
    st.title("Система авторизации и регистрации")

    if "user" not in st.session_state:
        role = st.radio("Выберите вашу роль:", ["Дилер", "Клиент", "Покупатель"])

        if role == "Дилер":
            login(role)
        elif role in {"Клиент", "Покупатель"}:
            action = st.radio(f"{role}: Выберите действие", ["Авторизация", "Регистрация"])
            if action == "Авторизация":
                login(role)
            elif action == "Регистрация":
                register(role)
    else:
        st.sidebar.success(f"Вы вошли как {st.session_state['role']}.")
        if st.sidebar.button("Выйти"):
            del st.session_state["user"]
            del st.session_state["role"]
            st.experimental_rerun()
