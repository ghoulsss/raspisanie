import requests
import psycopg2
from bs4 import BeautifulSoup

try:
    conn = psycopg2.connect(dbname='raspisanie_db', user='raspisanie', password='root', host='localhost')
    print("Connected to raspisanie_db")
except psycopg2.DatabaseError as r:
    print('Не подключился к бд...', r)


def get_kgasu():
    url = 'https://www.kgasu.ru/student/raspisanie-zanyatiy/'

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    week_type_element = soup.find('span', class_='kcolor')

    if week_type_element:
        week_type = week_type_element.get_text(strip=True)
        return week_type


class Vremya:
    days_of_week = {
        1: "Понедельник",
        2: "Вторник",
        3: "Среда",
        4: "Четверг",
        5: "Пятница",
        6: "Суббота",
        7: "Воскресенье"
    }
    url = 'http://worldtimeapi.org/api/timezone/Europe/Moscow'

    @classmethod
    def get_today(cls):
        try:
            response = requests.get(cls.url)
            response.raise_for_status()
            data = response.json()

            day_of_week_number = data['day_of_week']
            current_day = cls.days_of_week.get(day_of_week_number, "Неизвестный день")

            return current_day

        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса: {e}")
            return None

    @classmethod
    def get_tomorrow(cls):
        try:
            response = requests.get(cls.url)
            response.raise_for_status()
            data = response.json()

            day_of_week_number = data['day_of_week']
            tomorrow_number = (day_of_week_number + 1) % 7
            tomorrow_day = cls.days_of_week.get(tomorrow_number, "Неизвестный день")

            return tomorrow_day

        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса: {e}")
            return None


class Raspisanie:
    @staticmethod
    def pull_raspisanie():
        day = Vremya.get_today()
        if day in ("Суббота", "Воскресенье"):
            return 'Выходные'
        kgasu_type_week = get_kgasu()

        with conn.cursor() as curs:
            curs.execute(f"""SELECT d.day_name, c.class_name, s.class_time, wt.type_name, s.class_order
            FROM schedule s
            JOIN days d ON s.day_id = d.id
            JOIN classes c ON s.class_id = c.id
            JOIN week_types wt ON s.week_type_id = wt.id
            WHERE d.day_name = '{day}' AND wt.type_name = '{kgasu_type_week}'
            ORDER BY s.class_order;
            """)
            raspisanie = curs.fetchall()
            marked_rasp = '\n'.join([f'{r[2].strftime('%H:%M')} {r[1]}' for r in raspisanie])
            return marked_rasp

    @staticmethod
    def pull_raspisanie_tomorrow():
        day = Vremya.get_tomorrow()

        if day in ("Суббота", "Воскресенье"):
            return 'Выходные'
        kgasu_type_week = get_kgasu()

        with conn.cursor() as curs:
            curs.execute(f"""SELECT d.day_name, c.class_name, s.class_time, wt.type_name, s.class_order
            FROM schedule s
            JOIN days d ON s.day_id = d.id
            JOIN classes c ON s.class_id = c.id
            JOIN week_types wt ON s.week_type_id = wt.id
            WHERE d.day_name = '{day}' AND wt.type_name = '{kgasu_type_week}'
            ORDER BY s.class_order;
            """)
            raspisanie = curs.fetchall()
            marked_rasp = '\n'.join([f'{r[2].strftime('%H:%M')} {r[1]}' for r in raspisanie])
            return marked_rasp


# print(Raspisanie.pull_raspisanie())
# print(Vremya.time_in_moscow())
# Raspisanie.pull_raspisanie()
# print(get_joke())
