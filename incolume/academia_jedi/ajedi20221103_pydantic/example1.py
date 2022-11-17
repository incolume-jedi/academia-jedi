"""Pydantic python 3.10+."""
from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: datetime | None = None
    friends: list[int] = []


if __name__ == '__main__':  # pragma: no cover

    external_data = {
        'id': '123',
        'signup_ts': '2019-06-01T12:22:12.3456+03.30',
        'friends': [1, 2, '3'],
    }
    user = User(**external_data)
    print(user.id)
    # > 123
    print(repr(user.signup_ts))
    # > datetime.datetime(2019, 6, 1, 12, 22)
    print(user.friends)
    # > [1, 2, 3]
    print(user.dict())
    """
    {
        'id': 123,
        'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
        'friends': [1, 2, 3],
        'name': 'John Doe',
    }
    """
