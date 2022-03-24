
import server
from server import loadClubs
import json
import  pytest


clubs = {"clubs":[
    {
        "name":"Iron Temple",
        "email": "admin@irontemple.com",
        "points":"4"
    },
]}

expected_value = [{
        "name":"Iron Temple",
        "email": "admin@irontemple.com",
        "points":"4"
    }]

def test_load_clubs(mocker):
    read_data = json.dumps(clubs)
    mock_open = mocker.mock_open(read_data=read_data)
    mocker.patch('builtins.open', mock_open)
    assert loadClubs() == expected_value

