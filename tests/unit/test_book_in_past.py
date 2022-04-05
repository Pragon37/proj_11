from tests.conftest import client
from server import app
from server import clubs, clubs, IsDateOver, DATE_FORMAT
import flask
from flask import request
from datetime import datetime

futureDate = "2022-06-10 13:00:05"
passedDate = "2021-06-10 13:00:05"

def test_IsDateOver():
    print('NOW :', datetime.now())
    assert IsDateOver(datetime.now().strftime(DATE_FORMAT), futureDate) is False
    assert IsDateOver(datetime.now().strftime(DATE_FORMAT), passedDate) is True



    