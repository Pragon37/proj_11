from tests.conftest import client
from server import app
from server import clubs, clubs, IsPlacesAvailable, IsRequestNotPossible
import flask
from flask import request

def test_purchasePlaces_status_code_is_OK_200(client):
    response = client.post('/purchasePlaces', data={"club": "Simply Lift", "competition": "Spring Festival", "places": 5})
    assert response.status_code == 200

def test_purchasePlaces_no_club_status_code_is_400(client):
    response = client.post('/purchasePlaces', data={"competition": "Spring Festival", "places": 5})
    assert response.status_code == 400

def test_purchasePlaces_no_competition_status_code_is_400(client):
    response = client.post('/purchasePlaces', data={"club": "Simply Lift", "places": 5})
    assert response.status_code == 400

def test_purchasePlaces_no_places_status_code_is_400(client):
    response = client.post('/purchasePlaces', data={"club": "Simply Lift", "competition": "Spring Festival"})
    assert response.status_code == 400

def test_showSummary_is_OK_200(client):
    response = client.post('/showSummary', data={"email": "john@simplylift.co"})
    assert response.status_code == 200

def test_showSummary_is_NOK_400(client):
    response = client.post('/showSummary', data={})
    assert response.status_code == 400

def test_IsPlacesAvailable():
    assert IsPlacesAvailable(10, 4) is True
    assert IsPlacesAvailable(4, 10) is False
    assert IsPlacesAvailable(10, 10) is True

def test_IsRequestNotPossible():
    assert IsRequestNotPossible(pointsLeft=14, placesRequired=13) is False
    assert IsRequestNotPossible(pointsLeft=14, placesRequired=16) is True
    assert IsRequestNotPossible(pointsLeft=14, placesRequired=-1) is True
    assert IsRequestNotPossible(pointsLeft=0, placesRequired=0) is False

def test_book_competition_club_is_OK_200(client):
	response = client.get('/book/Spring%20Festival/Simply%20Lift')
	assert response.status_code == 200

def test_book_competition_club_is_NOK_500(client):
	response = client.get('/book/Spring%20Festival/SimplyLift')
	assert response.status_code == 500

def test_book_competition_club_is_NOK_404(client):
	response = client.get('/book/Spring%20Festival')
	assert response.status_code == 404

def test_book_competition_club_banner(client):
    response = client.get('/book/Spring%20Festival/Simply%20Lift')
    assert 'Spring Festival' in response.data.decode()
    response = client.get('/book/Fall%20Classic/She%20Lifts')
    assert 'Fall Classic' in response.data.decode()

def test_show_summary_banner(client):
    email = 'john@simplylift.co'
    response = client.post('/showSummary', data={"email": email})
    assert f'Welcome, {email}' in response.data.decode()

def test_purchase_places_banner(client):
    email = 'john@simplylift.co'
    response = client.post('/purchasePlaces', data={"club": "Simply Lift", "competition": "Spring Festival", "places": 5})
    assert f'Welcome, {email}' in response.data.decode()

"""
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

def test_getClubOrNone_is_None():
    with app.test_request_context("/showsummary", data={"email": "abc@abc.com"}):
        club = getClubOrNone()
    assert club == None

def test_getClubOrNone_is_not_None():
    with app.test_request_context("/showsummary", data={"email": "admin@irontemple.com"}):
        club = getClubOrNone()
    assert club['email'] == "admin@irontemple.com"
"""