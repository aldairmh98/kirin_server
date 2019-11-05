#from rasa.core.agent import Agent
#from rasa.core.interpreter import RasaNLUInterpreter
import asyncio
import threading
import sys
import time
import logging
from watchdog.observers import Observer
from my_handler import my_LoggingEventHandler
from git import Repo
from random import seed
from random import random

repo = Repo('.')

def tasksAutomation(intent):
    if intent == 'version':
        branch = repo.active_branch
        print(branch.name)

async def main():
    agent = Agent.load("./models/nlu.tar.gz")
    x = threading.Thread(target=watcher, daemon=True)
    x.start()
    the_input = 'not is exit definitively'
    while(the_input != 'exit'):
        print('Type exit to exit: What Do you want bro?')
        the_input = input()
        the_message = await agent.parse_message_using_nlu_interpreter(the_input)
        print(the_message['intent'])

def watcher():
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = my_LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

if __name__ == "__main__":
    changedFiles = [ item.a_path for item in repo.index.diff(None) ]
    print(changedFiles)
    repo.index.add(changedFiles)
    repo.index.commit(str(random))
    #asyncio.run(main())
    #Another change to proof this stuff bro gg