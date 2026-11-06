import asyncio
import aiohttp

async def fetch_page(session, url, name):
    print(f"[{name}] Starting download...")
    
    # We use the shared session passed from main()
    async with session.get(url) as response:
        html_content = await response.text()
        print(f"[{name}] Got the data!")
        return html_content[:200]

async def main():
    print("Program started. Fetching both sites concurrently using a shared session!")
    
    # 1. Open ONE session here so both tasks can share it
    async with aiohttp.ClientSession() as session:
        
        # 2. Fire off both requests at the exact same time using gather
        google_result, github_result = await asyncio.gather(
            fetch_page(session, "https://www.google.com", "Google"),
            fetch_page(session, "https://www.github.com", "GitHub")
        )
        
    print("\n🎉 Both tasks finished at the same time!")

if __name__ == "__main__":
    asyncio.run(main())