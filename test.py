import json


class ReadRasp:
    @staticmethod
    def read_raspisanie(filename='2grupa.json', type_week=None, day=1)->None:
        # Открываем файл на чтение
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Теперь переменная 'data' содержит данные из файла JSON

        # Пример доступа к данным
        schedule = data.get("Chet", {})  # Получаем расписание для четной недели (если есть)
        if schedule:
            monday_schedule = schedule.get("Понедельник", [])  # Получаем расписание на понедельник для четной недели
            for lesson in monday_schedule:
                lesson_time = lesson.get("Время")
                subject = lesson.get("Предмет", "")
                teacher = lesson.get("Преподаватель", "")
                lesson_type = lesson.get("Тип", "")
                classroom = lesson.get("Аудитория", "")

                print(f"{lesson_time}, {subject}, {teacher}, {lesson_type}, {classroom}")
