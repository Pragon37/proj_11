import json
from datetime import datetime
import pstats
from types import NoneType
from flask import Flask, render_template, request, redirect, flash, url_for

MAX_PLACES = 12
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def loadClubs():
    with open("clubs.json") as c:
        listOfClubs = json.load(c)["clubs"]
        return listOfClubs


def loadCompetitions():
    with open("competitions.json") as comps:
        listOfCompetitions = json.load(comps)["competitions"]
        return listOfCompetitions


def getClubOrNone():
    club = [club for club in clubs if club["email"] == request.form["email"]]
    if club == []:
        return None
    return club[0]


def IsPlacesAvailable(placesLeft, placesRequired):
    return placesLeft - placesRequired >= 0


def IsRequestNotPossible(pointsLeft, placesRequired):
    return (
        (pointsLeft - placesRequired < 0)
        or (placesRequired < 0)
        or placesRequired > MAX_PLACES
    )


def IsDateOver(todayDate, competitionDate):
    return competitionDate < todayDate


app = Flask(__name__)
app.secret_key = "something_special"


def create_app():
    app = Flask(__name__)
    return app


competitions = loadCompetitions()
clubs = loadClubs()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/showSummary", methods=["POST"])
def showSummary():
    email = request.form["email"]
    if getClubOrNone() is None:
        flash(f"There is no registered club for this email : {email}")
        return redirect(url_for("index"))
    return render_template(
        "welcome.html", club=getClubOrNone(), email=email, competitions=competitions
    )


@app.route("/book/<competition>/<club>")
def book(competition, club):
    try:
        foundClub = [c for c in clubs if c["name"] == club][0]
    except:
        foundClub = False
    try:
        foundCompetition = [c for c in competitions if c["name"] == competition][0]
    except:
        foundCompetition = False

    if foundClub and foundCompetition:
        return render_template(
            "booking.html", club=foundClub, competition=foundCompetition
        )
    else:
        flash("Something went wrong-please try again")
        return render_template("welcome.html", club=club, competitions=competitions)


@app.route("/purchasePlaces", methods=["POST"])
def purchasePlaces():
    competition = [c for c in competitions if c["name"] == request.form["competition"]][
        0
    ]
    club = [c for c in clubs if c["name"] == request.form["club"]][0]
    email = club["email"]
    placesRequired = (
        int(request.form["places"]) if request.form["places"] != "" else 0
    )
    placesLeft = int(competition["numberOfPlaces"])
    pointsLeft = int(club["points"])
    if IsDateOver(datetime.now().strftime(DATE_FORMAT), competition["date"]):
        flash(f"Cant book places in past competition : {competition['date']}")
    elif IsRequestNotPossible(pointsLeft, placesRequired):
        flash(
            f"Cant book {placesRequired} places. Book should be from 0 to {min(pointsLeft, MAX_PLACES)}"
        )
    elif IsPlacesAvailable(placesLeft, placesRequired):
        competition["numberOfPlaces"] = (
            int(competition["numberOfPlaces"]) - placesRequired
        )
        club["points"] = int(club["points"]) - placesRequired
        flash("Great-booking complete!")
    else:
        flash(f"Cant book {placesRequired} places. Available : {placesLeft}")
    return render_template(
        "welcome.html", club=club, email=email, competitions=competitions
    )


# TODO: Add route for points display
@app.route("/displayPoints", methods=["POST"])
def displayPoints():
    email = request.form["email"]
    return render_template(
        "points.html", email=email, clubs=clubs, competitions=competitions
    )


@app.route("/logout")
def logout():
    return redirect(url_for("index"))
