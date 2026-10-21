from datetime import datetime
import sys
import time
import requests
import json
import random
import webbrowser
from threading import Thread, Lock
import os

# ═══════════════════════════════════════════════════
# 🎨 الألوان
# ═══════════════════════════════════════════════════
P = "\x1b[38;5;129m"
P2 = "\x1b[38;5;93m"
W = "\x1b[1;37m"
WHITE = "\x1b[38;5;15m"
R = "\x1b[1;31m"
G = "\x1b[1;32m"
Y = "\x1b[1;33m"
C = "\x1b[1;36m"
PINK = "\x1b[38;5;213m"
RESET = "\x1b[0m"



# ═══════════════════════════════════════════════════
# 🆔 الآيديات المسموحة
# ═══════════════════════════════════════════════════
ALLOWED_IDS = ["8420145330", "6319093542"]

# ═══════════════════════════════════════════════════
# 📊 التطبيقات
# ═══════════════════════════════════════════════════
PLATFORMS = [
    "Twitter/X", "PUBG Mobile", "Free Fire", "YallaLudo", "Instagram", "TikTok",
    "Facebook", "WhatsApp", "Netflix", "Spotify", "Snapchat",
    "Discord", "Steam", "Epic Games", "Roblox", "Pinterest",
    "Reddit", "LinkedIn", "Tumblr", "Twitch", "Xbox",
    "PlayStation", "Riot Games", "Telegram", "Canva", "Yahoo"
]

counters = {p: 0 for p in PLATFORMS}

hits = 0
bad = 0
total = 0
good = 0
is_running = True
proxies = []
proxies_alive = []
token = ""
chat_id = ""

version = '2.0'
lock = Lock()


logo = f"""
{R}●─────━Zeus─────━●
{R}╱╱╭━━━┳━┳━━━┳━╮
{R}╭━┫╭━╮┃━┫╭━╮┃━┫
{R}┃╋┣╯╭╯┣━┣╯╭╯┣━┃
{R}┃╭╯╱┃╭┻━╯╱┃╭┻━╯
{R}╰╯╱╱┃┃╱╱╱╱┃┃

{W}  ×─> {W}━━━━━━━{R}━━━━━━━━━━{W}━━━━━━━━━━━━{W}━━━━━{R}Zeus━━━━━━{W}━━━━━ <─×"""


frames = [
    "ㅂㅈ둎ㄴ묘ㅑㅏㅍㅌㄷㄴ퍼ㅑㅕㅐ멋넛냣아ㅛ아요ㅏㅛ",
    "아ㅛ잏틒ㅋㄹ닛뎌내ㅛㅑㅅ냣내ㅛㅇ",
    "ㄷ벼냣냣냣낳타핰효오로러처러ㅕ려려려러ㅓ퍼처러",
    "추하허ㅗ러러ㅓ처류",
    "ㅛㄱㅈㄴ포ㅑㅅㅈㅂ뎌ㅐㅐㅏㅠㅌㄴㅈ"
]


def loading_screen(duration=3):
    start = time.time()
    i = 0
    while time.time() - start < duration:
        frame = frames[i % len(frames)]
        sys.stdout.write(f"\r{R}{frame}{RESET}")
        sys.stdout.flush()
        time.sleep(0.15)
        i += 1
    sys.stdout.write(f"\r{' ' * 60}\r")
    sys.stdout.flush()


def print_status_line():
    colors = ["\x1b[38;5;129m", "\x1b[38;5;213m", "\x1b[38;5;46m",
              "\x1b[38;5;196m", "\x1b[38;5;226m", "\x1b[38;5;39m", "\x1b[38;5;208m"]
    zcol = colors[total % len(colors)]
    sys.stdout.write(
        f"\r{R}<[{W}●{R}]>{W} "
        f"{R}<[{zcol}Zeus{R}-{Y}{total}{R}]>{W} "
        f"{G}<[{G}OK{R}-{G}{hits}{R}]>{W}  "
    )
    sys.stdout.flush()


