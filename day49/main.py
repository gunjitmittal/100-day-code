from time import sleep

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/gunji/Downloads/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
sleep(2)
sign_in = driver.find_element(by=By.CLASS_NAME, value="cta-modal__primary-btn")
sign_in_web = sign_in.get_attribute("href")
sign_in.click()
sleep(3)
username = driver.find_element(by=By.ID, value="username")
username.send_keys("gunjitmittal2@gmail.com")
password = driver.find_element(by=By.ID, value="password")
password.send_keys("buffalo")
button = driver.find_element(by=By.CLASS_NAME, value="btn__primary--large")
button.click()
sleep(5)
easy = driver.find_element(by=By.CLASS_NAME, value="jobs-apply-button")
easy.click()
sleep(2)
number = driver.find_element(by=By.CLASS_NAME, value="ember-text-field")
number.send_keys("0987654321")
next1 = driver.find_element(by=By.CLASS_NAME, value="artdeco-button--primary")
next1.click()
sleep(2)
next2 = driver.find_element(by=By.CLASS_NAME, value="artdeco-button--primary")
next2.click()
sleep(2)
experience = driver.find_element(by=By.NAME, value="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3175824042,63657634,numeric)")
experience.send_keys("1")
review = driver.find_element(by=By.CLASS_NAME, value="artdeco-button--primary")
review.click()
driver.close()
