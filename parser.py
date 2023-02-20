import time
import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import json


# driver = webdriver.Chrome()
# driver.get("https://apps.microsoft.com/store/category/Business")
# driver.set_window_size(1920, 1080)
#
# pixel_down = 200
# while pixel_down < 1000:
#     driver.execute_script(f"window.scrollBy(0,{pixel_down})", "")
#     time.sleep(3)
#     pixel_down += 200
#
# page_html = driver.page_source
#
# with open("main_page_bussines.html", "w", encoding="utf-8") as file:
#     file.write(page_html)
#     file.close()

# file = open("main_page_bussines.html", "r", encoding="utf-8")
# page = file.read()
#
# # спускаемся по дереву и извлекаем список всех тегов <a>
# soup = BeautifulSoup(page, "lxml")
# tree = soup.find("div", {"id": "root"}).find("div", {"id": "main"})
# tree = tree.find("div", {"class": "c0198 c013 c0126"}).find("div", {"role": "main"})
# all_a = tree.find("div", {"id": "all-products-listall-list-container"}).find_all("a")

# извлекаем из тегов <a> все ссылки и имена приложений
# apps_title_href_dict = {}
# for link in all_a:
#     title = link.find("span", {"class": "title-span"}).text
#     url = "https://apps.microsoft.com" + link.get("href")
#
#     apps_title_href_dict[title] = url
#
# # записываем список в файл JSON
# with open("apps_links.json", "w", encoding="utf-8") as file:
#     json.dump(apps_title_href_dict, file, indent=4, ensure_ascii=False)

with open("apps_links.json", encoding="utf-8") as file:
    apps_title_href = json.load(file)

count_apps = int(len(apps_title_href))
list_apps = []
count = 0
for title_app, link_app in apps_title_href.items():

    rep = [" ", "-", " -", ", ", ",", ": ", ": ", " , ", ":", ":"]
    for item in rep:
        if item in title_app:
            title_app = title_app.replace(item, "_")

    # проходимся по каждой ссылке с помощью webdriver
    driver = webdriver.Chrome()
    driver.get(link_app)
    time.sleep(2)
    driver.execute_script(f"window.scrollBy(0,500)", "")
    time.sleep(1)
    driver.execute_script(f"window.scrollBy(0,500)", "")
    app_page_html = driver.page_source

    # создаем файд html для каждой страницы с приложением
    file = open(f"data_pages/{count}_{title_app}.html", "w", encoding="utf-8")
    file.write(app_page_html)
    file.close()

    file = open(f"data_pages/{count}_{title_app}.html", "r", encoding="utf-8")
    page_html = file.read()

    soup = BeautifulSoup(page_html, "lxml")

    try:
        # получаем имя компании
        company_name = soup.find("h6", {"id": "publisherHeader_responsive"}).find_next().text.capitalize()

        # получаем дату релиза
        release = soup.find("h6", {"id": "versionHeader_responsive"}).find_next().text
        release = release.split(":")
        release = release[1].strip()

        list_apps.append(
            {
                "Title": title_app,
                "Company": company_name,
                "Release year": release,
            }
        )
    except Exception:
        print(f"{title_app} not found page_source")
        list_apps.append(
            {
                "Title": title_app,
                "Company": "not found",
                "Release year": "not found",
            }
        )

    count += 1
    count_apps -= 1

    stop_itaerable = 0

    if count_apps == stop_itaerable:
        print("Работа завершена или цикл прерван успешно")

    print(f"{title_app}: записан\nВсего выполнено: {count}\nОсталось: {count_apps}\n")

with open("apps_information.json", "w", encoding="utf-8") as file:
     json.dump(list_apps, file, indent=4, ensure_ascii=False)














