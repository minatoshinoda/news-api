import os
from flask import Flask

#Ensuring to import all routes
from web_app.routes.home_routes import home_routes
from web_app.routes.news_routes import news_routes
from web_app.routes.about_us_routes import about_us_routes

#SECRET_KEY = os.getenv("SECRET_KEY", default="super secret") 
API_KEY = os.getenv("NEWSAPI_KEY")

def create_app():
    app = Flask(__name__)
    #app.config["SECRET_KEY"] = SECRET_KEY

    app.register_blueprint(home_routes)
    app.register_blueprint(news_routes)
    app.register_blueprint(about_us_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)