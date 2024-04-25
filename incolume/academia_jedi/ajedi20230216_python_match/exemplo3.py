"""JSON Processing."""

orders = [
    {
        'statusCode': 200,
        'id': 1345347,
        'price': 235.80,
        'items': ['HDD', 'CPU', 'Headphones', 'Webcam'],
    },
    {'statusCode': 500, 'id': 0, 'price': 0, 'items': []},
    {'statusCode': 202, 'id': 3453, 'price': 30.80, 'items': ['Thumb Drive']},
    {
        'statusCode': 404,
    },
    {'statusCode': 200, 'price': 30.80, 'items': ['Thumb Drive']},
    {'statusCode': 200, 'id': 3453, 'price': 30.80, 'items': ['Thumb Drive']},
]


def process_json(response: dict):
    match response:
        case {
            'statusCode': 200,
            'id': _,
            'price': _,
            'items': [*products],
        }:  # Capture list
            print(f'Order contains following products: {products}')
        case {
            'statusCode': code,
            'id': _,
            'price': _,
            'items': _,
        } if code >= 400:  # Capture and guard
            print(f'Failed with status code: {code}')
        case {'statusCode': _, 'price': _, 'items': _}:
            print('Missing required field: ID')
        case {
            'statusCode': code,
            **fields,
        }:  # Destructure rest of the dictionary
            print(f'Code: {code}, data: {fields}')


def run():
    for order in orders:
        process_json(order)

    # Order contains following products: ['HDD', 'CPU', 'Headphones', 'Webcam']
    # Failed with status code: 500
    # Missing required field: ID
    # Code: 404, data: {}


if __name__ == '__main__':  # pragma: no cover
    run()
