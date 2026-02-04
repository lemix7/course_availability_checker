# 🎓 Course Watcher – University Registration Monitor

A Python automation tool that monitors your university course registration system and **notifies you on Telegram** when a specific course becomes available (quota > 0).

This project uses **Selenium** to interact with the university website, detects when disabled courses become selectable, and sends real‑time notifications so you can act fast.

---

## ✨ Features

* 🔐 Automated login (username + password)
* 🍪 Session persistence using cookies (no repeated logins)
* 👀 Monitors elective course availability
* 🚨 Instant Telegram notifications
* 🔒 Secrets managed via `.env`
* ⚡ Built with `uv` for fast dependency management

---

## 🗂 Project Structure

```
.
├── .env                  # Environment variables (not committed)
├── .venv/                # Virtual environment (uv-managed)
├── course_watcher/       # Application source code
│   ├── __init__.py
│   ├── main.py           # Entry point
│   ├── auth.py           # Login + cookie handling
│   ├── watcher.py        # Course availability watcher
│   ├── notifier.py       # Telegram notifications
│   └── config.py         # Config & environment loading
├── cookies.pkl           # Saved login session
├── pyproject.toml        # Project metadata & dependencies
├── uv.lock               # Locked dependencies
└── README.md
```

---

## 🛠 Requirements

* Python **3.10+**
* Google Chrome (or Chromium)
* `uv` package manager

---

## 📦 Installation

### 1️⃣ Install `uv`

```bash
pip install uv
```

### 2️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd course-watcher
```

### 3️⃣ Install dependencies

```bash
uv sync
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

⚠️ **Do not wrap values in quotes**

Add `.env` to `.gitignore` to keep secrets safe.

---

## 🤖 Telegram Bot Setup

1. Open Telegram and search for **@BotFather**
2. Create a new bot using `/newbot`
3. Copy the **bot token**
4. Start a chat with your bot and press **/start**
5. Get your chat ID via **@userinfobot**

---

## 🚀 Usage

### 1️⃣ First-time login (manual CAPTCHA)

```bash
uv run python -m course_watcher.main login
```

* A browser will open
* Log in manually and solve CAPTCHA
* Cookies are saved to `cookies.pkl`

You only need to do this **once** (unless cookies expire).

---

### 2️⃣ Start watching courses

```bash
uv run python -m course_watcher.main
```

The script will:

* Load saved cookies
* Navigate to course registration page
* Monitor elective dropdowns
* Notify you when a course becomes available

---

## 📲 Telegram Notifications

When a course opens, you’ll receive a message like:

```
🎉 Course Available!
CMPE344 - Database Management Systems
Available Seats: 1
```

Make sure notifications are **enabled and unmuted** for the bot chat.

---

## 🧠 How It Works (High Level)

1. Selenium logs into the university portal
2. Session cookies are reused to avoid repeated logins
3. The course selection `<select>` element is parsed
4. Disabled options (`quota == 0`) are ignored
5. When a target course becomes enabled, Telegram alert is sent

---

## ⚠️ Notes & Limitations

* CAPTCHA must be solved **manually** during initial login
* Website structure changes may require selector updates
* Intended for **personal use only**

---

## 🛡 Security

* Credentials are **never hardcoded**
* `.env` keeps secrets out of source control
* Cookies are stored locally only

---

## 🧩 Future Improvements

* ✅ Auto‑register when course becomes available
* ⏱ Periodic scheduling (cron / systemd)
* 📊 Seat history tracking
* 🧪 Headless mode with stealth

---

## 📄 License

This project is for **educational and personal use**.
Use responsibly and in accordance with your university’s policies.

---

## ❤️ Acknowledgements

Built with:

* Python
* Selenium
* python-telegram-bot
* uv

Good luck grabbing that seat 🚀
