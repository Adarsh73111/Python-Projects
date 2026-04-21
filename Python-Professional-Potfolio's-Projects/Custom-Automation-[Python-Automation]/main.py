import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

FORM_URL = "YOUR_GOOGLE_FORM_LINK_HERE"
ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(ZILLOW_CLONE_URL)
soup = BeautifulSoup(response.text, "html.parser")

all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link["href"] for link in all_link_elements]

all_address_elements = soup.select("[data-test='property-card-addr']")
all_addresses = [address.text.replace(" | ", " ").strip() for address in all_address_elements]

all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.text.split("+")[0].strip("/mo").split()[0] for price in all_price_elements]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(all_links)):
    driver.get(FORM_URL)
    time.sleep(2)

    address_input = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address_input.send_keys(all_addresses[n])
    price_input.send_keys(all_prices[n])
    link_input.send_keys(all_links[n])
    submit_button.click()

driver.quit()
print("Project Complete! Check your Google Form Responses.")