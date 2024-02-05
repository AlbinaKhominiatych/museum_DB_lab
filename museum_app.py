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
        # Логіка видалення експонату
        ...

    def edit_exhibit(self, exhibit_id, new_data):
        # Логіка редагування експонату
        ...

    def view_exhibit_info(self, exhibit_id):
        # Логіка перегляду інформації про експонат
        if self.redis.hexists('exhibits', exhibit_id):
            return json.loads(self.redis.hget('exhibits', exhibit_id))
        else:
            # ни чего не возвращаем, что бы не было ошибка при
            # проверке возвращаемых данных (if view_exhibit_info(exhibit_id):)
            # будет возвращен None, значит экспонат не найден
            print(f'Exhibit with id <{exhibit_id}> not found')

    def view_all_exhibits(self):
        # Логіка перегляду всіх експонатів
        ...

    def view_related_people(self, exhibit_id):
        # Логіка перегляду людей, пов'язаних з експонатом
        ...

    def view_related_exhibits(self, person_name):
        # Логіка перегляду експонатів, пов'язаних з людиною
        ...

    def view_exhibits_by_category(self, category):
        # Логіка перегляду експонатів за категорією
        ...
