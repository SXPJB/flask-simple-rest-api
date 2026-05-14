from flask import Blueprint, request, jsonify
from app.services.person_service import PersonService

person_bp = Blueprint('person', __name__)
person_service = PersonService()

@person_bp.route('', methods=['POST'])
def create():
    data = request.get_json()
    if not data or not all(k in data for k in ('name', 'surname', 'age')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    person = person_service.create_person(data)
    return jsonify(person), 201

@person_bp.route('', methods=['GET'])
def get_all():
    persons = person_service.get_all_persons()
    return jsonify(persons), 200

@person_bp.route('/<person_id>', methods=['GET'])
def get_one(person_id):
    person = person_service.get_person(person_id)
    if not person:
        return jsonify({'error': 'Person not found'}), 404
    return jsonify(person), 200

@person_bp.route('/<person_id>', methods=['PUT'])
def update(person_id):
    data = request.get_json()
    person = person_service.update_person(person_id, data)
    if not person:
        return jsonify({'error': 'Person not found'}), 404
    return jsonify(person), 200

@person_bp.route('/<person_id>', methods=['DELETE'])
def delete(person_id):
    success = person_service.delete_person(person_id)
    if not success:
        return jsonify({'error': 'Person not found'}), 404
    return jsonify({'message': 'Person deleted successfully'}), 200
