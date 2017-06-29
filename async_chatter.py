#!/usr/bin/env python

import asyncio
import random
import sys
from time import time
from math import log
from src.text_parse import TextParse

if sys.platform == 'win32':
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)
class AsyncChatter:
    def __init__(self):
        self.parser = TextParse()
    def process_input(self):
        text = sys.stdin.readline()
        text = self.parser.remove_punctuation(text)
        text = self.parser.remove_caps_preserve_nnp(text)
        if ('quit' in text):
            sys.exit()
        print("Your input was: " + text)


    @asyncio.coroutine
    def schedule_function(self, delay, func, **kwargs):
        # Delay is a value of seconds
        yield from asyncio.sleep(delay)
        print(kwargs)
        func(**kwargs)

    def print_hello(self, name, message):
        print('Hello ' + name + ' ' + message + '.')

    def greet(self):
        greeting_list = [
            "Good morning.",
            "How are you doing today?",
            "What can I do for you?",
        ]
        print(random.choice(greeting_list))

    def main(self):
        self.greet()
        loop = asyncio.get_event_loop()
        loop.add_reader(sys.stdin, self.process_input)
        loop.run_forever()

if __name__ == '__main__':
    AsyncChatter().main()
