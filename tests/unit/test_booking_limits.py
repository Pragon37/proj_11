from server import IsPlacesAvailable, IsRequestNotPossible


def test_purchasePlaces_status_code_is_OK_200(client):
    response = client.post(
        "/purchasePlaces",
        data={"club": "Simply Lift", "competition": "Spring Festival", "places": 5},
    )
    assert response.status_code == 200


def test_purchasePlaces_no_club_status_code_is_400(client):
    response = client.post(
        "/purchasePlaces", data={"competition": "Spring Festival", "places": 5}
    )
    assert response.status_code == 400


def test_purchasePlaces_no_competition_status_code_is_400(client):
    response = client.post("/purchasePlaces", data={"club": "Simply Lift", "places": 5})
    assert response.status_code == 400


def test_purchasePlaces_no_places_status_code_is_400(client):
    response = client.post(
        "/purchasePlaces",
        data={"club": "Simply Lift", "competition": "Spring Festival"},
    )
    assert response.status_code == 400


def test_showSummary_is_OK_200(client):
    response = client.post("/showSummary", data={"email": "john@simplylift.co"})
    assert response.status_code == 200


def test_showSummary_is_NOK_400(client):
    response = client.post("/showSummary", data={})
    assert response.status_code == 400


def test_IsPlacesAvailable():
    assert IsPlacesAvailable(10, 4) is True
    assert IsPlacesAvailable(4, 10) is False
    assert IsPlacesAvailable(10, 10) is True


def test_IsRequestNotPossible():
    assert IsRequestNotPossible(pointsLeft=28, placesRequired=9) is False
    assert IsRequestNotPossible(pointsLeft=9, placesRequired=10) is True
    assert IsRequestNotPossible(pointsLeft=14, placesRequired=-1) is True
    assert IsRequestNotPossible(pointsLeft=0, placesRequired=0) is False
    assert IsRequestNotPossible(pointsLeft=14, placesRequired=13) is True
