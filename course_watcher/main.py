
import sys
from .auth import save_cookies
from .watcher import watch_course
from .notifier import send_telegram_message

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "test-telegram":
        send_telegram_message("✅ Telegram notifications working!")
        return

    if len(sys.argv) > 1 and sys.argv[1] == "login":
        save_cookies()
    else:
        watch_course()

if __name__ == "__main__":
    main()
