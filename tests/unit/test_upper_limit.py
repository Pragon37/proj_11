from tests.conftest import client
from server import app
from server import clubs, clubs, IsPlacesAvailable, IsRequestNotPossible
import flask
from flask import request


def test_IsRequestNotPossible():
    assert IsRequestNotPossible(pointsLeft=10, placesRequired=9) is False
    assert IsRequestNotPossible(pointsLeft=9, placesRequired=10) is True
    assert IsRequestNotPossible(pointsLeft=10, placesRequired=-1) is True
    assert IsRequestNotPossible(pointsLeft=0, placesRequired=0) is False


    