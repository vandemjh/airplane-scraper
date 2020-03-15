# Logs all html available through terrible airplane wifi
# Requires requests
import os
import requests
import sys


URL = "https://www.aainflight.com/media/1"
page = requests.get(URL)
print(page.status_code)
print(page.content)
