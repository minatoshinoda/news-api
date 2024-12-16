from pandas import DataFrame

from app.news import fetch_news_csv

def test_news_data_fetching():

    response = fetch_news_csv("sports", "DataFrame")
    assert isinstance(response, DataFrame)
    assert set(response.columns) == {"author", "title", "description", "url", "time"}
    assert len(response) > 0

 #   earliest = df.iloc[-1]
 #   assert earliest["timestamp"] == '2018-04-03'
  #  assert earliest["adjusted_close"] == 149.01