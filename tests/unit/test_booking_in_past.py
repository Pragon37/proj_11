from tests.conftest import client
from server import app
from server import clubs, clubs, IsDateOver, DATE_FORMAT
import flask
from flask import request
from datetime import datetime
from dateutil.relativedelta import relativedelta


futureDate = datetime.now() + relativedelta(months=+6)
passedDate = datetime.now() + relativedelta(months=-6)

def test_IsDateOver():
    assert IsDateOver(datetime.now(), futureDate) is False
    assert IsDateOver(datetime.now(), passedDate) is True



    