from datetime import datetime
import pytz


class TypeWeek:
    moscow_timezone = pytz.timezone('Europe/Moscow')
    # Получаем текущий день недели (1 - понедельник)
    current_day = datetime.now(moscow_timezone).weekday() + 1
    type_week = "Chet"  # Nechet
    translate_type_week = "Четная" if type_week == 'Chet' else "Нечетная"

    @classmethod
    def check_type_week(cls):
        # Получаем текущий день недели (0 - понедельник, 1 - вторник, и так далее)
        if cls.current_day == 7:
            if cls.type_week == "Chet":
                cls.type_week = "Nechet"
                return cls.type_week
            elif cls.type_week == "Nechet":
                cls.type_week = "Chet"
                return cls.type_week
