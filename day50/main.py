from time import sleep

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/gunji/Downloads/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://tinder.com/app/recs")
sleep(2)
log_in_btn = driver.find_element(by=By.LINK_TEXT, value="Log in")
log_in_btn.click()
sleep(1)
more_btn = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/button")
more_btn.click()
sleep(1)
face_btn = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]")
face_btn.click()
sleep(5)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
email = driver.find_element(by=By.ID, value="email")
email.send_keys("gunjitmittal1@gmail.com")
password = driver.find_element(by=By.ID, value="pass")
password.send_keys("NSTSErank1")
log_btn = driver.find_element(by=By.NAME, value="login")
log_btn.click()
driver.switch_to.window(base_window)
sleep(10)
loc_btn = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div/div[3]/button[1]")
loc_btn.click()
sleep(1)
add_btn = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div/div[3]/button[2]/span")
add_btn.click()
coo_btn = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button")
sleep(20)
dis_btn = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button")
for i in range(100):
    dis_btn.click()
    sleep(2)