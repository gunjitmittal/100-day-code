from bs4 import BeautifulSoup
import requests

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

CHROME_DRIVER_PATH = "/Users/gunji/Downloads/chromedriver"
service = Service(executable_path=CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)
url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.60121382666016%2C%22east%22%3A-122.26544417333984%2C%22south%22%3A37.70293627371233%2C%22north%22%3A37.84757588976889%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }
i = 0
page = requests.get(url, headers=headers)
contents = page.text
soup = BeautifulSoup(contents, 'html.parser')
addresses = soup.find_all("address", class_="list-card-addr")
add_text = [address.text for address in addresses]
links = soup.find_all("a", class_="list-card-img")
link_text = [link.get('href') for link in links]
prices = soup.find_all("div", class_="list-card-price")
price_text = [price.text.split("$")[1].split("+")[0].split("/")[0].replace(",", "") for price in prices]
for link in link_text:
    linky = link
    if linky[0] == '/':
        link = "https://www.zillow.com" + linky
    link_text[i] = link
    i += 1
print(add_text)
print(link_text)
print(price_text)

form_url = "https://forms.gle/PLyTwwXsiHufUYAB8"
for i in range(len(price_text)):
    driver.get(form_url)
    sleep(5)
    adress = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    adress.send_keys(add_text[i])
    pric = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    pric.send_keys(price_text[i])
    lin = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    lin.send_keys(link_text[i])
    sub = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
    sub.click()
