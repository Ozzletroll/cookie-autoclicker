from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
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
        price = price.text
        if price != "":
            price_split = price.split(" - ")
            price_dict[price_split[0]] = int(price_split[1].replace(",", ""))

    cookies = int(driver.find_element(By.CSS_SELECTOR, "#money").text)

    for item in reversed(price_dict):
        if cookies > price_dict[item]:
            buy_item = driver.find_element(By.ID, f"buy{item}")
            buy_item.click()
            break


def autoclick():
    timer = time.time() + 1
    while timer >= time.time():
        cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
        time.sleep(0.01)
        cookie.click()


run = True
while run:
    autoclick()
    upgrades()
