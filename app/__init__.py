from flask import Flask
from app.config import Config
from app.database import db
from app.controllers.s3_controller import s3_bp
from app.controllers.health_controller import health_bp
from app.controllers.person_controller import person_bp
from app.services.s3_service import S3Service

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(s3_bp, url_prefix='/s3')
    app.register_blueprint(health_bp)
    app.register_blueprint(person_bp, url_prefix='/api/v1/person')

    # Initialize services
    with app.app_context():
        db.create_all()
        s3_service = S3Service()
        s3_service.ensure_bucket_exists()

    return app
