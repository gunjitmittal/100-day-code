from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

timeout = time.time() + 60*5
upgrade_timeout = time.time() + 5
chrome_driver_path = "/Users/gunji/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(by=By.ID, value="cookie")
store = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
prices = [int(store[i].text.split("-")[1].strip().split('\n')[0].replace(',', '')) for i in range(len(store)-1)]
money = driver.find_element(by=By.ID, value="money")
while True:
    cookie.click()
    if time.time() > timeout:
        break
    if time.time() > upgrade_timeout:
        gray_store = driver.find_elements(by=By.CSS_SELECTOR, value="#store .grayed")
        gray_prices = [int(gray_store[i].text.split("-")[1].strip().split('\n')[0].replace(',', '')) for i in range(len(gray_store)-1)]
        ava_prices = []
        for price in prices:
            if price not in gray_prices:
                ava_prices.append(price)
        maxi = prices.index(max(ava_prices))
        store = driver.find_elements(by=By.CSS_SELECTOR, value="#store div b")
        store[maxi].click()
        upgrade_timeout += 5

cps = driver.find_element(by=By.ID, value="cps")
print(cps.text.split(':')[1].strip())
driver.close()
