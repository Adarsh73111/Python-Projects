from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
)
from datetime import datetime
import time
import random


BASE_URL   = "https://appbrewery.github.io/gym"
LOGIN_URL  = f"{BASE_URL}/login/"
BOOK_URL   = f"{BASE_URL}/classes/"
MY_BOOK_URL = f"{BASE_URL}/my-bookings/"

EMAIL    = "angela@appbrewery.com"
PASSWORD = "testing1234"

TARGET_DAYS = ["Tuesday", "Thursday"]

MAX_RETRIES      = 3
SHORT_WAIT       = 3
LONG_WAIT        = 10
PAGE_LOAD_WAIT   = 15


def build_driver() -> webdriver.Chrome:
    opts = Options()
    opts.add_argument("--start-maximized")
    opts.add_argument("--mute-audio")
    opts.add_argument("--disable-extensions")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_experimental_option("excludeSwitches", ["enable-logging"])
    return webdriver.Chrome(options=opts)


def human_pause(lo: float = 0.4, hi: float = 1.1):
    time.sleep(random.uniform(lo, hi))


def slow_type(element, text: str):
    for ch in text:
        element.send_keys(ch)
        time.sleep(random.uniform(0.04, 0.12))


class GymBot:
    def __init__(self):
        self.driver  = build_driver()
        self.wait    = WebDriverWait(self.driver, PAGE_LOAD_WAIT)
        self.booked  = 0
        self.skipped = 0
        self.failed  = 0
        self.log_lines = []

    def log(self, msg: str):
        ts  = datetime.now().strftime("%H:%M:%S")
        out = f"[{ts}] {msg}"
        print(out)
        self.log_lines.append(out)

    def get(self, url: str):
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                self.driver.get(url)
                human_pause(1.5, 2.5)
                return
            except Exception as e:
                self.log(f"Navigation attempt {attempt} failed: {e}")
                if attempt == MAX_RETRIES:
                    raise
                time.sleep(SHORT_WAIT)

    def find(self, by, selector, timeout: int = PAGE_LOAD_WAIT):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, selector))
        )

    def click(self, by, selector, timeout: int = PAGE_LOAD_WAIT):
        el = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, selector))
        )
        try:
            el.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", el)
        human_pause()
        return el

    def login(self):
        self.log("Navigating to login page...")
        self.get(LOGIN_URL)

        try:
            email_field = self.find(By.ID, "email")
            email_field.clear()
            slow_type(email_field, EMAIL)
            human_pause(0.3, 0.7)

            pw_field = self.find(By.ID, "password")
            pw_field.clear()
            slow_type(pw_field, PASSWORD)
            human_pause(0.5, 1.0)

            self.click(By.CSS_SELECTOR, "button[type='submit']")

            self.wait.until(EC.url_contains("/gym"))
            self.log("Login successful ✓")
            return True

        except TimeoutException:
            self.log("Login failed — check credentials or page structure.")
            return False

    def is_already_booked(self, row) -> bool:
        try:
            btn = row.find_element(By.CSS_SELECTOR, "button, a.book-btn, input[type='submit']")
            btn_text = btn.text.strip().lower()
            classes  = btn.get_attribute("class") or ""
            return (
                "booked" in btn_text
                or "cancel" in btn_text
                or "booked" in classes.lower()
                or btn.get_attribute("disabled") is not None
            )
        except NoSuchElementException:
            return False

    def book_class(self, row, day: str, class_name: str) -> str:
        try:
            if self.is_already_booked(row):
                self.log(f"  [{day}] '{class_name}' already booked — skipping.")
                self.skipped += 1
                return "already_booked"

            btn = row.find_element(By.CSS_SELECTOR, "button, a.book-btn, input[type='submit']")
            human_pause(0.3, 0.8)

            try:
                btn.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", btn)

            human_pause(0.8, 1.5)

            try:
                confirm = WebDriverWait(self.driver, 4).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".confirm-btn, button.confirm, #confirm"))
                )
                confirm.click()
                human_pause(0.5, 1.0)
            except TimeoutException:
                pass

            self.booked += 1
            self.log(f"  [{day}] Booked '{class_name}' ✓")
            return "booked"

        except (NoSuchElementException, StaleElementReferenceException) as e:
            self.failed += 1
            self.log(f"  [{day}] Could not book '{class_name}': {e}")
            return "failed"

    def book_target_days(self):
        self.log(f"Loading classes page...")
        self.get(BOOK_URL)

        try:
            self.find(By.CSS_SELECTOR, "table, .classes-table, .schedule")
        except TimeoutException:
            self.log("Classes table not found on page.")
            return

        for day in TARGET_DAYS:
            self.log(f"Looking for {day} classes...")

            try:
                rows = self.driver.find_elements(By.CSS_SELECTOR, "tr, .class-row, .schedule-row")
                day_rows = []

                for row in rows:
                    try:
                        row_text = row.text
                        if day.lower() in row_text.lower():
                            day_rows.append(row)
                    except StaleElementReferenceException:
                        continue

                if not day_rows:
                    self.log(f"  No classes found for {day}.")
                    continue

                self.log(f"  Found {len(day_rows)} class(es) on {day}.")

                for row in day_rows:
                    try:
                        cells = row.find_elements(By.TAG_NAME, "td")
                        class_name = cells[1].text.strip() if len(cells) > 1 else "Unknown"
                        self.book_class(row, day, class_name)
                        human_pause(0.5, 1.2)
                    except (StaleElementReferenceException, IndexError):
                        continue

            except Exception as e:
                self.log(f"  Error processing {day}: {e}")

    def verify_bookings(self):
        self.log("Verifying bookings on 'My Bookings' page...")
        self.get(MY_BOOK_URL)

        try:
            self.find(By.CSS_SELECTOR, "table, .bookings-table, .my-bookings, main")
            page_text = self.driver.find_element(By.TAG_NAME, "body").text

            confirmed = []
            for day in TARGET_DAYS:
                if day.lower() in page_text.lower():
                    confirmed.append(day)
                    self.log(f"  Confirmed booking visible for {day} ✓")
                else:
                    self.log(f"  No booking found for {day} on My Bookings page.")

            return confirmed

        except TimeoutException:
            self.log("Could not load My Bookings page.")
            return []

    def time_travel_qa(self):
        self.log("Running Time Travel QA check...")

        qa_urls = [
            f"{BASE_URL}/classes/?day=Tuesday",
            f"{BASE_URL}/classes/?day=Thursday",
            f"{BASE_URL}/classes/?week=next",
        ]

        for url in qa_urls:
            try:
                self.get(url)
                body = self.driver.find_element(By.TAG_NAME, "body").text
                if "error" in body.lower() or "404" in body.lower():
                    self.log(f"  QA Warning — possible issue at: {url}")
                else:
                    self.log(f"  QA OK: {url} ✓")
            except Exception as e:
                self.log(f"  QA check skipped for {url}: {e}")

    def print_summary(self):
        print("\n" + "=" * 55)
        print("  📋  BOOKING SUMMARY")
        print("=" * 55)
        print(f"  ✅  Successfully booked : {self.booked}")
        print(f"  ⏭️   Already booked      : {self.skipped}")
        print(f"  ❌  Failed              : {self.failed}")
        print(f"  🎯  Target days         : {', '.join(TARGET_DAYS)}")
        print("=" * 55 + "\n")

    def run(self):
        try:
            self.log("=== Gym Booking Bot Started ===")

            if not self.login():
                self.log("Exiting — login failed.")
                return

            self.book_target_days()
            self.verify_bookings()
            self.time_travel_qa()
            self.print_summary()

        except KeyboardInterrupt:
            self.log("Stopped by user.")
            self.print_summary()

        except Exception as e:
            self.log(f"Unexpected error: {e}")
            self.print_summary()

        finally:
            time.sleep(2)
            self.driver.quit()
            self.log("Browser closed. Done!")


if __name__ == "__main__":
    bot = GymBot()
    bot.run()