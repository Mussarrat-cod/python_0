import asyncio
import httpx


async def check_url(url):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=5)
            print(url, response.status_code)

    except httpx.HTTPError as error:
        print(url, "Failed", error)


async def check_all_urls():
    urls = [
        "https://www.google.com",
        "https://www.python.org",
        "https://fastapi.tiangolo.com"
    ]

    for url in urls:
        await check_url(url)


def main():
    asyncio.run(check_all_urls())


main()