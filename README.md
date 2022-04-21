Flask API Development
===========


Flask application implementing a REST API to serve the content of the colors.json file


------------

1 - Installation (Guest OS approach)
===========================

Create a virtual environment:

    # Linux/MacOs
    python3 -m venv venv-wc #create
    source venv-wc/bin/activate #activate
    
    # Windows
    python -m venv venv-wc #create
    venv-wc\Scripts\activate.bat #activate

Install version using the following commands:

```
    git clone https://github.com/lcdcustodio/flask_api.git
    cd flask_api
    pip install -r requirements.txt (to get the dependencies)
```    

Next, initialize the database through:

```
    python src/db_init.py
```

In order to load colors.json into database

Launch the server:

```
    python src/wsgi.py
```

RESTful API Documentation
=========================
Navigate to the posted URL in your terminal to access Swagger doc in order to test the API.

Run Tests
===========================

Run the test suite:

```
    pytest -v
    pytest -v --cov=app.color  #test coverage
```   

See the test coverage report:

```
    ----------- coverage: platform win32, python 3.9.1-final-0 -----------
    Name                          Stmts   Miss  Cover
    -------------------------------------------------
    src\app\color\__init__.py         6      0   100%
    src\app\color\controller.py      34      0   100%
    src\app\color\model.py           14      1    93%
    src\app\color\schema.py           4      0   100%
    src\app\color\service.py         81      2    98%
    -------------------------------------------------
    TOTAL                           139      3    98%
```    


2 - Installation (Container approach using podman)
===========================

Deployment and running in a containerized environment, using podman

```
    git clone https://github.com/lcdcustodio/flask_api.git
    cd flask_api
    sudo buildah bud -t flask_api .
    sudo podman run --rm -it -p 5000:5000 flask_api
``` 

3 - Installation (Container approach using docker)
===========================

Deployment and running in a containerized environment, using docker

```
    git clone https://github.com/lcdcustodio/flask_api.git
    cd flask_api
    docker build -t flask_api .
    docker run -p 5000:5000 flask_api
``` 
