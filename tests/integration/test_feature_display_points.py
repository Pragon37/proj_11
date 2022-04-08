
def test_book_competition_club_OK(client):
    rv = client.get(
        "/book/Spring%20Festival/She%20Lifts",
        data={"club": "She Lifts", "competition": "Spring Festival", "places": 0},
        follow_redirects=True,
    )

    assert "Spring Festival" in rv.data.decode()


def test_book_competition_club_NOK(client):
    rv = client.get(
        "/book/SpringFestival/She%20Lift",
        data={"club": "She Lifts", "competition": "Spring Festival", "places": 0},
        follow_redirects=True,
    )

    assert "Something went wrong-please try again" in rv.data.decode()
