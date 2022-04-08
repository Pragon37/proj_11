from server import app
from server import getClubOrNone


def test_index_status_code_is_200(client):
    response = client.get("/")
    assert response.status_code == 200


def test_index_welcome_user(client):
    response = client.get("/")
    assert (
        "<h1>Welcome to the GUDLFT Registration Portal!</h1>" in response.data.decode()
    )


def test_logout_status_code_is_302(client):
    response = client.get("/logout")
    assert response.status_code == 302


def test_logout_return_redirected_url(client):
    response = client.get("/logout")
    expectedValue = "http://localhost/"
    assert response.headers[2][1] == expectedValue


def test_getClubOrNone_is_None():
    with app.test_request_context("/showsummary", data={"email": "abc@abc.com"}):
        club = getClubOrNone()
    assert club is None


def test_getClubOrNone_is_not_None():
    with app.test_request_context(
        "/showsummary", data={"email": "admin@irontemple.com"}
    ):
        club = getClubOrNone()
    assert club["email"] == "admin@irontemple.com"
