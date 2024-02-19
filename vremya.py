from datetime import datetime
import pytz
import json


class TypeWeek:
    days = {1: 'Понедельник',
            2: 'Вторник',
            3: 'Среда',
            4: 'Четверг',
            5: 'Пятница'}
    moscow_timezone = pytz.timezone('Europe/Moscow')
    # Получаем текущий день недели (1 - понедельник)
    number_of_day = datetime.now(moscow_timezone).weekday() + 1
    day_month = datetime.now().day
    type_week = ["Chet", day_month]

    #translate_type_week = "Четная" if type_week == 'Chet' else "Нечетная"

    @classmethod
    def check_type_week(cls):
        if cls.number_of_day == 7 and cls.type_week[1] != :
            if cls.type_week == "Chet":
                cls.type_week = "Nechet"
                return cls.type_week
            elif cls.type_week == "Nechet":
                cls.type_week = "Chet"
                return cls.type_week
    @classmethod
    def change_type_week(cls):
