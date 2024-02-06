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
