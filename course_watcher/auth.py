

import pickle
from .config import LOGIN_URL, COOKIES_FILE
from .browser import create_driver

def save_cookies():
    driver = create_driver()
    driver.get(LOGIN_URL)

    print("🔐 Log in manually and solve CAPTCHA.")
    print("➡️ Navigate to the course page.")
    input("Press ENTER once logged in...")

    with open(COOKIES_FILE, "wb") as f:
        pickle.dump(driver.get_cookies(), f)

    print("✅ Cookies saved.")
    driver.quit()
