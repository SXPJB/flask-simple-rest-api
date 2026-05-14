from app.database import db
from app.infrastructure.models import PersonModel

class PersonRepository:
    def create(self, id, name, surname, age):
        person = PersonModel(id=id, name=name, surname=surname, age=age)
        db.session.add(person)
        db.session.commit()
        return person

    def get_all(self):
        return PersonModel.query.all()

    def get_by_id(self, id):
        return PersonModel.query.get(id)

    def update(self, id, name, surname, age):
        person = self.get_by_id(id)
        if person:
            person.name = name
            person.surname = surname
            person.age = age
            db.session.commit()
        return person

    def delete(self, id):
        person = self.get_by_id(id)
        if person:
            db.session.delete(person)
            db.session.commit()
            return True
        return False
