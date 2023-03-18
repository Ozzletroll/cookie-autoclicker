from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("C:/Program Files (x86)/Google/Chrome/chromedriver.exe")
options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

run = True
while run:
    cookies_total = driver.find_element(By.CSS_SELECTOR, "#money")
    cookies = int(cookies_total.text)
    cps = driver.find_element(By.CSS_SELECTOR, "#cps")
    cps_text = cps.text.split(": ")
    cookies_per_second = float(cps_text[1])

    # Cookie autoclick
    cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
    cookie.click()












driver.quit()