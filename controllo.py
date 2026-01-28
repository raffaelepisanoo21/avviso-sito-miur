import requests
import hashlib
import os

URL = "https://www.istruzione.it/manutenzione/index.html"
HASH_FILE = "hash.txt"

BOT_TOKEN = "8269210005:AAGBq0UmOzZA2jhrno
—NtTXdY5wQHdXXJS4"
CHAT_ID = "1470726827"

def get_page_hash():
    r = requests.get(URL, timeout=15)
    r.raise_for_status()
    return hashlib.sha256(r.text.encode()).hexdigest()

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

def main():
    new_hash = get_page_hash()

    if not os.path.exists(HASH_FILE):
        with open(HASH_FILE, "w") as f:
            f.write(new_hash)
        return

    with open(HASH_FILE, "r") as f:
        old_hash = f.read()

    if new_hash != old_hash:
        send_telegram_message("🔔 Il sito MIUR è stato aggiornato!")
        with open(HASH_FILE, "w") as f:
            f.write(new_hash)

if __name__ == "__main__":
    main()

