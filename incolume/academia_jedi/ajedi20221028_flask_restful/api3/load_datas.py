import requests
import csv
import pandas as pd


__author__ = "@britodfbr"  # pragma: no cover

# with open("data.csv") as f:
#     r = csv.reader(f)
#     data = [row for row in r if row]


df = pd.read_csv(
    'https://raw.githubusercontent.com/jhnwr/flask-restful-demo/main/data.csv',
    header=None,
    names=["game_id", "home_team", "away_team", "home_score", "away_score"]
)

# print(df)
# print(df.columns)
# print(df.info())
# for i, values in df.iterrows():
#     print(values, end='\n---\n')

# for values in df.values:
#     print(values)


def post_data(item):
    headers = {
        "Content-type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.5112.102 Safari/537.36",
    }
    # payload = {
    #     "game_id": item[0],
    #     "home_team": item[1],
    #     "away_team": item[2],
    #     "home_score": item[3],
    #     "away_score": item[4],
    # }
    payload = item.to_dict()
    resp = requests.post(
        "http://localhost:5555",
        headers=headers,
        json=payload
    )
    return resp.json()


# for item in data:
#     print(post_data(item))

for i, values in df.iterrows():
    print(post_data(values))

