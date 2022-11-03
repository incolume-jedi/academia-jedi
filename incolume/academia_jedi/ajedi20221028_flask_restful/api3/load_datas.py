import requests
import csv
import pandas as pd


__author__ = "@britodfbr"  # pragma: no cover

# with open("data.csv") as f:
#     r = csv.reader(f)
#     data = [row for row in r if row]


df = pd.read_csv('https://raw.githubusercontent.com/jhnwr/flask-restful-demo'
                 '/main/data.csv')

# print(df)
# for i, values in df.iterrows():
#     print(values, end='\n---\n')


def post_data(item):
    headers = {"Content-type": "application/json"}
    payload = {
        "game_id": item[0],
        "home_team": item[1],
        "away_team": item[2],
        "home_score": item[3],
        "away_score": item[4],
    }
    resp = requests.post(
        "http://localhost:5555",
        headers=headers,
        json=payload
    )
    return resp.json()


# for item in data:
#     print(post_data(item))

for values in df.values:
    print(post_data(values))

