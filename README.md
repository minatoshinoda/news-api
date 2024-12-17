# news-api

## Setup

Create a virtual environment:

```sh
conda create -n news-api python=3.10
```

Activate the environment:

```sh
conda activate news-api
```

Install packages:

```sh
pip install -r requirements.txt
```

[Obtain an API Key](https://newsapi.org/account)


Create a ".env" file and add contents like the following:

```sh
NEWSAPI_KEY="..."
```
## Usage

Run article generator 
```sh
python -m app.news
```
## Web App 

Run the web app (then view in the browser at http://127.0.0.1:5000):

```sh
FLASK_APP=web_app flask run
```
## Testing

Run tests:

```sh
pytest
```

## Deployed Site

https://news-api-c9g1.onrender.com