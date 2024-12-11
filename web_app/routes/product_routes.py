# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template

product_routes = Blueprint("product_routes", __name__)

@product_routes.route("/products")
def products_list():
    print("PRODUCTS...")

    # this is some data from the internet maybe
    products = [
        {
            'name': 'Strawberries',
            'description': 'Juicy organic strawberries.',
            'price': 4.99,
            'url': 'https://picsum.photos/id/1080/360/200'
        },
        {
            'name': 'Cup of Tea',
            'description': 'An individually-prepared tea or coffee of choice.',
            'price': 3.49,
            'url': 'https://picsum.photos/id/225/360/200'
        },
        {
            'name': 'Textbook',
            'description': 'It has all the answers.',
            'price': 129.99,
            'url': 'https://picsum.photos/id/24/360/200'
        }
    ]

    return render_template("products.html", products=products)