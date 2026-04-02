import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# --- PHASE 1: WEB SCRAPING ---
ZILLOW_CONE_URL = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(ZILLOW_CONE_URL)
zillow_web_page = response.text
soup = BeautifulSoup(zillow_web_page, "html.parser")

all_links_elements = soup.select(".property-card-link")
all_links = [link.get("href") for link in all_links_elements]

all_address_elements = soup.select("address")
all_addresses = [address.get_text().strip() for address in all_address_elements]

all_price_elements = soup.select(".PropertyCardWrapper__StyledPriceLine")
all_prices = [price.get_text().strip().split("+")[0].split("/")[0] for price in all_price_elements]

print(f"Total Links: {len(all_links)}")
print(f"Total Addresses: {len(all_addresses)}")
print(f"Total Prices: {len(all_prices)}\n")

# --- PHASE 2: AUTOMATION ---
FORM_URL = "YOUR_GOOGLE_FORM_URL_LINK_HERE"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Loop through all 44 properties
for n in range(len(all_links)):
    driver.get(FORM_URL)

    # Wait for the form to load
    time.sleep(2)
    print(f"Filling out form for property {n + 1}/{len(all_links)}")

    # Locate the fields using YOUR XPaths
    address_input = driver.find_element(By.XPATH,
                                        'YOUR_ADDRESS_XPATH_HERE')
    price_input = driver.find_element(By.XPATH,
                                      'YOUR_PRICE_XPATH_HERE')
    link_input = driver.find_element(By.XPATH,
                                     'YOUR_PROPERTY_LINK_XPATH_HERE')
    submit_button = driver.find_element(By.XPATH, 'YOUR_SUBMIT_BUTTON_XPATH_HERE')

    # Type the data
    address_input.send_keys(all_addresses[n])
    price_input.send_keys(all_prices[n])
    link_input.send_keys(all_links[n])

    # Click Submit
    submit_button.click()

    # Small pause before loading the next form so Google doesn't block you
    time.sleep(1)

print("Project Complete! Check your Google Form Responses.")
driver.quit()