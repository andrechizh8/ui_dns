from dataclasses import dataclass
from faker import Faker
from typing import Literal
from model.utils.date_generator import date_generate
import random


@dataclass
class User:
    first_name: str
    last_name: str
    nickname: str
    random_email: str
    random_text: str
    city: Literal['Москва', 'Санкт-Петербург', 'Новосибирск', 'Краснодар', 'Екатеринбург',
    'Казань', 'Уфа', 'Нижний Новгород', 'Челябинск', 'Самара', 'Ростов-на-Дону',
    'Омск', 'Красноярск', 'Воронеж', 'Пермь', 'Волгоград', 'Владивосток']
    phone_model: str
    phone_memory: str
    eBook: str
    search_product: str
    question: str
    item: str
    date: str
    file: str


avatar = ["resources/1.png", "resources/2.png", "resources/3.png"]

faker = Faker('ru_RU')
current_user = User(first_name=faker.first_name(), last_name=faker.last_name(), nickname=f"{faker.job()}_008",
                    random_email=faker.email(), random_text=faker.text(), city="Москва", phone_model="Samsung",
                    phone_memory="64", eBook="Digma k2", file=random.choice(avatar), search_product="Смартфоны",
                    question="Оценка работы",
                    item="Интернет-магазин", date=date_generate())
