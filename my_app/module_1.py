import time
from .api_utils import escape_hatch


@escape_hatch(start_message="I'm an escape hatch")
def function_that_runs_forever():
    """I'm a function that runs forever"""

    while 2 > 1:
        print("Just_Running")
        time.sleep(5)


def run():
    function_that_runs_forever()
