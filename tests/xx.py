
from tests.conftest import client
from server import app
from server import clubs, clubs, getClubOrNone
import flask
from flask import request


def test_index_status_code_is_200(client):
	response = client.get('/')
	assert response.status_code == 200

def test_index_welcome_user(client):
    response = client.get('/')
    assert '<h1>Welcome to the GUDLFT Registration Portal!</h1>' in response.data.decode()


def test_logout_status_code_is_302(client):
	response = client.get('/logout')
	assert response.status_code == 302

def test_logout_return_redirected_url(client):
    response = client.get('/logout')
    expectedValue = 'http://localhost/'
    assert response.headers[2][1] == expectedValue

def _login_user(client, email):
    rv = client.get(
        "/", data={'email': email}
    )
    assert rv.status_code == 200
    data = rv.data.decode()
    assert data.find("Login User") == -1


def test_login_user_OK(client):
    _login_user(client, "john@simplylift.co")

def test_login_user_KO(client):
    rv = client.get(
        "/",
        data={"email": "abc@gmail.com"}
    )
    assert rv.status_code == 200

def test_login_unregistered_user(client):
        rv = client.get(
        "/",
        data={"email": "abc@gmail.com"}
    )        
        club = [club for club in clubs if club['email'] == request.form['email']]
        assert club == []

def test_login_registered_user(client):
        rv = client.get(
        "/",
        data={"email": "kate@shelifts.co.uk"}
    )        
        club = [club for club in clubs if club['email'] == request.form['email']]
        assert club[0]['name'] == "She Lifts"        

def test_getClubOrNone_is_None():
    with app.test_request_context("/showsummary", data={"email": "abc@abc.com"}):
        club = getClubOrNone()
    assert club == None

def test_getClubOrNone_is_not_None():
    with app.test_request_context("/showsummary", data={"email": "admin@irontemple.com"}):
        club = getClubOrNone()
    assert club['email'] == "admin@irontemple.com"