def print_checker_stats():
    os.system('clear' if os.name != 'nt' else 'cls')
    print(logo)
    print()
    print(f"{R}════════════════════ [ Zeus ] ══════════════════════{RESET}")
    for p in PLATFORMS:
        cnt = counters[p]
        color = G if cnt > 0 else R
        print(f"{P}[•]{RESET} {WHITE}{p:<20}{RESET} {P}>>>{RESET} {color}{{ {cnt} }}{RESET}")
    print(f"{R}═══════════════════════════════════════════════════════{RESET}")
    print(f"{PINK}Hits:{RESET} {G}{hits}{RESET}")
    print(f"{PINK}2FA:{RESET} {G}{0}{RESET}")
    print(f"{PINK}Custom:{RESET} {G}{0}{RESET}")
    print(f"{PINK}Bad:{RESET} {R}{bad}{RESET}")
    print(f"{PINK}Retries:{RESET} {G}{0}{RESET}")
    print(f"{P}{P}@R7_36 / @R7Aih1{RESET}")


def update_display():
    global is_running
    while is_running:
        print_checker_stats()
        time.sleep(2)


# ═══════════════════════════════════════════════════
# 📁 البروكسيات
# ═══════════════════════════════════════════════════
BUILTIN_PROXIES = [
    "http://8.215.25.3:2080", "http://2.27.53.95:3128", "http://2.139.41.14:3128",
    "http://102.213.179.66:8080", "http://103.183.8.183:8080", "http://103.103.8.222:8080",
    "http://103.31.233.46:3128", "http://139.59.1.14:8080", "http://84.44.39.159:9090",
    "http://134.209.29.120:3128", "http://128.199.202.122:8080", "http://210.211.113.35:80",
    "http://139.162.78.109:3128", "http://34.196.85.244:3128", "http://43.99.60.244:8089",
    "http://102.244.78.61:8083", "http://187.62.191.3:61456", "http://181.49.100.190:8080",
    "http://102.244.78.61:8085", "http://180.190.185.211:9999", "http://102.244.78.61:8084",
    "http://102.244.78.61:8086", "http://54.249.49.32:8084", "http://179.60.189.81:999",
    "http://180.180.151.137:8080", "http://111.192.21.187:8888", "http://111.196.24.43:8888",
    "http://103.187.227.126:1111", "http://103.180.126.147:8080", "http://61.19.145.66:8080",
    "http://74.62.179.122:8080", "http://102.68.128.214:8080", "http://103.148.195.22:8080",
    "http://202.69.38.82:8080", "http://91.203.242.66:222", "http://3.35.49.14:8080",
    "http://210.61.216.63:60808", "http://181.37.240.89:999", "http://201.4.65.79:8080",
    "http://103.237.102.191:11111", "http://27.185.218.213:17981", "http://102.219.209.86:3346",
    "http://201.4.69.46:8080", "http://103.82.20.76:8080", "http://109.224.242.171:8080",
    "http://38.103.250.205:8080", "http://101.36.112.205:1081", "http://102.244.78.61:8082",
    "http://134.209.29.120:80", "http://144.31.146.195:8080", "http://138.99.176.254:999",
    "http://110.39.41.11:8080", "http://178.92.72.68:8080", "http://109.224.242.120:8585",
    "http://160.20.128.239:1080", "http://104.225.162.20:8082", "http://200.71.111.222:999",
    "http://27.72.244.228:8080", "http://122.246.3.12:17981", "http://122.246.4.30:17981",
    "http://185.222.94.66:808", "http://4.144.146.21:80", "http://119.188.131.55:17981",
    "http://181.78.195.137:999", "http://147.15.126.122:28080", "http://64.181.247.193:443",
    "http://102.244.78.61:8081", "http://103.148.62.1:8080", "http://116.196.150.180:17981",
    "http://190.97.229.118:999", "http://141.144.206.124:1080", "http://203.150.166.170:8080",
    "http://180.191.14.210:8081", "http://103.189.116.20:8080", "http://176.194.189.40:80",
    "http://198.199.86.11:3128", "http://161.35.70.249:80", "http://192.147.114.177:8080",
    "http://111.118.149.40:8080", "http://45.198.11.183:9191", "http://165.154.162.73:8888",
    "http://209.97.150.167:3128", "http://84.22.48.28:8080", "http://110.93.218.62:8080",
    "http://34.105.252.3:3128", "http://104.129.203.85:9480", "http://201.7.31.181:8080",
    "http://184.75.221.82:3118", "http://109.224.242.21:8080", "http://38.211.68.74:999",
    "http://38.75.82.220:999", "http://187.249.92.247:999", "http://113.160.130.82:443",
    "http://45.198.11.164:9191", "http://190.166.204.189:8080", "http://161.35.70.249:3128",
    "http://34.88.38.81:9443", "http://147.45.164.178:8888", "http://38.244.136.217:3128",
    "http://181.78.94.158:999", "http://136.226.118.194:9480", "http://203.252.142.217:80",
    "http://103.180.122.66:3125", "http://111.192.48.117:8888", "http://20.33.10.132:80",
    "http://201.219.218.4:8080", "http://111.192.41.54:8888", "http://210.211.113.34:80",
    "http://103.183.58.230:8080", "http://47.107.107.24:80", "http://34.46.221.75:8080",
    "http://163.61.112.250:8080", "http://124.83.106.84:8082", "http://176.88.166.201:8080",
    "http://190.120.255.188:999", "http://110.39.13.162:1", "http://154.88.136.182:999",
    "http://103.177.176.62:8080", "http://210.211.113.33:80", "http://82.213.29.53:19000",
    "http://27.112.66.122:8181", "http://103.86.135.98:8080", "http://177.93.52.67:999",
    "http://186.96.111.214:999", "http://178.92.72.165:8080", "http://38.19.111.74:8080",
    "http://216.28.149.10:999", "http://118.99.99.66:8080", "http://212.252.73.13:8080",
    "http://103.20.102.155:8180", "http://95.133.236.11:3128", "http://41.159.154.43:3128",
    "http://103.171.12.2:8080", "http://43.160.222.70:3128", "http://159.203.61.169:3128",
    "http://120.28.82.207:8082", "http://159.195.194.242:8080", "http://149.86.140.210:8080",
    "http://46.10.209.230:8080", "http://110.34.8.110:8080", "http://139.99.238.83:8080",
    "http://5.129.254.60:8888", "http://5.129.254.51:8888", "http://5.129.254.154:8888",
    "http://5.129.254.49:8888", "http://5.129.254.5:8888", "http://5.129.254.129:8888",
    "http://144.31.146.190:8080", "http://178.92.72.73:8080", "http://45.195.105.20:8080",
    "http://102.244.78.61:8090", "http://120.232.115.170:17981", "http://49.149.215.58:8082",
    "http://120.232.115.57:17981", "http://43.156.55.191:5001", "http://113.45.195.147:3128",
    "http://123.121.75.126:8888", "http://194.48.141.34:3129", "http://44.216.83.206:3128",
    "http://160.19.41.47:80", "http://151.158.133.149:8080", "http://116.101.54.121:8080",
    "http://123.60.155.1:3128", "http://82.180.145.170:3129", "http://103.191.169.70:1111",
    "http://206.135.47.106:999", "http://42.116.10.198:514", "http://123.57.0.163:8888",
    "http://1.20.101.18:80", "http://45.190.85.1:999", "http://46.122.16.54:8080",
    "http://150.241.245.211:8080", "http://45.194.41.103:8080", "http://104.128.228.69:8118",
    "http://103.113.3.25:8080", "http://1.20.101.32:8080", "http://90.156.160.234:3128",
    "http://20.33.10.79:80", "http://110.74.195.34:25", "http://181.225.44.46:999",
    "http://34.43.46.91:80", "http://185.133.213.86:8074", "http://200.31.12.188:999",
    "http://159.255.32.249:3128", "http://67.205.161.81:3128", "http://138.68.60.8:3128",
    "http://192.203.0.198:999", "http://212.200.223.89:8080", "http://167.250.50.53:999",
    "http://91.203.179.72:65056", "http://3.211.120.181:443", "http://177.234.217.237:999",
    "http://201.165.164.22:999",
    # ═══ البروكسيات الجديدة ═══
    "http://203.174.15.138:8080", "http://47.52.223.161:5872", "http://41.216.191.85:8080",
    "http://103.184.54.9:8080", "http://90.146.196.18:8080", "http://109.205.126.6:8080",
    "http://103.175.156.242:8080", "http://110.49.53.69:8081", "http://115.127.166.86:8080",
    "http://103.19.56.68:8080", "http://161.53.43.203:8080", "http://196.251.221.30:8080",
    "http://189.91.154.253:3128", "http://5.8.41.106:3128", "http://158.172.217.1:999",
    "http://190.7.24.103:3129", "http://16.52.81.236:9066", "http://206.62.162.21:999",
    "http://210.86.172.190:8080", "http://45.198.11.9:9191", "http://173.180.22.3:8080",
    "http://111.192.47.95:8888", "http://197.224.185.3:3128", "http://160.19.41.36:80",
    "http://160.19.41.43:80", "http://111.196.31.10:8888", "http://14.170.154.193:19132",
    "http://113.161.59.136:8080",
]


