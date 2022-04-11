# Proj_11 : Add tests to improve a Python web app

[Project 11](https://github.com/Pragon37/proj_11)

This project is a booking API, that is used by heavy lifting clubs to enrol in competition. 
After they have registered, users may enrol club members provided that:
- there are free slots available
- the club has enough points to book the desired number of slots
- the number of required slots is 12 maximum

## Installing / Getting started

It is implemented as a FLASK python API. To setup the environment you need to execute the following instructions:

```shell
cd proj_11
git checkout QA
python -m venv env
env/Scripts/activate
pip install -r requirements.txt
$env:FLASK_APP = "server"
$env:FLASK_DEBUG=1
flask run

To stop and quit the application: CTRL-BREAK.

```
Then you run the web application by loading :
[Project 11] (http://127.0.0.1:5000/)
It opens up the registration page.
From this page :
- you can login the system to book slots
- you can navigate to display the registered clubs and their points



## Tests Implementation
The fixes for errors, bugs, and new features and the related tests have been implemented in different branches.

To clone the project :

-git clone https://github.com/Pragon37/proj_11.git

Checkout branch QA:
git checkout QA


To checkout other branches :

1 - Fixes for : Unknown email crashes the system (code fixes + tests)
[Issue 1 ](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues/1)

git checkout error_unknown_email

2 - Fixes for :  Not allowed to use more than their points (code fixes + tests)
[Issue 2 ](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues/2)

git checkout bug_booking_limits

3- Fixes for : Not allowed to book more than 12 places per competition (code fixes + tests)
[Issue 4 ](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues/4)

git checkout bug_upper_limit

4- Fixes for : Not allowed to book places in past competitions (code fixes + tests)
[Issue 5 ](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues/5)

git checkout bug_book_in_past

5- Fixes for : Remove points that have been used (code fixes + tests)
[Issue 6 ](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues/6)

git checkout bug_points_update

6- Fixes for : Implement Points Display Board (code fixes + tests)
[Issue 7 ](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues/7)

git checkout feature_display_points



## Links


- Project homepage : [Project 11](https://github.com/Pragon37/proj_11)
- Repository: https://github.com/Pragon37/proj_11.git

#Testing and documentation 
The API has been tested using Postman.
The test collection can be imported from : SoftDeskAPI.postman_collection.json

The documentation was recorded with Postman and is available at the following URL:
[SoftDesk Doc](https://documenter.getpostman.com/view/17937229/UVkvLDXE)

## Run tests (unit, integration, functional)

git checkout QA
pytest


## Generate and display test coverage
git checkout QA
pytest --cov=. --cov-report html

Then display in your browser :
file:<Your Path>/htmlcov/server_py.html

## generate and display test performance
cd tests/performance
locust

in your browser load page : http://localhost:8089/
Notice that  http://0.0.0.0:8089 does not work
Start the test with :
users: 6
rate: 10
site: http://127.0.0.1:5000/
Make sure that flask is running at the above address.


## Author

Pierre : pragon37@outlook.fr

## Credits
[Selenium] (https://selenium-python.readthedocs.io/locating-elements.html)
[Flask](https://flask.palletsprojects.com/en/2.0.x/tutorial/tests/)
[testdriven.io](https://testdriven.io/blog/flask-pytest/)