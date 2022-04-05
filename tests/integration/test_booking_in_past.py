from tests.conftest import client
from server import app
from server import clubs, competitions, MAX_PLACES, DATE_FORMAT 
import flask
import pytest
from flask import request


def test_purchase_places_overbooking_flash_message(client):
    response = client.post(
    "/purchasePlaces",
    data={"club": "Iron Temple", "competition": "Spring Festival 2021", "places": 5}, follow_redirects=True
    )
    assert f"Cant book places in past competition : {competitions[2]['date']}" in response.data.decode()


