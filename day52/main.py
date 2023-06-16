from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

CHROME_DRIVER_PATH = "/Users/gunji/Downloads/chromedriver"
IG_PASSWORD = "Buffalo123"
IG_USERNAME = "just_Random1301"
SIMILAR_ACCOUNT = "chefsteps"


class FollowerBot:
    def __init__(self):
        service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=service)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(3)
        username = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input")
        username.send_keys(IG_USERNAME)
        password = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input')
        password.send_keys(IG_PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(5)
        not_now = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/section/main/div/div/div/div/button")
        not_now.click()
        sleep(2)
        noti = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]")
        noti.click()
        sleep(2)

    def find_followers(self):
        search = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/div[1]/div")
        search.click()
        sleep(2)
        recent = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/ul/div/a/div/div[2]/div[2]/div")
        recent.click()
        sleep(3)
        followers = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a")
        followers.click()
        sleep(2)
        scr1 = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]')
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)

    def follow(self):
        pass


bot = FollowerBot()
bot.login()
bot.find_followers()
bot.follow()
