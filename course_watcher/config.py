from dotenv import load_dotenv
import os 


LOGIN_URL = "https://sis.ciu.edu.tr/users/login"
COURSE_PAGE_URL = "https://sis.ciu.edu.tr/student/course/registration"

COURSE_CODE = "CMPE485"
CHECK_INTERVAL = 120  # seconds

COOKIES_FILE = "cookies.pkl"

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")