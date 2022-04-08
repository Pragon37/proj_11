from server import IsDateOver
from datetime import datetime
from dateutil.relativedelta import relativedelta


futureDate = datetime.now() + relativedelta(months=+6)
passedDate = datetime.now() + relativedelta(months=-6)


def test_IsDateOver():
    assert IsDateOver(datetime.now(), futureDate) is False
    assert IsDateOver(datetime.now(), passedDate) is True
