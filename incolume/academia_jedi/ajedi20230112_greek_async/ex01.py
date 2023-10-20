import asyncio


async def function_asyc():
    for i in range(100000):
        if i % 50000 == 0:
            print("Hello, I'm Abhishek")
            print('GFG is Great')

            # New Line Added
            await asyncio.sleep(0.01)
    return 0


async def function_2():
    print('\n HELLO WORLD \n')
    return 0


async def main():
    f1 = loop.create_task(function_asyc())
    f2 = loop.create_task(function_2())
    await asyncio.wait([f1, f2])


if __name__ == '__main__':  # pragma: no cover

    # to run the above function we'll
    # use Event Loops these are low level
    # functions to run async functions
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

    # You can also use High Level functions Like:
