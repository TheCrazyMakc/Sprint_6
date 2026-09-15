import random

from datetime import date, timedelta


# Генерируем словарь для заполнения формы заказа
def generate_order_info():
    metro_stations = ["Бульвар Рокоссовского", "Чистые пруды", "Спортивная",
                      "Преображенская площадь", "Сокольники", "Комсомольская",
                      "Новогиреево", "Алтуфьево", "Новокузнецкая"]
    colors = ['black', 'grey']
    rental_durations = ['сутки', 'двое суток', 'трое суток', 'четверо суток',
                        'пятеро суток', 'шестеро суток', 'семеро суток']

    return {
        'name': random.choice(['Данна', 'Паша', 'Евлампий', 'Вася']),
        'surname': random.choice(['Жарк', 'Сушкин', 'Вальдемарович', 'Пупкин']),
        'address': random.choice(['Тверская', 'Гражданская',
                                  'Город, улица, дом', 'Тудым Сюдым']),
        'metro': random.choice(metro_stations),
        'phone': str(random.randint(12345678901, 98989898989)),
        'date': (date.today() + timedelta(
            days=random.randint(1, 7))).strftime('%d.%m.%Y'),
        'duration': random.choice(rental_durations),
        'color': random.choice(colors),
        'comment': random.choice(['', 'позвонить за час', 'оставить у двери',
                                  'домофон не работает'])
    }
