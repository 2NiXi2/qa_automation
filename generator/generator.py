import random

from data.data import Person, Color, Date

from faker import Faker

faker_ru = Faker('ru_Ru')
faker_en = Faker('En')
Faker.seed()
def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + '' + faker_ru.last_name() + '' + faker_ru.middle_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(15, 85),
        salary=random.randint(100, 15000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),
    )

def generated_file():
    path = rf"D:\PYcharm\qa_automation\testfile{random.randint(0, 888)}.txt"
    file = open(path, 'w+')
    file.write(f"Hallo world{random.randint(0, 126354)}")
    return path, file.name

def generated_subject():
    subjects = [
        "Hindi", "English", "Maths", "Physics", "Chemistry",
        "Biology", "Computer Science", "Commerce", "Accounting",
        "Economics", "Arts", "Social Studies", "History", "Civics"]
    return random.choice(subjects)

def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black",
                    "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )

def generated_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time='12:00'
    )