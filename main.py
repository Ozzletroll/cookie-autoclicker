from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import threading
import time

service = Service("C:/Program Files (x86)/Google/Chrome/chromedriver.exe")
options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")


def check_upgrades():
    # Upgrade cost check
    time_machine_cost = driver.find_element(By.CSS_SELECTOR, "#buyTime\ machine > b")
    time_machine_cost_formatted = int(time_machine_cost.text.split(" - ")[1].replace(",", ""))

    portal_cost = driver.find_element(By.CSS_SELECTOR, "#buyPortal > b")
    portal_cost_formatted = int(portal_cost.text.split(" - ")[1].replace(",", ""))

    alchemy_cost = driver.find_element(By.CSS_SELECTOR, "#buyAlchemy\ lab > b")
    alchemy_cost_formatted = int(alchemy_cost.text.split(" - ")[1].replace(",", ""))

    shipment_cost = driver.find_element(By.CSS_SELECTOR, "#buyShipment > b")
    shipment_cost_formatted = int(shipment_cost.text.split(" - ")[1].replace(",", ""))

    mine_cost = driver.find_element(By.CSS_SELECTOR, "#buyMine > b")
    mine_cost_formatted = int(mine_cost.text.split(" - ")[1].replace(",", ""))

    factory_cost = driver.find_element(By.CSS_SELECTOR, "#buyFactory > b")
    factory_cost_formatted = int(factory_cost.text.split(" - ")[1].replace(",", ""))

    grandma_cost = driver.find_element(By.CSS_SELECTOR, "#buyGrandma > b")
    grandma_cost_formatted = int(grandma_cost.text.split(" - ")[1].replace(",", ""))

    cursor_cost = driver.find_element(By.CSS_SELECTOR, "#buyCursor > b")
    cursor_cost_formatted = int(cursor_cost.text.split(" - ")[1].replace(",", ""))

    # Check if player can afford upgrades
    if cookies > time_machine_cost_formatted:
        time_buy = driver.find_element(By.CSS_SELECTOR, "#buyTime\ machine")
        time_buy.click()
    elif cookies > portal_cost_formatted:
        portal_buy = driver.find_element(By.CSS_SELECTOR, "#buyPortal > b")
        portal_buy.click()
    elif cookies > alchemy_cost_formatted:
        alchemy_buy = driver.find_element(By.CSS_SELECTOR, "#buyAlchemy\ lab")
        alchemy_buy.click()
    elif cookies > shipment_cost_formatted:
        shipment_buy = driver.find_element(By.CSS_SELECTOR, "#buyShipment")
        shipment_buy.click()
    elif cookies > mine_cost_formatted:
        mine_buy = driver.find_element((By.CSS_SELECTOR, "#buyMine > b"))
        mine_buy.click()
    elif cookies > factory_cost_formatted:
        factory_buy = driver.find_element((By.CSS_SELECTOR, "#buyFactory"))
        factory_buy.click()
    elif cookies > grandma_cost_formatted:
        grandma_buy = driver.find_element((By.CSS_SELECTOR, "#buyGrandma"))
        grandma_buy.click()
    elif cookies > cursor_cost_formatted:
        cursor_buy = driver.find_element(By.CSS_SELECTOR, "#buyCursor")
        cursor_buy.click()


def autoclick():
    timer = time.time() + 5
    while timer >= time.time():
        cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
        cookie.click()


run = True
while run:
    cookies_total = driver.find_element(By.CSS_SELECTOR, "#money")
    cookies = int(cookies_total.text)
    cps = driver.find_element(By.CSS_SELECTOR, "#cps")
    cps_text = cps.text.split(": ")
    cookies_per_second = float(cps_text[1])

    autoclick()
    check_upgrades()

# driver.quit()