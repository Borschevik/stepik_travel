import importlib

from flask import Flask, render_template

from resource.tours import tours
from service.departure.filterservice import (
    FilterService as DepartureFilterService,
)
from utils.util_module import module_to_dict
from utils.util_string import lower_byindex

app: Flask = Flask(__name__)
title: dict = module_to_dict(importlib.import_module("stepik_travel.resource.title"))


@app.route("/")
def index():
    """
    Main page

    :return: rendered page
    """
    data: dict = tours.copy()

    return render_template("index.html", title=title, tours=data)


@app.route("/departures/<string:departure>/")
def departues(departure: str):
    """
    Departure location

    :param departure:
    :return: rendered page
    """
    data: dict = tours.copy()
    filter = DepartureFilterService(data)
    filtered_tours: dict = filter.filter(departure)

    return render_template(
        "departure.html",
        title=title,
        location=departure,
        tours=filtered_tours,
        lower_byindex=lower_byindex,
    )


@app.route("/tours/<int:id>/")
def tours_id(id: int):
    """
    Tour page rendering

    :param id: int
    :return: rendered page
    """
    data: dict = tours.copy()

    return render_template(
        "tour.html", title=title, tour=data[id], lower_byindex=lower_byindex
    )


if __name__ == "__main__":
    app.run()
