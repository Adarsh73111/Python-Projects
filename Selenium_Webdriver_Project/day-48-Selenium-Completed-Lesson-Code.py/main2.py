from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    TimeoutException
)
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--mute-audio")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=chrome_options)

# ── Use the ORIGINAL Cookie Clicker — no Cloudflare! ──
print("[Setup] Opening Cookie Clicker (original version)...")
driver.get("https://orteil.dashnet.org/experiments/cookie/")
time.sleep(3)
print("[Setup] Page opened ✓")


print("[Setup] Waiting for game to load...")

try:
    big_cookie = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "cookie"))
    )
    print("[Setup] Big cookie found — let's gooo 🍪\n")
except TimeoutException:
    print("[ERROR] Game didn't load. Check your internet and try again.")
    driver.quit()
    exit()


def parse_number(text: str) -> int:
    try:
        return int(text.strip().replace(",", ""))
    except ValueError:
        return 0

def get_current_cookies() -> int:
    try:
        raw = driver.find_element(By.ID, "cookies").text
        number_part = raw.split(" ")[0]
        return parse_number(number_part)
    except Exception:
        return 0

def buy_best_item():
    try:
        current_cookies = get_current_cookies()
        store_items = driver.find_elements(By.CSS_SELECTOR, "#store div")

        best_item  = None
        best_price = 0

        for item in store_items:
            try:
                item_text = item.get_attribute("title")
                if not item_text:
                    continue

                if "costs" in item_text:
                    price_str = item_text.split("costs ")[-1].strip()
                    price = parse_number(price_str)

                    if price <= current_cookies and price > best_price:
                        best_item  = item
                        best_price = price

            except (StaleElementReferenceException, NoSuchElementException):
                continue

        if best_item is not None:
            best_item.click()
            print(f"  [Store] Bought item for {best_price:,} cookies 🏠")

    except Exception:
        pass


def print_stats(elapsed: int, total_clicks: int):
    cookies = get_current_cookies()
    mins = elapsed // 60
    secs = elapsed % 60
    print(
        f"\n{'='*50}\n"
        f"  ⏱  Runtime     : {mins}m {secs}s\n"
        f"  🖱  Total clicks : {total_clicks:,}\n"
        f"  🍪  Cookie count : {cookies:,}\n"
        f"{'='*50}\n"
    )


print("🤖  Bot is running! Press Ctrl+C to stop.\n")

total_clicks      = 0
start_time        = time.time()
last_store_check  = start_time
last_stats_time   = start_time

STORE_INTERVAL = 5
STATS_INTERVAL = 30

try:
    while True:
        try:
            big_cookie.click()
            total_clicks += 1
        except StaleElementReferenceException:
            big_cookie = driver.find_element(By.ID, "cookie")
        except Exception:
            pass

        now = time.time()

        if now - last_store_check >= STORE_INTERVAL:
            buy_best_item()
            last_store_check = now

        if now - last_stats_time >= STATS_INTERVAL:
            print_stats(int(now - start_time), total_clicks)
            last_stats_time = now

except KeyboardInterrupt:
    elapsed = int(time.time() - start_time)
    print("\n\n[Bot stopped by user]")
    print_stats(elapsed, total_clicks)
    print("Closing browser... bye! 👋")
    driver.quit()