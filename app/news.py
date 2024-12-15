import requests
import csv
#from pprint import pprint
#from IPython.display import Image, display
import pandas as pd
from datetime import datetime
from app.news_service import API_KEY

def to_datetime(x): #formats time consistently to help with sorting articles by date later on
    date_object = datetime.strptime(x, "%Y-%m-%dT%H:%M:%S%z")
    formatted_date = date_object.strftime('%m-%d-%Y, %I:%M:%S %p')
    return(formatted_date)



def fetch_news_csv(topic): #fetches the news article data across various topics
    request_url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={API_KEY}"
    response = requests.get(request_url)
    if response.status_code != 200:
        print("Error fetching data from API")
        return pd.DataFrame()
    
    data = response.json()
    articles = data.get("articles", [])
    
    sorted_articles = sorted(articles, key=lambda x: datetime.strptime(x["publishedAt"], "%Y-%m-%dT%H:%M:%SZ"), reverse=True)
    #sorts the articles based on recency
    
    documented_data = sorted_articles[0:5]  # Get the top 5 most recent articles
    result = []
    
    for d in documented_data:        
        result.append({
            "author": d.get("author"),
            "title": d.get("title"),
            "description": d.get("description"),
            "url": d.get("url"),
            "time": d.get("time")
        })
    return result
    #result_df = pd.DataFrame(result)
    #result_df = result_df.to_json()
    #return result_df