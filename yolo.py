import _thread
import time


def worker():
    _thread.interrupt_main()


_thread.start_new_thread(worker, ())

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt as e:
    print("the main thread has been interrupted")
