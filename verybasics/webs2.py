import asyncio
import aiohttp


async def fetch_website(session, url):

    try:
        print("Fetching:", url)

        async with session.get(url) as response:
            content = await response.text()

            print(url, response.status)
            print(content[:250])
            print("-------------------")

    except aiohttp.ClientError as error:
        print("Failed:", url, error)


async def main():

    urls = [
        "https://www.google.com",
        "https://www.github.com"
    ]

    async with aiohttp.ClientSession() as session:

        for url in urls:
            await fetch_website(session, url)

    print("All websites checked!")


asyncio.run(main())