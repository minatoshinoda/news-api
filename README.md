# my-first-app

## Setup

Create a virtual environment:

```sh
conda create -n reports-env-2024 python=3.10
```

Activate the environment:

```sh
conda activate reports-env-2024
```

Install packages:

```sh
pip install -r requirements.txt
```

[Obtain an API Key](https://newsapi.org/account)

TODO include instructions here for signing up for email sending platform 

Create a ".env" file and add contents like the following:

```sh
# this is the ".env" file:
NEWSAPI_KEY="..."
```


## Web App 

Run the web app (then view in the browser at http://localhost:5000/):

```sh
FLASK_APP=web_app flask run
```
## Testing

Run tests:

```sh
pytest
```