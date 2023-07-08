import itertools
import time
from multiprocessing import Process, Event #threading.Event is a class but multiprocessing.Event is a function  which returns synchronize.Event instance ?? 
from multiprocessing import synchronize

def spin(msg: str, done: synchronize.Event) -> None:
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
    spinner = Process(target=spin, 
                      args = ("thinking!", done))
    print(f"spinner object : {spinner}")
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result

def main() -> None:
    result = supervisor()
    print(f"Answer : {result}")

if __name__ == "__main__":
    main()