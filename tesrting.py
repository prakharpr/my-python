from bs4 import beautifulscop
import requests
import requests.exceptions
import urllib.parse
from collection import deque
import re

user_url = str(input('[+]Enter url : '))
urls = deque([user_url])

scrapped_url = set()
email = set()

count = 0
try:
    while len(urls):
        count += 1
        if count == 100:
            break
            scrapped_url.add(urls)

            parts=urllib.parse.urlsplit(urls)
            base_url = '{0.scheme}' ://