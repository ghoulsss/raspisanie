from datetime import datetime
import pytz
import json


class TypeWeek:
    days = {1: 'Понедельник',
            2: 'Вторник',
            3: 'Среда',
            4: 'Четверг',
            5: 'Пятница',
            6: 'Суббота',
            7: 'Воскресенье'}
    moscow_timezone = pytz.timezone('Europe/Moscow')
    current_day = days[datetime.now(moscow_timezone).weekday() + 1]  # Понедельник
    date = f"{datetime.now().day:02d}.{datetime.now().month:02d}"  # 19.01
    tomorrow_date = f"{datetime.now().day + 1:02d}.{datetime.now().month:02d}"  # 20.01

    @staticmethod
    def is_even_week(date=date) -> str:
        date_object = datetime.strptime(date, "%d.%m")

        week_number = date_object.isocalendar()[1]
        return 'Chet' if week_number % 2 == 0 else 'Nechet'


class ReadRasp:
    @staticmethod
    def pull_raspisanie(type_week, day, filename='2grupa.json'):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        schedule = data.get(type_week, {})
        sending_message = ''

        if day in ('Суббота', 'Воскресенье'):
            return 'Зачилься выходные же'

        monday_schedule = schedule.get(day, [])
        #monday_schedule = schedule.get('Среда', [])
        for i, lesson in enumerate(monday_schedule, start=1):
            lesson_time = lesson.get("Время")
            subject = lesson.get("Предмет", "")
            teacher = lesson.get("Преподаватель", "")
            lesson_type = lesson.get("Тип", "")
            classroom = lesson.get("Аудитория", "")

            if i != len(monday_schedule):
                if subject == 'Физ-ра':
                    sending_message += f"{i}) {lesson_time}, {subject}\n\n"
                else:
                    sending_message += f"{i}) {lesson_time}, {subject}, {teacher}, {lesson_type}, {classroom}\n\n"
            else:
                if subject == 'Физ-ра':
                    sending_message += f"{i}) {lesson_time}, {subject}"
                else:
                    sending_message += f"{i}) {lesson_time}, {subject}, {teacher}, {lesson_type}, {classroom}"

        return sending_message

    @staticmethod
    def pull_raspisanie_nedelya(type_week, filename='2grupa.json'):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        schedule = data.get(type_week, {})
        sending_message = 'Нечетная\n' if type_week == 'Nechet' else 'Четная\n'
        sending_message += ''

        # Перебираем дни недели
        days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
        for day in days_of_week:
            sending_message += f"{day}:\n"
            day_schedule = schedule.get(day, [])

            # Перебираем уроки в текущем дне
            for i, lesson in enumerate(day_schedule, start=1):
                lesson_time = lesson.get("Время")
                subject = lesson.get("Предмет", "")
                teacher = lesson.get("Преподаватель", "")
                lesson_type = lesson.get("Тип", "")
                classroom = lesson.get("Аудитория", "")
                if subject == 'Физ-ра':
                    sending_message += f"{i}) {lesson_time}, {subject}\n"
                else:
                    sending_message += f"{i}) {lesson_time}, {subject}, {teacher}, {lesson_type}, {classroom}\n"

            if day != 'Пятница':
                sending_message += "\n"

        return sending_message

    @staticmethod
    def pull_raspisanie_next_nedelya(type_week, filename='2grupa.json'):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        type_week = 'Nechet' if type_week == 'Chet' else 'Chet'
        schedule = data.get(type_week, {})
        sending_message = 'Нечетная\n' if type_week == 'Nechet' else 'Четная\n'
        sending_message += ''

        # Перебираем дни недели
        days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
        for day in days_of_week:
            sending_message += f"{day}:\n"
            day_schedule = schedule.get(day, [])

            # Перебираем уроки в текущем дне
            for i, lesson in enumerate(day_schedule, start=1):
                lesson_time = lesson.get("Время")
                subject = lesson.get("Предмет", "")
                teacher = lesson.get("Преподаватель", "")
                lesson_type = lesson.get("Тип", "")
                classroom = lesson.get("Аудитория", "")
                if subject == 'Физ-ра':
                    sending_message += f"{i}) {lesson_time}, {subject}\n"
                else:
                    sending_message += f"{i}) {lesson_time}, {subject}, {teacher}, {lesson_type}, {classroom}\n"

            if day != 'Пятница':
                sending_message += "\n"

        return sending_message


#print(TypeWeek.current_day, TypeWeek.date)
# print(ReadRasp.pull_raspisanie(TypeWeek.is_even_week(TypeWeek.tomorrow_date), TypeWeek.days[1]))
