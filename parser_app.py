import time

import requests
from bs4 import BeautifulSoup
import json
import re
from selenium import webdriver

driver = webdriver.Chrome()
time.sleep(1)
driver.get("https://apps.microsoft.com/store/detail/slack/9WZDNCRDK3WP")
app_page_html = driver.page_source

print()