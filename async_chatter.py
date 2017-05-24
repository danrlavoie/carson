import asyncio
import sys
import asyncio
from time import time
from math import log

if sys.platform == 'win32':
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)

def process_input():
    text = sys.stdin.readline()
    n = int(text.strip())
    print('fib({}) = {}'.format(n, log(n)))


@asyncio.coroutine
def print_hello():
    while True:
        print("{} - Hello world!".format(int(time())))
        yield from asyncio.sleep(3)


def main():
    loop = asyncio.get_event_loop()
    loop.add_reader(sys.stdin, process_input)
    loop.run_until_complete(print_hello())


if __name__ == '__main__':
    main()
# def main():
#     loop = asyncio.get_event_loop()
#     loop.add_reader(sys.stdin, handle_stdin)
#     loop.run_until_complete(tick())    

    # loop = asyncio.get_event_loop()
    # try:
    #     loop.run_until_complete(just_print_messages())
    # finally:
    #     loop.close()
 
if __name__ == '__main__':
    main()