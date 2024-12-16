from flask import Blueprint, render_template, request, redirect, flash
from app.news import fetch_news_csv
import string 

news_routes = Blueprint("news_routes", __name__)

@news_routes.route("/news/form") #routes to the news form html file
def news_form():
    return render_template("news_form.html")

@news_routes.route("/news/dashboard", methods=["GET", "POST"]) #routes to the news dashboard file
def news_dashboard():
    try:
        if request.method == "POST":
            request_data = dict(request.form)
        else:
            request_data = dict(request.args)

        topic = request_data.get("topic", "Sports") #Retrieve the topic, use sports as default if not given

        documented_data = fetch_news_csv(topic=topic, return_type="json") #Fetch news article data for the chosen topic
        
        flash("Fetched Most Recent News Articles", "success") # Flash success message implemented, routes to the news dashboard html
        return render_template(
            "news_dashboard.html",
            topic=topic,
            data=documented_data 
        )
    except Exception as err: #This should not occur due to our implementation of a drop down
        print("Error:", err) 
        flash("News Articles Fetch Error. Please check your topic and try again!", "danger")
        return redirect("/news/form")