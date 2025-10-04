import asyncio


async def greet(name: str):
    print(f"Hello {name}")
    await asyncio.sleep(1)
    print(f"Done greeting {name}")


async def main():
    await asyncio.gather(greet("Tony"), greet("Merlin"), greet("Linus"))


if __name__ == "__main__":
    asyncio.run(main())
