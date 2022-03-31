from tests.conftest import client
from server import app
from server import clubs, clubs, getClubOrNone
import flask
from flask import request


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
        data={"email": "abc@gmail.com"}, follow_redirects=True
    )
    #assert 'There is no registered club for this email' in rv.data.decode()
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

def test_login_unregistered_user_flash_message(client):
    rv = client.post(
        "/showSummary",
        data={"email": "abc@gmail.com"}, follow_redirects=True
    )
    assert 'There is no registered club for this email' in rv.data.decode()