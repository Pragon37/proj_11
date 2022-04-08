def test_display_points_status_code_is_NOK_400(client):
    response = client.post("/displayPoints")
    assert response.status_code == 400


def test_display_points_for_unknown_status_code_is_OK_200(client):
    response = client.post(
        "/displayPoints", data={"email": "abc@gmail.com"}, follow_redirects=True
    )
    assert response.status_code == 200


def test_display_points_for_actual_user_status_code_is_OK_200(client):
    response = client.post(
        "/displayPoints", data={"email": "kate@shelifts.co.uk"}, follow_redirects=True
    )
    assert response.status_code == 200


def test_display_points_welcome_user(client):
    email = "kate@shelifts.co.uk"
    response = client.post(
        "/displayPoints", data={"email": email}, follow_redirects=True
    )
    assert f"<h2>Welcome, {email} </h2>" in response.data.decode()
