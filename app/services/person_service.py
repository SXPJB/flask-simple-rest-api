import uuid
from app.infrastructure.person_repository import PersonRepository

class PersonService:
    def __init__(self):
        self.repository = PersonRepository()

    def create_person(self, data):
        person_id = str(uuid.uuid4())
        self.repository.create(
            person_id,
            data['name'],
            data['surname'],
            data['age']
        )
        return self.get_person(person_id)

    def get_all_persons(self):
        persons = self.repository.get_all()
        return [self._map_to_dict(p) for p in persons]

    def get_person(self, person_id):
        person = self.repository.get_by_id(person_id)
        if person:
            return self._map_to_dict(person)
        return None

    def update_person(self, person_id, data):
        existing = self.get_person(person_id)
        if not existing:
            return None
        
        name = data.get('name', existing['name'])
        surname = data.get('surname', existing['surname'])
        age = data.get('age', existing['age'])
        
        self.repository.update(person_id, name, surname, age)
        return self.get_person(person_id)

    def delete_person(self, person_id):
        existing = self.get_person(person_id)
        if not existing:
            return False
        self.repository.delete(person_id)
        return True

    def _map_to_dict(self, person):
        return person.to_dict()
