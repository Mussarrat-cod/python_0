
import httpx    

def check_url(url):
    
    try:
        response=httpx.get(url,timeout=5)

        print(url, response.status_code)

    except httpx.HTTPError as error:
        print(url,"Failed",error)

def main():

    urls=[
        "https://www.google.com",
        "https://www.pytho  n.org",
        "https://fastapi.tiangolo.com"
    ]

    for url in urls:
        check_url(url)

main()
