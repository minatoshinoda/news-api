from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/") #routes to the home html file
@home_routes.route("/home")
def index():
    return render_template("home.html")