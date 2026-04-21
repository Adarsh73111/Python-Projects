from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

INSTAGRAM_EMAIL = "YOUR_EMAIL"
INSTAGRAM_PASSWORD = "YOUR_PASSWORD"
TARGET_ACCOUNT = "TARGET_USERNAME"


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        username_field = self.driver.find_element(By.NAME, "username")
        username_field.send_keys(INSTAGRAM_EMAIL)

        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(INSTAGRAM_PASSWORD)
        password_field.send_keys(Keys.ENTER)
        time.sleep(5)

        try:
            not_now = self.driver.find_element(By.XPATH, "//button[text()='Not Now']")
            not_now.click()
        except:
            pass

        time.sleep(3)

        try:
            not_now_notif = self.driver.find_element(By.XPATH, "//button[text()='Not Now']")
            not_now_notif.click()
        except:
            pass

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/followers")
        time.sleep(3)

        modal = self.driver.find_element(By.XPATH, "//div[@class='_aano']")

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

        self.all_followers = self.driver.find_elements(By.XPATH, "//div[@class='_aano']//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd']")

    def follow(self):
        for follower in self.all_followers:
            follower.click()
            time.sleep(2)

            try:
                follow_button = self.driver.find_element(By.XPATH, "//button[text()='Follow']")
                follow_button.click()
                time.sleep(2)
            except:
                try:
                    cancel_button = self.driver.find_element(By.XPATH, "//button[text()='Cancel']")
                    cancel_button.click()
                except:
                    pass

            self.driver.back()
            time.sleep(2)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()