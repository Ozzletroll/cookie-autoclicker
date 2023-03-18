from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service("C:/Program Files (x86)/Google/Chrome/chromedriver.exe")
options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")


def upgrades():
    store = driver.find_elements(By.CSS_SELECTOR, "#store b")
    price_dict = {}
    for price in store:
        price_split = price.text.split(" - ")
        price_dict[price_split[0]] = int(price_split[1])

    affordable_upgrades = {}
    for item in price_dict:
        pass

def autoclick():
    timer = time.time() + 5
    while timer >= time.time():
        cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
        cookie.click()


run = True
while run:
    #
    # cps = driver.find_element(By.CSS_SELECTOR, "#cps")
    # cps_text = cps.text.split(": ")
    # cookies_per_second = float(cps_text[1])

    upgrades()
    time.sleep(5)

driver.quit()