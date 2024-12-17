from pandas import DataFrame
from app.news_service import API_KEY
from app.news import fetch_news_csv
import os

from dotenv import load_dotenv
load_dotenv()

def test_news_data_fetching():
    assert len(os.environ.get("NEWSAPI_KEY"))>5
    response = fetch_news_csv("sports", "DataFrame")
    assert isinstance(response, DataFrame)
    #assert set(response.columns) == {"author", "title", "description", "url", "publishedAt"}
    assert len(response) > 0