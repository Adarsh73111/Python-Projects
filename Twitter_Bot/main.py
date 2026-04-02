from selenium import webdriver
from selenium.webdriver.common.by import By
import tweepy
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "YOUR_EMAIL"
TWITTER_PASSWORD = "YOUR_PASSWORD"
TWITTER_USERNAME = "YOUR_USERNAME"

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.down = 0
        self.up = 0
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        time.sleep(3)

        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        time.sleep(60)

        self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)

        print(f"Download: {self.down} Mbps")
        print(f"Upload: {self.up} Mbps")

    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            client = tweepy.Client(
                consumer_key=API_KEY,
                consumer_secret=API_SECRET,
                access_token=ACCESS_TOKEN,
                access_token_secret=ACCESS_TOKEN_SECRET
            )

            tweet = (f"Hey @YourInternetProvider, why is my internet speed so slow?! "
                     f"I'm getting {self.down} Mbps down and {self.up} Mbps up "
                     f"but I'm paying for {PROMISED_DOWN} Mbps down and {PROMISED_UP} Mbps up!")

            client.create_tweet(text=tweet)
            print("Tweet sent!")
        else:
            print("Speed is fine, no tweet needed.")

        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()