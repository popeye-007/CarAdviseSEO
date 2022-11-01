# CarAdviseSEO
Building a small app to read and update SEO data for a selected Car Service

## Technologies used:
* Python 3.10 - with the following core libraries
    * Flask
    * Flask-WTF
    https://pypi.org/project/Flask-WTF/
    ```
    pip install Flask-WTF
    ```
    * flask-sqlalchemy
    https://pypi.org/project/flask-sqlalchemy/
    ```
    $ pip install -U Flask-SQLAlchemy
    ```
* BootStrap 5
* Package Managers:
    * pip


## Folder Strucure:
```
~/<someFolderName>
    |-- run.py                  # The entry point and the value of FLASK_APP environment variable
    |-- config.py               # Defines app configuration
    |-- requirement.txt
    |__ /.env                   # Virtual Environment
    |__ /app                
        |-- __init__.py
        |-- /module_one         # Our Application Module
            |-- __init__.py
            |-- controllers.py  # Handles the app routing like login, logout and register
            |-- models.py       # Defines DB tables
            |-- forms.py        # Defines application forms (sign in,sign out, data update, data addition,...)
         |__ /templates
            |-- base.html
            |-- 404.html
            |-- index.html
            |__ /module_one
                |-- hello.html
        |__ /static             # CSS files, Javascripts files
        |__ ..
        |__ .
    |__ ..
    |__ .
```

### config.py template
    # Statement for enabling the development environment
    DEBUG = True

    # Define the application directory
    import os
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

    # Define the database - we are working with
    # SQLite for this example
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    DATABASE_CONNECT_OPTIONS = {}

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED     = True

    # Use a secure, unique and absolutely secret key for
    # signing the data. 
    CSRF_SESSION_KEY = "secret"

    # Secret key for signing cookies
    SECRET_KEY = "secret"

### run.py template
    # Run a test server.
    from app import app
    app.run(host='0.0.0.0', port=8080, debug=True)