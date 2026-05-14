from flask import Blueprint, request, jsonify, send_file
from app.services.s3_service import S3Service
import io

s3_bp = Blueprint('s3', __name__)
s3_service = S3Service()

@s3_bp.route('/all', methods=['GET'])
def list_files():
    try:
        files = s3_service.list_files()
        return jsonify({"files": files}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@s3_bp.route('', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    try:
        s3_service.upload_file(file, file.filename)
        return jsonify({"message": f"File {file.filename} uploaded successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@s3_bp.route('/<path:id>', methods=['GET'])
def download_file(id):
    try:
        file_content = s3_service.download_file(id)
        if file_content is None:
            return jsonify({"error": "File not found"}), 404
        
        return send_file(
            io.BytesIO(file_content),
            download_name=id,
            as_attachment=True
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@s3_bp.route('/<path:id>', methods=['DELETE'])
def delete_file(id):
    try:
        success = s3_service.delete_file(id)
        if not success:
            return jsonify({"error": "File not found"}), 404
        return jsonify({"message": f"File {id} deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
