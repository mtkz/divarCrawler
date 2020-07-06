"""
author : mohammad tahourian
description : crawler of diver's site 
author_url : https://mtkz.ir 
version : 1.0.0

"""

import time
import detail

from selenium import webdriver


class Divar:

    items = []

    def __init__(self):
        self.driver = webdriver.Firefox()

    def url_data_getter(self, data, city):
        driver = self.driver

        URL = f"https://divar.ir/s/{city}?q="

        url = URL + data
        driver.get(url)

    def item_finder(self):
        driver = self.driver
        for i in range(2):
            driver.execute_script(
                'window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)

            items = driver.find_elements_by_class_name("post-card")

        for item in items:
            self.items.append(item.get_attribute("href"))


def main():

    data = input('Search a word  ... ')
    divar = Divar()
    cities = detail.CITIES

    for i in range(len(cities)):
        divar.url_data_getter(data, city=cities[i])
        divar.item_finder()

    with open('links.txt', 'w') as link:
        for item in divar.items:
            link.write(item)
            link.write("\n")

    link.close()  # finished the work

    print("data exported !")


# run app
if __name__ == "__main__":
    main()
