from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker("ru_RU")


def generate_order_data(include_optional=True):
    # Генерация обязательных полей
    data = {
        "name": fake.first_name(),
        "surname": fake.last_name(),
        "address": fake.address().replace("\n", ", "),
        "phone": fake.phone_number(),
        "metro": random.choice(["Черкизовская", "Сокольники", "Красносельская", "Комсомольская"]),
        "delivery_date": (datetime.now() + timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d"),
        "rental_period": random.choice(["сутки", "двое суток", "трое суток", "четверо суток"]),
        "color": random.choice(["black", "grey"]),  # Для чекбоксов
    }

    # Опциональные поля
    if include_optional:
        data.update({
            "comment": fake.text(max_nb_chars=100),
            "phone_extension": fake.random_number(digits=3),
        })

    return data


def generate_invalid_order_data():
    """Генерация специально некорректных данных для негативных тестов"""
    return {
        "name": " " * 5,  # Пробелы
        "surname": fake.last_name() + "!",  # Спецсимвол
        "address": "A" * 300,  # Слишком длинный
        "phone": "not_a_phone",  # Не номер
        "delivery_date": "2020-01-01",  # Прошедшая дата
    }