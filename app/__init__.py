from flask import Flask
from config_defaults import DevelopmentEnv, TESTINGENV # Repalce with "ProductionEnv" for Production

# define application 
def app(test_enabled=None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object('DevelopmentEnv')

    if test_enabled is not True:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_object('TESTINGENV')

    # Register Test page -- Remove after modules creation
    @app.route('/test_page')
    def test_page():
        return 'This is just a Test'

    return app

