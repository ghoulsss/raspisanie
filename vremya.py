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
    current_day = days[datetime.now(moscow_timezone).weekday() + 1]  # Понедельник
    date = f"{datetime.now().day:02d}.{datetime.now().month:02d}"  # 19.01

    @staticmethod
    def is_even_week(date=date):
        date_object = datetime.strptime(date, "%d.%m")

        week_number = date_object.isocalendar()[1]
        return 'Chet' if week_number % 2 == 0 else 'Nechet'


class ReadRasp:
    @staticmethod
    def pull_raspisanie(type_week, day, filename='2grupa.json'):
        # Открываем файл на чтение
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Теперь переменная 'data' содержит данные из файла JSON

        # Пример доступа к данным
        schedule = data.get(type_week, {})  # Получаем расписание для четной недели (если есть)
        sending_message = ''
        monday_schedule = schedule.get(day, [])  # Получаем расписание на понедельник для четной недели
        for lesson in monday_schedule:
            lesson_time = lesson.get("Время")
            subject = lesson.get("Предмет", "")
            teacher = lesson.get("Преподаватель", "")
            lesson_type = lesson.get("Тип", "")
            classroom = lesson.get("Аудитория", "")

            sending_message += f"{lesson_time}, {subject}, {teacher}, {lesson_type}, {classroom}\n"
        print(sending_message)


ReadRasp.pull_raspisanie(TypeWeek.is_even_week(), TypeWeek.current_day)