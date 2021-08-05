from app.color.model import Color
from flask_sqlalchemy import SQLAlchemy

def test_color_create(color: Color):
    assert color

def test_request_return_404(client):
    assert client.get("/url_does_not_exist").status_code == 404      

def test_request_return_200(client):
    response = client.get("/") 
    assert client.get("/").status_code == 200      


def test_get_single_color(client, color: Color, db: SQLAlchemy):
    db.session.add(color)
    db.session.commit()
    response = client.get("/api/v1/color/blue").get_json()['result']   
    print (response)

    payload = {'value':'#00f','color': 'blue'} 
    assert [payload] == response

def test_get_single_color_error(client, color: Color, db: SQLAlchemy):
    db.session.add(color)
    db.session.commit()
    response = client.get("/api/v1/color/orange").get_json() 
    
    payload = {'message':'Color \'orange\' not found','success': False} 
    assert payload == response

def test_post_color(client, color: Color, db: SQLAlchemy):
    db.session.add(color)
    db.session.commit()
    payload = {"value":"#a52a2a","color":"brown"} 
    
    response = client.post("/api/v1/color/", json = payload)
    assert response == 201

def test_get_all_color(client):
    assert client.get("/api/v1/color/").status_code == 200    


def test_post_color_error_exist_color(client, color: Color, db: SQLAlchemy):
    db.session.add(color)
    db.session.commit()    
    payload = {'value':'#00f','color': 'blue'} 
    assert client.post("/api/v1/color/", json = payload).status_code == 409    

def test_post_color_error_wrong_colorname(client, color: Color, db: SQLAlchemy):
    db.session.add(color)
    db.session.commit()    
    payload = {'value':'#00f','color': 'blue2'} 

    response = client.post("/api/v1/color/", json = payload).get_json() 
    
    payload = {'message':"\'blue2\' is not a recognized color.",'success': False} 
    assert payload == response

def test_post_color_error_wrong_hexcode(client, color: Color, db: SQLAlchemy):
    db.session.add(color)
    db.session.commit()    
    payload = {'value':'#0hf','color': 'blue'} 

    response = client.post("/api/v1/color/", json = payload).get_json() 
    
    payload = {"message": "Value \'#0hf\' is not web format. Need 3 or 6 hex digit",'success': False} 
    assert payload == response

def test_post_color_error_hexcode_mismatch(client, color: Color, db: SQLAlchemy):
    db.session.add(color)
    db.session.commit()    
    payload = {'value':'#0ff','color': 'orange'} 
      

    response = client.post("/api/v1/color/", json = payload).get_json() 
    
    payload = {"message": "Color \'orange\' and hex code \'#0ff\' mismatch",'success': False} 
    assert payload == response    