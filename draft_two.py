import requests


def get_data():
    url = "https://apps.microsoft.com/store/category/Business"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "MS-CV": "03e8e3a3-f6b6-4152-bd87-851010ee9639",
        "Referer": "https://apps.microsoft.com/store/category/Business",
        "Request-Id": "|e58f47fc754641468ac735c6e677b333.1fe12409bb384e02",
        "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "traceparent": "00-e58f47fc754641468ac735c6e677b333-1fe12409bb384e02-01",
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"'
    }

    r = requests.get(url=url, headers=headers)

    with open("page_html.html", "w", encoding="utf-8") as file:
        file.write(r.text)
        file.close()


get_data()