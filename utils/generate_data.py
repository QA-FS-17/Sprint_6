from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker('ru_RU')

def generate_order_data():
    metro_stations = ["Алексеевская", "Бабушкинская", "ВДНХ", "Полежаевская", "Сокольники"]
    return {
        'name': fake.first_name(),
        'lastname': fake.last_name(),
        'address': fake.street_address(),
        'metro': random.choice(metro_stations),
        'phone': f"+79{random.randint(100000000, 999999999)}",
        'date': (datetime.now() + timedelta(days=3)).strftime("%d.%m.%Y"),
        'rental_period': random.choice(["сутки", "двое суток"]),
        'color': random.choice(["black", "grey"]),
        'comment': fake.text(max_nb_chars=50)
    }