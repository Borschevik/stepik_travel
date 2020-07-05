from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """
    Main page

    :return: rendered page
    """

    return render_template("index.html")


@app.route("/departures/<string:departure>/")
def departues(departure: str):
    """
    Departure location

    :param departure:
    :return: rendered page
    """

    return render_template("departure.html")


@app.route("/tours/<int:id>/")
def tours(id: int):
    """
    Tour page rendering

    :param id: int
    :return: rendered page
    """

    return render_template("tour.html")


if __name__ == "__main__":
    app.run()
