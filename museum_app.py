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
        if self.redis.hexists('exhibits', exhibit_id):
            return json.loads(self.redis.hget('exhibits', exhibit_id))
        else:
            # ни чего не возвращаем, что бы не было ошибка при
            # проверке возвращаемых данных (if view_exhibit_info(exhibit_id):)
            # будет возвращен None, значит экспонат не найден
            print(f'Exhibit with id <{exhibit_id}> not found')

    def view_all_exhibits(self):
        # Логіка перегляду всіх експонатів
        all_exhibits = self.redis.hgetall('exhibits')
        for key, value in all_exhibits.items():
            print(f"{key}: {value}")

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
        # Get a list of all exhibit keys
        exhibit_keys = self.redis.keys('exhibit:*')
        filtered_exhibits = []

        for key in exhibit_keys:
            # For each key, get the hash representing the exhibit
            exhibit = self.redis.hgetall(key)
            # Check if the exhibit's category matches the given category
            if exhibit.get('category') == category:
                filtered_exhibits.append(exhibit)

        # Return the list of exhibits filtered by category as a JSON string
        return json.dumps(filtered_exhibits, ensure_ascii=False)
