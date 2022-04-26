from server import IsRequestNotPossible


def test_IsRequestNotPossible():
    assert IsRequestNotPossible(pointsLeft=28, placesRequired=9) is False
    assert IsRequestNotPossible(pointsLeft=9, placesRequired=10) is True
    assert IsRequestNotPossible(pointsLeft=10, placesRequired=-1) is True
    assert IsRequestNotPossible(pointsLeft=0, placesRequired=0) is False
