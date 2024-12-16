from pandas import DataFrame

from app.news import fetch_news_csv

def test_news_data_fetching():

    response = fetch_news_csv("sports", "DataFrame")
    assert isinstance(response, DataFrame)
    assert set(response.columns) == {"author", "title", "description", "url", "publishedAt"}
    assert len(response) > 0