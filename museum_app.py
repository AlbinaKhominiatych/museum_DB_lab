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
        if not self.redis.hexists('exhibits', exhibit_id):
            print("Експонат не знайдено.")
            return
        stored_data = self.redis.hget('exhibits', exhibit_id)
        # Переконуємось, що збережені дані не є пустими та можуть бути декодовані як JSON
        if stored_data:
            try:
                exhibit_data = json.loads(stored_data)
            except json.JSONDecodeError:
                print("Помилка декодування даних експонату.")
                return
        else:
            print("Дані експонату відсутні або пошкоджені.")
            return

        # Оновлюємо дані експонату новими значеннями
        for key, value in new_data.items():
            if value:  # Переконуємось, що значення не є пустим перед оновленням
                exhibit_data[key] = value

        # Зберігаємо оновлені дані назад у Redis
        self.redis.hset('exhibits', exhibit_id, json.dumps(exhibit_data))
        print("Інформація про експонат оновлена.")

    def view_exhibit_info(self, exhibit_id):
        # Логіка перегляду інформації про експонат
        ...

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
