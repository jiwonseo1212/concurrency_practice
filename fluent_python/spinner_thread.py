import itertools
import time
from threading import Thread, Event


def spin(msg: str, done: Event) -> None:
    """
    args : done => instance of threading.Event a simple object to synchronize threads
    """
    for char in itertools.cycle(r'\|/-'): #inifinite loop
        status = f'\r{char}{msg}'
        print(status, end=" ", flush=True)
        if done.wait(.1): #.1s timeout sets the frame rate of the aninmation to 10 FBS 
            break
    blanks = " " * len(status)
    print(f"\r{blanks}\r", end=" ")

def slow() -> int: #called by main threade slow API call over the network
    time.sleep(3)
    return 42

def supervisor() -> int:
    done = Event()
    spinner = Thread(target=spin, args = ("thinking!", done))
    print(f"spinner object : {spinner}") # initial state means this Thread is not started yet
    spinner.start() # start the thread
    result = slow() # blocks the main thread MeanWhile the secondary thread is running the spinner animation
    done.set() #set the event flag to True, this will terminate the for loop inside the spin function
    spinner.join() # wait until the spinner thread finishes
    return result

def main() -> None:
    result = supervisor()
    print(f"Answer : {result}")

if __name__ == "__main__":
    main()