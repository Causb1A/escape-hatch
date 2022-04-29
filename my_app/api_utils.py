# Base Library Packages
import _thread

# Third Party Packages
from pynput import keyboard
from functools import wraps
import sys


def escape_hatch(
    start_message="",
    end_message="",
    keyboard_key=keyboard.Key.esc,
    key_string="Esc",
):
    """Function to decorate API calls as an escape hatch
    Args:
      method: method to be decorated
      keyboard_key (keyboard.Key or keyboard.KeyCode):
    interrupt key to listen for
      key_string (str): string representation of key to print in message"""

    def decorate(func):
        def keyboard_handler(key, escape_key=keyboard_key):
            if key == escape_key:
                print("    Program terminated by user")
                _thread.interrupt_main()

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Handle keyboard interrupts by user
            with keyboard.Listener(on_press=keyboard_handler):
                print(start_message)
                print(
                    f"    Press '{key_string}' any time to terminate the program",
                )
                # Do inner function
                result = func(*args, **kwargs)

                # Print message after API response received
                print()(end_message)
            return result

        return wrapper

    return decorate
