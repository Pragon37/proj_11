from server import app
from server import clubs, MAX_PLACES


def test_purchase_places_negative_flash_message(client):
    rv = client.post(
        "/purchasePlaces",
        data={"club": "Simply Lift", "competition": "Spring Festival", "places": -1},
        follow_redirects=True,
    )
    with app.test_request_context(
        "/purchasePlaces",
        data={"club": "Simply Lift", "competition": "Spring Festival", "places": -1},
    ):
        points = int(clubs[0]["points"])
    assert (
        f"Cant book -1 places. Book should be from 0 to {min(points, MAX_PLACES)}"
        in rv.data.decode()
    )


def test_purchase_places_overbooking_flash_message(client):
    response = client.post(
        "/purchasePlaces",
        data={"club": "Iron Temple", "competition": "Spring Festival", "places": 5},
        follow_redirects=True,
    )
    assert "Cant book 5 places. Book should be from 0 to 4" in response.data.decode()


def test_purchase_places_negative_NOK(client):
    response = client.post(
        "/purchasePlaces",
        data={"club": "Simply Lift", "competition": "Spring Festival", "places": -1},
        follow_redirects=True,
    )
    assert "Number of Places: 25" in response.data.decode()


def test_purchase_places_overbooking_NOK(client):
    response = client.post(
        "/purchasePlaces",
        data={"club": "Simply Lift", "competition": "Spring Festival", "places": 14},
        follow_redirects=True,
    )
    assert "Number of Places: 25" in response.data.decode()


"""Actually decrements the number of available seat. This may influence the result of following tests"""


def test_purchase_places_OK(client):
    response = client.post(
        "/purchasePlaces",
        data={"club": "Simply Lift", "competition": "Spring Festival", "places": 1},
        follow_redirects=True,
    )
    assert "Number of Places: 13" in response.data.decode()


def test_purchase_places_OK_flash_message(client):
    response = client.post(
        "/purchasePlaces",
        data={"club": "Simply Lift", "competition": "Spring Festival", "places": 1},
        follow_redirects=True,
    )
    assert "Great-booking complete!" in response.data.decode()


def test_purchase_places_book_too_many_flash_message(client):
    response = client.post(
        "/purchasePlaces",
        data={"club": "Simply Lift", "competition": "Fall Classic", "places": 4},
        follow_redirects=True,
    )
    response = client.post(
        "/purchasePlaces",
        data={"club": "She Lifts", "competition": "Fall Classic", "places": 10},
        follow_redirects=True,
    )
    assert "Cant book 10 places. Available : 9" in response.data.decode()
