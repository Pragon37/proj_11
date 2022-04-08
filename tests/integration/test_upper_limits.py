from server import app
from server import clubs, MAX_PLACES


def test_purchase_places_above_max_places_flash_message(client):
    rv = client.post(
        "/purchasePlaces",
        data={"club": "Simply Lift", "competition": "Spring Festival", "places": 13},
        follow_redirects=True,
    )
    with app.test_request_context(
        "/purchasePlaces",
        data={"club": "Simply Lift", "competition": "Spring Festival", "places": 13},
    ):
        points = int(clubs[0]["points"])
    assert (
        f"Cant book 13 places. Book should be from 0 to {min(points, MAX_PLACES)}"
        in rv.data.decode()
    )
