# !/usr/bin/env python
__author__ = '@britodfbr'  # pragma: no cover
import keyword


def run():
    """Docker run -it --rm --name py311 -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3.11.0rc2-alpine3.16 python -c 'import this'
    docker run -it --rm --name py311 -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3.11.0rc2-alpine3.16 python main.py.
    """
    print(keyword.kwlist)


if __name__ == '__main__':  # pragma: no cover
    run()
