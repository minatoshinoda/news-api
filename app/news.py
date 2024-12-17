import requests
import csv
#from pprint import pprint
#from IPython.display import Image, display
import pandas as pd
from datetime import datetime
from app.news_service import API_KEY
import string

def to_datetime(x): #formats time consistently to help with sorting articles by date later on
    date_object = datetime.strptime(x, "%Y-%m-%dT%H:%M:%S%z")
    formatted_date = date_object.strftime('%m-%d-%Y, %I:%M:%S %p')
    return(formatted_date)



def fetch_news_csv(topic, return_type, apikey=None): #fetches the news article data across various topics
    if API_KEY is not None:
        apikey = API_KEY
    request_url = f"https://www.newsapi.org/v2/everything?q={topic}&apiKey={apikey}"
    response = requests.get(request_url)
    #print(return_type)
    #print(request_url)
    #print(response.status_code)
    if response.status_code != 200:
        print("Error fetching data from API")
        return pd.DataFrame()
    
    data = response.json()
    #print(data)
    articles = data.get("articles", [])
    
    
    sorted_articles = sorted(articles, key=lambda x: datetime.strptime(x["publishedAt"], "%Y-%m-%dT%H:%M:%SZ"), reverse=True)
    #sorts the articles based on recency

    documented_data = sorted_articles[0:5]  # Get the top 5 most recent articles
    result = []
    print(documented_data)

    for d in documented_data:  

        # if the type is not none, escape the double quote
        if d.get("title") is None:
            title = d.get("title")     
        else:
            title =  d.get("title").replace('"', '\\"')

        if d.get("description") is None:
            description = d.get("description")     
        else:
            description =  d.get("description").replace('"', '\\"').replace('\n', '<br>')

        result.append({
            "author": d.get("author"),
            "title": title,
            "description": description,
            "url": d.get("url"),
            "publishedAt": d.get("publishedAt")
        })
    #print(result)
    if return_type =="json":
        return result   
    else: 
        result_df = pd.DataFrame(result)
        return result_df