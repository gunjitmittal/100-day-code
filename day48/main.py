from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/gunji/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(by=By.NAME, value="fName")
fname.send_keys("Hello")
lname = driver.find_element(by=By.NAME, value="lName")
lname.send_keys("World")
email = driver.find_element(by=By.NAME, value="email")
email.send_keys("helloworld@123.com")
submit = driver.find_element(by=By.CSS_SELECTOR, value="button")
submit.click()
# driver.quit()
