import requests
import random
import time


URL = "http://aoshang.com.au/main/home/mall"

r = requests.get("http://aoshang.com.au/main/home/mall")
# print(r.text)
# print(r.json())
# print(r.headers)
print(r.status_code)
print(r.content)
URLS = ['http://aoshang.com.au/main/home/mall',
      'http://aoshang.com.au/main/home/cat?categoy=%E9%99%90%E6%97%B6%E7%89%B9%E6%83%A0&page=2',
      'http://aoshang.com.au/main/home/cat?categoy=%E5%A9%B4%E5%84%BF%E5%A5%B6%E7%B2%89'
        ]

for ls in URLS:
    r = requests.get(url=ls)