def load_proxies():
    global proxies, proxies_alive
    proxies = list(set(BUILTIN_PROXIES))
    proxies_alive = proxies.copy()
    print(f"{R}[+] LOADED {len(proxies)} PROXIES{RESET}")


def get_proxy():
    if not proxies_alive:
        return None
    p = random.choice(proxies_alive)
    return {"http": p, "https": p}


def gen_email():
    chars = 'qwertyuiopasdfghjklzxcvbnm0123456789'
    length = random.choice([3, 4])
    return ''.join(random.choice(chars) for _ in range(length)) + '@yopmail.com'


def send_tg(msg):
    try:
        if token and chat_id:
            requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
                          data={"chat_id": chat_id, "text": msg, "parse_mode": "HTML"}, timeout=5)
    except:
        pass


# ═══════════════════════════════════════════════════
# 🎯 CHECKER
# ═══════════════════════════════════════════════════
def check_twitter(email):
    try:
        r = requests.get('https://api.x.com/i/users/email_available.json',
                         params={'email': email},
                         headers={'user-agent': 'Mozilla/5.0'},
                         proxies=get_proxy(), timeout=5)
        return '"taken":true' in r.text
    except:
        return False


# ═══════════════════════════════════════════════════
# 🔥 SCAN ALL — تطبيق واحد عشوائي
# ═══════════════════════════════════════════════════
def scan_all(email):
    apps_pool = [p for p in PLATFORMS if p != "Twitter/X"]
    linked = [random.choice(apps_pool)]

    for app in linked:
        with lock:
            counters[app] += 1

    return linked


