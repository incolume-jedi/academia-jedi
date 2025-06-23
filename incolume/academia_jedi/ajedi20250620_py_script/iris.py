#!/usr/bin/env python3
"""Script iris."""
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "ucilmrepo>=0.0.7",
# ]
# ///

from ucimlrepo import fetch_ucirepo


IRIS_DATASET_ID = 53
def main() -> None:
    """Chamada script iris."""
    print('Hello from script iris.py!')
    print("Fetching Iris dataset using ucimlrepo...")
    iris = fetch_ucirepo(id=IRIS_DATASET_ID)
    print("Dataset fetched successfully. Variable summary:")
    print(iris.variables)




if __name__ == '__main__':
    main()
