import redis
import json
import datetime


class MuseumApp:
    def __init__(self, redis_host='localhost', redis_port=6379, redis_db=2):
        self.redis = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db, decode_responses=True)

    def add_exhibit(self, exhibit_data):
        # Логіка додавання експонату
        ...

    def delete_exhibit(self, exhibit_id):
        exhibit_key = f'exhibit:{exhibit_id}'
        self.redis.delete(exhibit_key)

        # Отримання ключів осіб зі множини з Redis
        related_people_keys = self.redis.smembers(f'{exhibit_key}:related_people')
        # Проходимось по ключах
        for person_key in related_people_keys:
            self.redis.srem(f'{person_key}:related_exhibits', exhibit_key)

        print("Експонат успішно видалений.")

    def edit_exhibit(self, exhibit_id, new_data):
        # Логіка редагування експонату
        ...

    def view_exhibit_info(self, exhibit_id):
        # Логіка перегляду інформації про експонат
        ...

    def view_all_exhibits(self):
        # Логіка перегляду всіх експонатів
        ...

    def view_related_people(self, exhibit_id):
        from modules.vitalii.People import PeopleFacade

        facade = PeopleFacade()

        # Get from redis people who are connected to exhibit_id. Now it is an example
        facade.add_person('Vova')
        facade.add_person('Kolya')

        print(facade.get_people_names())

    def view_related_exhibits(self, person_name):
        # Логіка перегляду експонатів, пов'язаних з людиною
        ...

    def view_exhibits_by_category(self, category):
        # Логіка перегляду експонатів за категорією
        ...
