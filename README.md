Flask API Development
===========


Flask application implementing a REST API to serve the content of the colors.json file


------------

Installation
===========================

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
===========================
```
    python src/wsgi.py
```

RESTful API Documentation
=========================
Navigate to the posted URL in your terminal (http://127.0.0.1:5000/) to access Swagger doc in order to test the API.

Run Tests
===========================

Run the test suite:

```
    pytest -v
```   

See the test coverage report through:

```
    pytest -v --cov=app.color
```    