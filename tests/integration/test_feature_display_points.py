from tests.conftest import client
from server import app
from server import clubs, MAX_PLACES
import flask
from flask import request


def test_book_competition_club_OK(client):
    rv = client.get(
        "/book/Spring%20Festival/She%20Lifts",
        data={"club": "She Lifts", "competition": "Spring Festival", "places": 0}, follow_redirects=True
    )
    
    assert f'Spring Festival' in rv.data.decode()

def test_book_competition_club_NOK(client):
    rv = client.get(
        "/book/SpringFestival/She%20Lift",
        data={"club": "She Lifts", "competition": "Spring Festival", "places": 0}, follow_redirects=True
    )
    
    assert f'Something went wrong-please try again' in rv.data.decode()