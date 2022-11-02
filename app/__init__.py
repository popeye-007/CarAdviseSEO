from flask import Flask, g, url_for, redirect, render_template
from .config_defaults import DEVENV, TESTINGENV 

# define application 
def create_app(test_enabled=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(DEVENV())

    if test_enabled is not True:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_object(TESTINGENV())

    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404
    
    # Register Test page -- Remove after modules creation
    @app.route('/test_page')
    def test_page():
        return 'This is just a Test'

    @app.route('/')
    def index():
        return render_template('index.html')

    return app