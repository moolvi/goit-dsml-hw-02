from faker import Faker
from random import randint, choice

from appdata_mongodb import *

NUMBER = 10

def generate_fake_data(number = NUMBER) -> tuple():
    fake_data = Faker('uk-UA')
    for_data = []
    for _ in range(number):
        for_data.append(
            {
                "name": choice(NICKNAME),
                "age": randint(0, 18),
                "features": fake_data.text().split()[0:randint(0, 5):1],
            })
    
    return tuple(for_data)