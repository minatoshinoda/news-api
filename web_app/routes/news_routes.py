
# this is the "web_app/routes/news_routes.py" file ...
#
#from flask import Blueprint, request, render_template, redirect, flash
#
#from app.news import fetch_news_csv
#
#news_routes = Blueprint("news_routes", __name__)
#
#@news_routes.route("/news/form")
#def news_form():
#    print("NEWS FORM...")
#    return render_template("news_form.html")
#
#@news_routes.route("/news/dashboard", methods=["POST"])
##@news_routes.route("/news/dashboard", methods=["GET", "POST"])
#def news_dashboard():
#    print("NEWS DASHBOARD...")
#
#    if request.method == "POST":
#        # for data sent via POST request, form inputs are in request.form:
#        request_data = dict(request.form)
#        print("FORM DATA:", request_data)
#    else:
#        # for data sent via GET request, url params are in request.args
#        request_data = dict(request.args)
#        print("URL PARAMS:", request_data)
#
#    topic = request_data.get("topic") or "NFLX"
#
#    try:
#        df = fetch_news_csv(topic=topic)
#        #latest_close_usd = format_usd(df.iloc[0]["adjusted_close"])
#        #latest_date = df.iloc[0]["timestamp"]
#        #data = df.to_dict("records")
#
#        flash("Fetched Real-time Market Data!", "success")
#        return render_template("news_dashboard.html",
#            topic=topic,
#           # latest_close_usd=latest_close_usd,
#           # latest_date=latest_date,
#           # data=data
#        )
#    except Exception as err:
#        print('OOPS', err)
#
#    flash("Market Data Error. Please check your topic and try again!", "danger")
#    return redirect("/news/form")
#
##
## API ROUTES
##
#
#@news_routes.route("/api/news.json")
#def news_api():
#    print("NEWS DATA (API)...")
#
#    # for data supplied via GET request, url params are in request.args:
#    url_params = dict(request.args)
#    print("URL PARAMS:", url_params)
#    topic = url_params.get("topic") or "NFLX"
#
#    try:
#        df = fetch_news_csv(topic=topic)
#        data = df.to_dict("records")
#        return {"topic": topic}
#    except Exception as err:
#        print('OOPS', err)
#        return {"message":"Market Data Error. Please try again."}, 404

from flask import Blueprint, render_template, request, redirect, flash
from app.news import fetch_news_csv  # Assuming the corrected `fetch_news_csv` function is imported

news_routes = Blueprint("news_routes", __name__)

@news_routes.route("/news/form")
def news_form():
    # Render the news form template
    return render_template("news_form.html")

@news_routes.route("/news/dashboard", methods=["GET", "POST"])
def news_dashboard():
    try:
        if request.method == "POST":
            # Data sent via POST request (form inputs)
            request_data = dict(request.form)
            print("FORM DATA:", request_data)
        else:
            # Data sent via GET request (URL parameters)
            request_data = dict(request.args)
            print("URL PARAMS:", request_data)

        # Get the topic from the request, default to "NFLX" if not provided
        topic = request_data.get("topic", "NFLX")

        # Fetch news data for the given topic
        documented_data = fetch_news_csv(topic=topic)

        # Flash success message and render the dashboard template
        flash("Fetched Real-Time Market Data", "success")
        return render_template(
            "news_dashboard.html",
            topic=topic,
            data=documented_data  # Pass the processed data to the template
        )

    except Exception as err:
        print("Error:", err)  # Log the error for debugging
        flash("Market Data Error. Please check your topic and try again!", "danger")
        return redirect("/news/form")