import asyncio
from platform import python_version

if python_version() < '3.11.0':
    print("This application need Python 3.11+")
    exit(1)


async def read_file(filename: str):
    with open(filename) as f:
        data: str = f.read()
    return data


async def fetch_data(data: int) ->dict:
    if data == 0:
        raise Exception('No data found..')
    return {'data': data}


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(read_file('anime.png'))
            tg.create_task(read_file('icon.png'))
            tg.create_task(read_file('python.png'))
            tg.create_task(read_file('file.png'))
            # await asyncio.sleep(2)
            tg.create_task(fetch_data(0))
        print('Completed.')
    except* FileNotFoundError as eg:
        for error in eg.exceptions:
            print(error)
    except* Exception as e:
        print(e.exceptions)

if __name__ == '__main__':    # pragma: no cover
    asyncio.run(main())
