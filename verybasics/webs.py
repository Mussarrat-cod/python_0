
import asyncio
import aiohttp


async def fetch_website(session, url):

    try:
        print("Fetching:", url)

        async with session.get(url) as response:

            content = await response.text()

            print("Website:", url)
            print("Status:", response.status)
            print("Content:", content[:250])
            print("------------------------")

    except aiohttp.ClientError as error:
        print("Failed:", url, error)


async def main():

    urls = [
        "https://www.google.com",
        "https://www.github.com"
    ]

    async with aiohttp.ClientSession() as session:

        task1 = asyncio.create_task(
            fetch_website(session, urls[0])
        )

        task2 = asyncio.create_task(
            fetch_website(session, urls[1])
        )

        await task1
        await task2

    print("All websites checked!")


if __name__ == "__main__":
    asyncio.run(main())
