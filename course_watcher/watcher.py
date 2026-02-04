

import time
import pickle
from selenium.webdriver.common.by import By
from .config import LOGIN_URL, COURSE_PAGE_URL, COURSE_CODE, CHECK_INTERVAL, COOKIES_FILE
from .notifier import send_telegram_message

from .browser import create_driver


def load_cookies(driver):
    with open(COOKIES_FILE, "rb") as f:
        cookies = pickle.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)


def is_course_available(driver) -> bool:
    options = driver.find_elements(By.TAG_NAME, "option")

    for opt in options:
        text = opt.text.strip()

        if COURSE_CODE in text:
            disabled = opt.get_attribute("disabled")

            if disabled is None:
                print(f"✅ {COURSE_CODE} AVAILABLE → {text}")
                return True
            else:
                print(f"❌ {COURSE_CODE} FULL → {text}")
                return False

    print(f"⚠️ Course {COURSE_CODE} not found")
    return False


def watch_course():
    driver = create_driver()

    # Open base domain FIRST
    driver.get(LOGIN_URL)

    # 2️ Load cookies
    load_cookies(driver)


    driver.refresh()
    time.sleep(3)

    # go to course registration page
    driver.get(COURSE_PAGE_URL)
    time.sleep(5)

    print(f"👀 Watching course: {COURSE_CODE}")

    while True:
        driver.refresh()
        time.sleep(5)

        if is_course_available(driver):
            msg = f"🎉 COURSE AVAILABLE!\n\n{COURSE_CODE} is now open for registration."
            print(msg)
            send_telegram_message(msg)
            break
        else:
            print("⏳ Still unavailable...")

        time.sleep(CHECK_INTERVAL)

    driver.quit()
