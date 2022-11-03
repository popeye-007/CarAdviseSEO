from flask import Flask, g, url_for, redirect, render_template
from .config_defaults import DEVENV, TESTINGENV 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# define application as a function to use different 
# configurations for different environments
def create_app(test_enabled=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(DEVENV())

    if test_enabled is not True:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_object(TESTINGENV())

    # http error Handlers 
    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404
    
    # Test page -- Remove after modules creation
    @app.route('/test_page')
    def test_page():
        return 'This is just a Test'

    @app.route('/')
    def index():
        return render_template('index.html')

    return app


app = create_app()
# Application Extention for DB connection
db = SQLAlchemy(app)
# initiate DB connection, the KEY 'SQLALCHEMY_DATABASE_URI'
# comes from the selected config
db.init_app(app)

# Buid Database tables:
with app.app_context():
    db.create_all()

migrate = Migrate(app,db)