from flask import Blueprint, jsonify

health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@health_bp.route('/ready', methods=['GET'])
def ready_check():
    return jsonify({"status": "ready"}), 200
