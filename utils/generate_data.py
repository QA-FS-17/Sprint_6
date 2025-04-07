import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('ru_RU')


def generate_order_data():
    metro_stations = ["Алексеевская", "Бабушкинская", "ВДНХ", "Полежаевская", "Сокольники"]
    valid_addresses = [
        "ул. Тверская, 7",
        "ул. Арбат, 1",
        "пр. Мира, 101",
        "Ленинский проспект, 32",
        "ул. Покровка, 47"
    ]

    return {
        'name': fake.first_name(),
        'lastname': fake.last_name(),
        'address': random.choice(valid_addresses),
        'metro': random.choice(metro_stations),
        'phone': f"+79{random.randint(100000000, 999999999)}",
        'date': (datetime.now() + timedelta(days=3)).strftime("%d.%m.%Y"),
        'rental_period': random.choice(["сутки", "двое суток"]),
        'color': random.choice(["black", "grey"]),
        'comment': fake.text(max_nb_chars=50)
    }