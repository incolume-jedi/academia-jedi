"""JSON Processing."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

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
