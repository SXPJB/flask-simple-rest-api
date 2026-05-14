from app.database import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class PersonModel(db.Model):
    __tablename__ = 'person'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'surname': self.surname,
            'age': self.age
        }
