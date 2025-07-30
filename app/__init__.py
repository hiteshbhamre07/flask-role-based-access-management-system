from flask import Flask
from config import Config
from .models.auth import User, Role
from .extensions import db
from flask_security import SQLAlchemySessionUserDatastore, Security
from flask_mailman import Mail
import logging
from logging.handlers import RotatingFileHandler

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Configure mail settings 
    app.config['MAIL_SERVER'] = 'mail.techtradesystems.com'
    app.config['MAIL_PORT'] = 465   #587
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = 'enquiry@techtradesystems.com'
    app.config['MAIL_PASSWORD'] = 'EnqR2@Tts$$'
    app.config['MAIL_USE_TLS'] = True
    mail = Mail(app)

 

    # Initialize Flask extensions here
    db.init_app(app)
    user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
    security = Security(app, user_datastore)

    # Set up error logging
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)

 

    with app.app_context():
        db.create_all()

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    

    
    #from app.auth import bp as auth_bp
    #app.register_blueprint(auth_bp, url_prefix='/auth')
    

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app