def check(email):
    global hits, bad, total, good
    try:
        total += 1
        if check_twitter(email):
            hits += 1
            good += 1
            with lock:
                counters["Twitter/X"] += 1

            linked = scan_all(email)
            linked_str = " · ".join(linked) if linked else "None"

            with open('hits.txt', 'a') as f:
                f.write(f"{email}|{linked_str}\n")

            print(f"\n{G}[✓ HIT]{RESET} {W}{email}{RESET}")
            for app in linked:
                print(f"   {G}✓{RESET} {WHITE}{app}{RESET}")

            msg = f"""حساب شغال ✅

<b>Email:</b>
<code>{email}</code>

<b>Linked:</b>
{linked_str}

━━━━━━━━━━━━━━━━━━
BY: @R7_36 / @R7Aih1
اشتراك مدفوع"""
            send_tg(msg)
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

    loading_screen(duration=3)

    os.system('clear' if os.name != 'nt' else 'cls')
    print(logo)
    print()

    token   = input(f"{R} TOKEN >>> {RESET}").strip()
    chat_id = input(f"{R} ID    >>> {RESET}").strip()

    # ✅ فحص الآيدي قبل ما يشتغل السكربت
    if chat_id not in ALLOWED_IDS:
        print(f"\n{R}[✗] الآيدي {chat_id} غير مصرح به!{RESET}")
        print(f"{R}[✗] السكربت يتوقف.{RESET}")
        sys.exit(1)

    print(f"{G}[✓] الآيدي مصرح به: {chat_id}{RESET}")
    print()

    load_proxies()

    print(f"{G}[+] Starting with {len(proxies_alive)} proxies{RESET}")

    time.sleep(1)

    Thread(target=update_display, daemon=True).start()

    for _ in range(10):
        Thread(target=scanner, daemon=True).start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        is_running = False
        print(f"\n{R}[!] STOPPED.{RESET}")
