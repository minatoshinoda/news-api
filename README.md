# my-first-app

## Setup

Create a virtual environment (first time only):

```sh
conda create -n reports-env-2024 python=3.10
```

Activate the environment (whenever you come back to this project):

```sh
conda activate reports-env-2024
```

Install packages:

```sh
pip install -r requirements.txt
```

[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

TODO include instructions here for signing up for email sending platform 

Create a ".env" file and add contents like the following (using your own AlphaVantage API Key):

```sh
# this is the ".env" file:
ALPHAVANTAGE_API_KEY="..."
```

## Usage

Run the example script:

```sh
python app/my_script.py
```

Run the unemployment report:

```sh
#ALPHAVANTAGE_API_KEY="..." python app/unemployment.py

python -m app.unemployment
```
Run the stocks report:

```sh
python -m app.stocks
```
### Web App 

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

## Testing

Run tests:

```sh
pytest
```