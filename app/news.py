#from getpass import getpass
import requests
import csv
from pprint import pprint
##from IPython.display import Image, display
import pandas as df
from datetime import datetime
#
def to_datetime(x):
    date_object = datetime.strptime(x, "%Y-%m-%dT%H:%M:%S%z")
    formatted_date = date_object.strftime('%m-%d-%Y, %I:%M:%S %p')
    return(formatted_date)

#assert to_datetime("2024-06-07T14:17:12+0000") == "06-07-2024, 02:17:12 PM"
#
#
#def fetch_news_csv(topic):
#    request_url = f"https://newsapi.org/v2/everything?q={topic}&apiKey=1bb2735a929a4e9886a1944523c3b065"
#    df = read_csv(request_url)
#    sorted_articles = sorted(df["articles"], key=lambda x: datetime.strptime(x["publishedAt"], "%Y-%m-%dT%H:%M:%S%z"), reverse=True) 
#    documented_data = sorted_articles[0:5]
#    new_dict={}
#    for d in documented_data:
#        print("---------------------------------------")
#        print("AUTHOR: ", d["author"])
#        print("TITLE: ", d["title"])
#        print("DESCRIPTION: ", d["description"])
#        print("URL: ", d["url"])
#        print("TIME: ", to_datetime(d["publishedAt"]))
#        new_dict.append(d)
#    return new_dict
#
##url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={NEWSAPI}"
##response = requests.get(url)
##request_data = json.loads(response.text)
#
#sorted_articles = sorted(df["articles"], key=lambda x: datetime.strptime(x["publishedAt"], "%Y-%m-%dT%H:%M:%S%z"), reverse=True) 
#
#documented_data = sorted_articles[0:5]
#
#for d in documented_data:
#    print("---------------------------------------")
#    print("AUTHOR: ", d["author"])
#    print("TITLE: ", d["title"])
#    print("DESCRIPTION: ", d["description"])
#    print("URL: ", d["url"])
#    print("TIME: ", to_datetime(d["publishedAt"]))
#
import requests
from datetime import datetime

def fetch_news_csv(topic):
    #api_key = "YOUR_NEWS_API_KEY"  # Replace with your actual API key
    request_url = f"https://newsapi.org/v2/everything?q={topic}&apiKey=1bb2735a929a4e9886a1944523c3b065"
    
    response = requests.get(request_url)
    if response.status_code != 200:
        print("Error fetching data from API")
        return df.DataFrame()
    
    data = response.json()
    articles = data.get("articles", [])
    
    sorted_articles = sorted(
        articles, 
        key=lambda x: datetime.strptime(x["publishedAt"], "%Y-%m-%dT%H:%M:%SZ"), 
        reverse=True
    )

    documented_data = df.DataFrame([{
        "AUTHOR": d.get("author", "Unknown"),
        "TITLE": d.get("title", "No title"),
        "DESCRIPTION": d.get("description", "No description"),
        "URL": d.get("url", "No URL"),
        "TIME": datetime.strptime(d["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")
    } for d in sorted_articles[:5]])  # Top 5 articles
    
    return documented_data

 #   documented_data = sorted_articles[:5]  # Get the top 5 most recent articles
 #   result = []
 #   
 #   for d in documented_data:
 #       print("------------------------------------")
 #       print("AUTHOR: ", d.get("author", "Unknown"))
 #       print("TITLE: ", d.get("title", "No title"))
 #       print("DESCRIPTION: ", d.get("description", "No description"))
 #       print("URL: ", d.get("url", "No URL"))
 #       print("TIME: ", datetime.strptime(d["publishedAt"], "%Y-%m-%dT%H:%M:%SZ"))
 #       
 #       result.append({
 #           "author": d.get("author"),
 #           "title": d.get("title"),
 #           "description": d.get("description"),
 #           "url": d.get("url"),
 #           "publishedAt": d.get("publishedAt")
 #       })
 #   
 #   return result