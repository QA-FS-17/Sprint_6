from faker import Faker

fake = Faker("ru_RU")

def generate_order_data():
    return {
        "name": fake.first_name(),
        "surname": fake.last_name(),
        "address": fake.address().replace("\n", ", "),
        "phone": fake.phone_number(),
        "delivery_date": "2024-12-31",
        "comment": fake.text(max_nb_chars=200),  # Ограничиваем длину текста
    }