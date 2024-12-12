# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template

about_us_routes = Blueprint("about_us_routes", __name__)

@about_us_routes.route("/about/us")
def about_list():
    print("ABOUT US...")

    # this is some data from the internet maybe
    about = [
        {
            'name': 'Abhi Meka',
            'info': 'Class of 2026, Finance & OPAN',
            'url': 'https://picsum.photos/id/1080/360/200'
        },
        {
            'name': 'Minato Shinoda',
            'info': 'Class of 2026, Marketing & OPAN',
            'url': 'https://picsum.photos/id/225/360/200'
        },
        {
            'name': 'Sneha Selvaraj',
            'info': 'Class of 2026, Marketing & OPAN',
            'url': 'https://picsum.photos/id/24/360/200'
        }
    ]

    return render_template("about_us.html", about=about)