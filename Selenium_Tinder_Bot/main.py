from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
)
import time
import random
from datetime import datetime


FACEBOOK_EMAIL    = "your_facebook_email@gmail.com"
FACEBOOK_PASSWORD = "your_facebook_password"

TINDER_URL   = "https://tinder.com"
LIKE_RATIO   = 0.80
MAX_SWIPES   = 100
SWIPE_DELAY  = (1.2, 3.5)


def build_driver() -> webdriver.Chrome:
    opts = Options()
    opts.add_argument("--start-maximized")
    opts.add_argument("--disable-notifications")
    opts.add_argument("--disable-extensions")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--mute-audio")

    opts.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
    opts.add_experimental_option("useAutomationExtension", False)

    opts.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=opts)

    driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"},
    )

    return driver


def human_pause(lo: float = 0.5, hi: float = 1.8):
    time.sleep(random.uniform(lo, hi))


def slow_type(element, text: str):
    for ch in text:
        element.send_keys(ch)
        time.sleep(random.uniform(0.05, 0.15))


class TinderBot:
    def __init__(self):
        self.driver  = build_driver()
        self.wait    = WebDriverWait(self.driver, 15)
        self.actions = ActionChains(self.driver)
        self.likes    = 0
        self.passes   = 0
        self.errors   = 0
        self.start_ts = datetime.now()

    def log(self, msg: str):
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"[{ts}] {msg}")

    def safe_click(self, by, selector, timeout: int = 10):
        try:
            el = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, selector))
            )
            try:
                el.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", el)
            human_pause(0.4, 0.9)
            return el
        except TimeoutException:
            return None

    def open_tinder(self):
        self.log("Opening Tinder...")
        self.driver.get(TINDER_URL)
        human_pause(3.0, 5.0)
        self.log("Tinder loaded ✓")

    def navigate_to_login(self):
        self.log("Navigating to login page...")
        try:
            login_btn = self.wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//a[contains(@href,'login')] | //button[contains(text(),'Log in')] | //button[contains(text(),'Sign in')]"
                ))
            )
            login_btn.click()
            human_pause(2.0, 3.5)
            self.log("Login page reached ✓")
        except TimeoutException:
            self.log("Login button not found — Tinder may have updated its layout.")

    def login_with_facebook(self):
        self.log("Attempting Facebook login...")
        try:
            fb_btn = self.wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//button[contains(text(),'Facebook')] | //span[contains(text(),'Facebook')]/.."
                ))
            )
            fb_btn.click()
            human_pause(2.5, 4.0)

            all_windows = self.driver.window_handles
            if len(all_windows) > 1:
                self.driver.switch_to.window(all_windows[-1])
                self.log("Facebook popup opened, filling credentials...")

                email_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "email"))
                )
                email_field.clear()
                slow_type(email_field, FACEBOOK_EMAIL)
                human_pause(0.4, 0.8)

                pw_field = self.driver.find_element(By.ID, "pass")
                pw_field.clear()
                slow_type(pw_field, FACEBOOK_PASSWORD)
                human_pause(0.5, 1.0)

                pw_field.send_keys(Keys.RETURN)
                human_pause(4.0, 7.0)

                self.driver.switch_to.window(all_windows[0])
                self.log("Facebook login submitted, waiting for Tinder to load...")
                human_pause(5.0, 8.0)

                self.log("Logged in via Facebook ✓")
            else:
                self.log("No Facebook popup appeared — page may have changed.")

        except TimeoutException:
            self.log("Facebook login button not found.")

    def dismiss_all_popups(self):
        self.log("Dismissing popups and permission requests...")

        popup_selectors = [
            "//button[contains(text(),'Allow')]",
            "//button[contains(text(),'allow')]",
            "//button[contains(text(),'Not interested')]",
            "//button[contains(text(),'No Thanks')]",
            "//button[contains(text(),'No thanks')]",
            "//button[contains(text(),'Maybe Later')]",
            "//button[contains(text(),'I agree')]",
            "//button[contains(text(),'OK')]",
            "//button[contains(text(),'Got it')]",
            "//button[@aria-label='Close']",
            "//button[contains(@class,'close')]",
        ]

        dismissed = 0
        rounds     = 0

        while rounds < 5:
            found_any = False
            for xpath in popup_selectors:
                try:
                    btn = WebDriverWait(self.driver, 2).until(
                        EC.element_to_be_clickable((By.XPATH, xpath))
                    )
                    btn.click()
                    dismissed += 1
                    found_any = True
                    human_pause(0.6, 1.2)
                except (TimeoutException, ElementClickInterceptedException,
                        ElementNotInteractableException):
                    continue

            if not found_any:
                break
            rounds += 1

        self.log(f"Dismissed {dismissed} popup(s) ✓")

    def swipe_like(self):
        try:
            like_btn = self.driver.find_element(
                By.XPATH,
                "//button[@aria-label='Like'] | //button[contains(@class,'like')] | "
                "//span[contains(text(),'Like')]/.."
            )
            like_btn.click()
            self.likes += 1
            self.log(f"  👍 Like #{self.likes}")
            return True
        except (NoSuchElementException, ElementClickInterceptedException,
                StaleElementReferenceException):
            try:
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_RIGHT)
                self.likes += 1
                self.log(f"  👍 Like #{self.likes} (keyboard)")
                return True
            except Exception:
                return False

    def swipe_pass(self):
        try:
            pass_btn = self.driver.find_element(
                By.XPATH,
                "//button[@aria-label='Nope'] | //button[contains(@class,'nope')] | "
                "//span[contains(text(),'Nope')]/.."
            )
            pass_btn.click()
            self.passes += 1
            self.log(f"  👎 Pass #{self.passes}")
            return True
        except (NoSuchElementException, ElementClickInterceptedException,
                StaleElementReferenceException):
            try:
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_LEFT)
                self.passes += 1
                self.log(f"  👎 Pass #{self.passes} (keyboard)")
                return True
            except Exception:
                return False

    def handle_match_popup(self):
        try:
            close = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//button[contains(@class,'close')] | //button[@aria-label='Close'] | "
                    "//a[contains(@href,'/app/recs')]"
                ))
            )
            close.click()
            self.log("  🎉 Match popup closed")
            human_pause(0.4, 0.8)
        except TimeoutException:
            pass

    def is_out_of_likes(self) -> bool:
        try:
            body = self.driver.find_element(By.TAG_NAME, "body").text.lower()
            return any(phrase in body for phrase in [
                "out of likes", "come back later", "increase your chances",
                "you've run out", "get gold", "upgrade"
            ])
        except Exception:
            return False

    def start_swiping(self):
        self.log(f"Starting swipe loop — target: {MAX_SWIPES} swipes (like ratio: {LIKE_RATIO:.0%})")

        total = 0

        while total < MAX_SWIPES:
            if self.is_out_of_likes():
                self.log("Out of likes — Tinder limit reached. Stopping.")
                break

            self.handle_match_popup()
            self.dismiss_all_popups()

            decision = random.random()

            if decision < LIKE_RATIO:
                success = self.swipe_like()
            else:
                success = self.swipe_pass()

            if success:
                total += 1
            else:
                self.errors += 1
                self.log(f"  ⚠️  Swipe failed (attempt {self.errors}) — retrying after pause")
                human_pause(2.0, 4.0)

                if self.errors >= 5:
                    self.log("Too many consecutive errors — stopping.")
                    break

            if success:
                self.errors = 0

            delay = random.uniform(*SWIPE_DELAY)

            if total % 10 == 0 and total > 0:
                delay += random.uniform(3.0, 8.0)
                self.log(f"  [Pause] Taking a human-like break after {total} swipes...")

            time.sleep(delay)

    def print_summary(self):
        duration = datetime.now() - self.start_ts
        mins     = int(duration.total_seconds()) // 60
        secs     = int(duration.total_seconds()) % 60

        print("\n" + "=" * 55)
        print("  💘  TINDER BOT SUMMARY")
        print("=" * 55)
        print(f"  ⏱   Runtime  : {mins}m {secs}s")
        print(f"  👍  Likes    : {self.likes}")
        print(f"  👎  Passes   : {self.passes}")
        print(f"  ⚠️   Errors   : {self.errors}")
        total = self.likes + self.passes
        ratio = (self.likes / total * 100) if total > 0 else 0
        print(f"  📊  Like rate : {ratio:.1f}%")
        print("=" * 55 + "\n")

    def run(self):
        try:
            self.open_tinder()
            self.navigate_to_login()
            self.login_with_facebook()
            self.dismiss_all_popups()
            self.start_swiping()
            self.print_summary()

        except KeyboardInterrupt:
            self.log("Stopped by user.")
            self.print_summary()

        except Exception as e:
            self.log(f"Unexpected crash: {e}")
            self.print_summary()

        finally:
            time.sleep(2)
            self.driver.quit()
            self.log("Browser closed. Done 👋")


if __name__ == "__main__":
    bot = TinderBot()
    bot.run()