from datetime import datetime
import pytz



moscow_timezone = pytz.timezone('Europe/Moscow')

# Получаем текущий день недели (1 - понедельник)
current_day = datetime.now(moscow_timezone).weekday() + 1

type_week = "Chet"  # Nechet


def change_week(type_week=type_week):
    # Получаем текущий день недели (0 - понедельник, 1 - вторник, и так далее)
    if current_day == 7:
        if type_week == "Chet":
            type_week = "Nechet"
            return type_week
        elif type_week == "Nechet":
            type_week = "chet"
            return type_week


def is_even_week() -> bool:
    # Предположим, что ваш учебный период начинается с понедельника
    # Если текущий день недели - понедельник, то текущая неделя четная
    pass


print(current_day)
change_week()
print(current_day)
