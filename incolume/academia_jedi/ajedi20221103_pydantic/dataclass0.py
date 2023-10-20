from datetime import datetime

from pydantic.dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str = 'John Doe'
    signup_ts: datetime = None


user = User(id='42', signup_ts='1997-06-20T12:34:56.789-03:00')
print(user)

# > User(
# id=42, name='John Doe', signup_ts=datetime.datetime(2032, 6, 21, 12, 0)
# )
