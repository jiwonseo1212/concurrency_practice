import asyncio
import itertools
import time

async def spin(msg: str) -> None:
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, flush=True, end="")
        try:
            await asyncio.sleep(.1) # use asyncio sleep to pause without blocking other coroutines. 
        except asyncio.CancelledError: # raised when cancel method called
            break
    blanks = " "*len(status)
    print(f"\r{blanks}\r", end=" ")

async def slow() -> int:
    await asyncio.sleep(3)
    return 42

def main() -> None:
    result = asyncio.run(supervisor())
    print(f"Answer : {result}")


async def supervisor() -> int:
    spinner = asyncio.create_task(spin("thinking"))
    print(f"spinner object : {spinner}")
    result = await slow()
    spinner.cancel()
    return result

if __name__ == "__main__":
    main()