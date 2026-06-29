import asyncio
import time 
def timer(func):
    async def wrapper(*args, **kwargs):
        st = time.time()
        await func()
        end = time.time()
        print(f"The time to run {func.__name__} is {end-st}")
    return wrapper

@timer
async def co_routine1():
    print("Co-routine 1 Working...")
    await asyncio.sleep(5)           
    print("Co-routine 1 completed")

async def co_routine2():
    print("Co-routine 2 Working...")
    await asyncio.sleep(3)              # thread waits here because of await
    print("Co-routine 2 completed")

async def co_routine3():
    print("Co-routine 3 Working...")
    await asyncio.sleep(2)              
    print("Co-routine 3 completed")

@timer
async def main(): # Creating a single Coroutine gathering all 
    await asyncio.gather(
        co_routine1(), 
        co_routine2(),
        co_routine3()
    )

if __name__ == "__main__":  # running the bigger coroutine 
    asyncio.run(main())


