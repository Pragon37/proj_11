from tests.conftest import client
from server import app
from server import clubs, MAX_PLACES
import flask
from flask import request


def test_purchase_places_negative_does_not_update_points_OK(client):
    with app.test_request_context("/purchasePlaces", data={"club": "Simply Lift", "competition": "Spring Festival", "places": 0}):
        points = int(clubs[0]['points'])
    print('POINTS : ', points)
    rv = client.post(
        "/purchasePlaces",
        data={"club": "Simply Lift", "competition": "Spring Festival", "places": -1}, follow_redirects=True
    )
    assert f'Points available: {points}' in rv.data.decode()

def test_purchase_places_null_does_not_update_points_OK(client):
    with app.test_request_context("/purchasePlaces", data={"club": "Simply Lift", "competition": "Spring Festival", "places": 0}):
        points = int(clubs[0]['points'])
    print('POINTS : ', points)
    rv = client.post(
        "/purchasePlaces",
        data={"club": "Simply Lift", "competition": "Spring Festival", "places": ''}, follow_redirects=True
    )
    assert f'Points available: {points}' in rv.data.decode()

def test_purchase_places_more_than_max_does_not_update_points_OK(client):
    with app.test_request_context("/purchasePlaces", data={"club": "Simply Lift", "competition": "Spring Festival", "places": 0}):
        points = int(clubs[0]['points'])
    print('POINTS : ', points)
    rv = client.post(
        "/purchasePlaces",
        data={"club": "Simply Lift", "competition": "Spring Festival", "places": MAX_PLACES + 1}, follow_redirects=True
    )
    assert f'Points available: {points}' in rv.data.decode()

def test_purchase_places_more_than_own_does_not_update_points_OK(client):
    with app.test_request_context("/purchasePlaces", data={"club": "Iron Temple", "competition": "Spring Festival", "places": 0}):
        points = int(clubs[1]['points'])
    print('POINTS : ', points)
    rv = client.post(
        "/purchasePlaces",
        data={"club": "Iron Temple", "competition": "Spring Festival", "places": points + 1}, follow_redirects=True
    )
    assert f'Points available: {points}' in rv.data.decode()

def test_purchase_places_update_points_OK(client):
    with app.test_request_context("/purchasePlaces", data={"club": "Iron Temple", "competition": "Spring Festival", "places": 0}):
        points = int(clubs[1]['points'])
    print('POINTS : ', points)
    rv = client.post(
        "/purchasePlaces",
        data={"club": "Iron Temple", "competition": "Spring Festival", "places": 2}, follow_redirects=True
    )
    assert f'Points available: {points - 2}' in rv.data.decode()

