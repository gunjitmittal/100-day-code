from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

PROMISED_DOWN = 300
PROMISED_UP = 100
CHROME_DRIVER_PATH = "/Users/gunji/Downloads/chromedriver"
TWITTER_PASSWORD = "Buffalo123"
TWITTER_EMAIL = "smtptestemail.0.1.2.3@gmail.com"
TWITTER_USERNAME = "just_Random1301"


class ComplaintBot:
    def __init__(self):
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP
        service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=service)
        self.practical_down = ""
        self.practical_up = ""

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(2)
        go_button = self.driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        go_button.click()
        sleep(60)
        down_speed = self.driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        self.practical_down = down_speed.text
        up_speed = self.driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        self.practical_up = up_speed.text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        sleep(3)
        email = self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        # nex = self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
        # nex.click()
        sleep(3)
        username = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_USERNAME)
        username.send_keys(Keys.ENTER)
        sleep(3)
        password = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        # login = self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div")
        # login.click()
        sleep(5)
        textbox = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        textbox.send_keys(f"Hey Internet Provider, why is my internet speed {self.practical_down}down/{self.practical_up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")


bot = ComplaintBot()
bot.get_internet_speed()
bot.tweet_at_provider()
