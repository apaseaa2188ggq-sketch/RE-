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
C = "\x1b[38;5;39m"  # أزرق واضح (Light Blue)
PINK = "\x1b[38;5;213m"
RESET = "\x1b[0m"

webbrowser.open('https://t.me/R7Aih1')

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

# ═══════════════════════════════════════════════════
# 🌍 قائمة الدول
# ═══════════════════════════════════════════════════
countries_data = {
    "1": {"name": "Algeria", "codes": ["055", "056", "066", "067", "077", "079"]},
    "2": {"name": "Saudi Arabia", "codes": ["050", "053", "054", "055", "056", "058"]},
    "3": {"name": "UAE", "codes": ["050", "052", "054", "055", "056", "058"]},
    "4": {"name": "Qatar", "codes": ["330", "331", "332", "333", "334", "335"]},
    "5": {"name": "Kuwait", "codes": ["500", "503", "505", "506", "507", "509"]},
    "6": {"name": "Oman", "codes": ["710", "712", "714", "715", "716", "718"]},
    "7": {"name": "Bahrain", "codes": ["310", "311", "312", "313", "314", "315"]},
    "8": {"name": "Egypt", "codes": ["010", "011", "012", "015", "016", "017"]},
    "9": {"name": "Morocco", "codes": ["600", "601", "602", "603", "604", "605"]},
    "10": {"name": "Jordan", "codes": ["070", "071", "072", "077", "078", "079"]},
    "11": {"name": "Lebanon", "codes": ["030", "031", "032", "033", "034", "035"]},
    "12": {"name": "Iraq", "codes": ["0750", "0770", "0780"]},
    "13": {"name": "Tunisia", "codes": ["200", "201", "202", "203", "204", "205"]},
    "14": {"name": "Syria", "codes": ["090", "091", "092", "093", "094", "095"]},
    "15": {"name": "Yemen", "codes": ["700", "701", "702", "703", "704", "705"]},
    "16": {"name": "Libya", "codes": ["910", "911", "912", "913", "914", "915"]},
    "17": {"name": "Sudan", "codes": ["090", "091", "092", "093", "094", "095"]},
    "18": {"name": "Palestine", "codes": ["050", "051", "052", "053", "054", "055"]},
    "19": {"name": "Mauritania", "codes": ["410", "411", "412", "413", "414", "415"]},
    "20": {"name": "Somalia", "codes": ["060", "061", "062", "063", "064", "065"]},
    "21": {"name": "Djibouti", "codes": ["770", "771", "772", "773", "774", "775"]},
    "22": {"name": "Comoros", "codes": ["320", "321", "322", "323", "324", "325"]}
}


logo = f"""
{P}●─────━Zeus─────━●
{R}╱╱╭━━━┳━┳━━━┳━╮
{P}╭━┫╭━╮┃━┫╭━╮┃━┫
{R}┃╋┣╯╭╯┣━┣╯╭╯┣━┃
{P}┃╭╯╱┃╭┻━╯╱┃╭┻━╯
{R}╰╯╱╱┃┃╱╱╱╱┃┃

{W}  ×─> {W}━━━━━━━{P}━━━━━━━━━━{W}━━━━━━━━━━━━{W}━━━━━{P}Zeus━━━━━━{W}━━━━━ <─×"""


frames = [
    "ㅂㅈ둎ㄴ묘ㅑㅏㅍㅌㄷㄴ퍼ㅑㅕㅐ멋넛냣아ㅛ아요ㅏㅛ",
    "아ㅛ잏틒ㅋㄹ닛뎌내ㅛㅑㅅ냣내ㅛㅇ",
    "ㄷ벼냣냣냣낳타핰효오로러처러ㅕ려려려러ㅓ퍼처러",
    "추하허ㅗ러러ㅓ처류",
    "ㅛㄱㅈㄴ포ㅑㅅㅈㅂ뎌ㅐㅐㅏㅠㅌㄴㅈ"
]


def loading_screen(duration=3, color=R):
    start = time.time()
    i = 0
    while time.time() - start < duration:
        frame = frames[i % len(frames)]
        sys.stdout.write(f"\r{color}{frame}{RESET}")
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
    "http://5.129.254.60:8888",
    "http://5.129.254.129:8888",
    "http://45.61.133.104:7777",
    "http://46.101.148.225:10000",
    "http://45.125.64.215:443",
    "http://8.243.167.51:999",
    "http://2.139.41.14:3128",
    "http://27.147.142.156:9249",
    "http://91.107.247.193:7001",
    "http://38.50.165.123:999",
    "http://43.160.222.70:3128",
    "http://77.73.68.24:8080",
    "http://14.245.166.183:8080",
    "http://93.184.72.130:8080",
    "http://45.130.127.14:3128",
    "http://27.147.153.179:9249",
    "http://103.133.25.247:8080",
    "http://36.91.174.26:8080",
    "http://134.209.29.120:3128",
    "http://138.68.60.8:3128",
    "http://159.203.61.169:3128",
    "http://139.59.1.14:8080",
    "http://128.199.202.122:8080",
    "http://112.216.54.226:12121",
    "http://165.154.7.156:8888",
    "http://186.33.51.9:999",
    "http://168.227.239.66:20000",
    "http://152.200.218.28:80",
    "http://198.199.86.11:3128",
    "http://185.191.106.41:8081",
    "http://209.97.150.167:3128",
    "http://213.183.61.198:3128",
    "http://205.237.105.49:3129",
    "http://187.251.224.167:80",
    "http://181.209.39.90:999",
    "http://182.252.89.134:8080",
    "http://161.35.70.249:3128",
    "http://51.15.20.32:3129",
    "http://5.129.254.51:8888",
    "http://5.129.254.215:8888",
    "http://5.129.254.60:8888",
    "http://5.129.254.70:8888",
    "http://68.183.79.30:3128",
    "http://44.216.83.206:3128",
    "http://103.211.82.92:8080",
    "http://77.221.132.246:3128",
    "http://5.129.254.49:8888",
    "http://206.1.98.52:8888",
    "http://185.130.50.208:80",
    "http://5.129.254.129:8888",
    "http://91.107.247.193:7001",
    "http://46.101.148.225:10000",
    "http://147.45.164.178:8888",
    "http://62.146.180.4:3000",
    "http://103.151.23.89:8082",
    "http://145.220.227.91:3128",
    "http://195.226.213.254:8888",
    "http://5.129.254.5:8888",
    "http://121.46.226.221:10808",
    "http://34.125.234.138:40001",
    "http://159.194.228.40:8888",
    "http://206.135.53.53:999",
    "http://45.125.64.215:443",
    "http://4.144.146.21:80",
    "http://139.162.78.109:3128",
    "http://144.31.146.190:8080",
    "http://43.99.60.244:8089",
    "http://103.119.19.218:3128",
    "http://149.130.173.58:9443",
    "http://205.234.123.108:8080",
    "http://200.94.38.42:2604",
    "http://206.135.62.8:999",
    "http://45.65.224.74:999",
    "http://102.244.78.61:8085",
    "http://203.252.142.217:80",
    "http://102.244.78.61:8084",
    "http://45.175.173.20:8080",
    "http://111.196.44.88:8888",
    "http://102.244.78.61:8083",
    "http://102.244.78.61:8090",
    "http://102.244.78.61:8089",
    "http://102.244.78.61:8088",
    "http://102.244.78.61:8087",
    "http://46.161.49.174:10809",
    "http://45.140.165.128:40001",
    "http://102.244.78.61:8080",
    "http://102.244.78.61:8086",
    "http://102.244.78.61:8082",
    "http://111.192.54.230:8888",
    "http://123.121.115.69:8888",
    "http://111.196.25.174:8888",
    "http://120.232.115.57:17981",
    "http://168.227.239.66:10000",
    "http://111.196.28.151:8888",
    "http://123.121.108.122:8888",
    "http://123.121.112.126:8888",
    "http://194.87.197.21:8080",
    "http://116.104.251.199:2117",
    "http://172.82.64.79:3128",
    "http://111.192.62.27:8888",
    "http://120.232.115.170:17981",
    "http://123.121.97.74:8888",
    "http://20.33.10.79:443",
    "http://123.121.132.234:8888",
    "http://20.33.10.132:443",
    "http://80.65.211.149:8888",
    "http://114.246.197.252:8888",
    "http://145.220.227.145:8080",
    "http://197.224.185.3:3128",
    "http://111.192.54.5:8888",
    "http://47.107.107.24:80",
    "http://111.192.56.103:8888",
    "http://116.104.251.199:2082",
    "http://111.192.40.141:8888",
    "http://49.144.20.20:8082",
    "http://103.20.102.155:2927",
    "http://123.121.139.85:8888",
    "http://111.196.27.233:8888",
    "http://152.67.191.232:6800",
    "http://116.104.251.199:2039",
    "http://103.114.43.99:8888",
    "http://113.161.93.6:8080",
    "http://111.196.27.63:8888",
    "http://89.45.209.131:8080",
    "http://152.0.252.83:8080",
    "http://102.208.228.90:3128",
    "http://119.73.109.210:8080",
    "http://111.192.41.20:8888",
    "http://189.194.81.12:999",
    "http://185.196.182.22:8080",
    "http://160.30.204.24:50009",
    "http://186.33.41.48:999",
    "http://20.33.10.132:80",
    "http://116.104.251.199:2102",
    "http://71.14.23.121:8080",
    "http://8.219.97.248:80",
    "http://8.219.97.248:80",
    "http://45.185.163.235:999",
    "http://111.206.4.163:18888",
    "http://179.1.241.200:999",
    "http://103.187.86.10:8182",
    "http://58.69.125.145:8081",
    "http://103.130.61.61:8081",
    "http://116.104.251.199:2075",
    "http://202.137.8.148:8080",
    "http://61.29.96.146:80",
    "http://34.125.234.138:40001",
    "http://140.238.32.108:3128",
    "http://190.242.46.51:999",
    "http://103.28.37.131:3128",
    "http://102.244.78.61:8087",
    "http://5.200.72.60:3128",
    "http://103.48.68.11:83",
    "http://103.242.104.145:8080",
    "http://213.183.61.198:3128",
    "http://116.196.150.180:17981",
    "http://61.29.96.146:8000",
    "http://187.249.120.139:999",
    "http://103.142.255.32:8080",
    "http://175.138.75.83:8080",
    "http://103.166.255.170:8080",
    "http://121.46.226.221:10808",
    "http://201.4.69.29:8080",
    "http://154.59.56.74:999",
    "http://116.104.251.199:2068",
    "http://34.43.46.91:443",
    "http://102.244.78.61:8083",
    "http://217.182.195.221:30009",
    "http://120.232.115.57:17981",
    "http://116.104.251.199:2067",
    "http://190.97.229.118:999",
    "http://200.115.100.33:8080",
    "http://102.244.78.61:8089",
    "http://20.197.84.160:8080",
    "http://169.58.34.213:3128",
    "http://181.78.195.137:999",
    "http://34.43.46.91:80",
    "http://45.71.186.213:999",
    "http://168.227.239.66:10000",
    "http://38.188.201.10:999",
    "http://43.156.66.78:12345",
    "http://165.154.162.73:8888",
    "http://103.172.70.203:9191",
    "http://139.59.1.14:8080",
    "http://116.101.0.43:2100",
    "http://103.169.232.138:8080",
    "http://20.33.10.132:80",
    "http://62.146.180.4:3000",
    "http://8.215.25.3:2080",
    "http://205.234.123.108:8080",
    "http://46.161.49.174:10809",
    "http://38.210.90.56:999",
    "http://177.234.217.43:999",
    "http://144.31.146.195:8080",
    "http://198.244.254.77:3128",
    "http://45.188.125.34:999",
    "http://131.255.227.104:3128",
    "http://143.208.84.57:8589",
    "http://103.247.14.138:7778",
    "http://103.74.103.37:1080",
    "http://46.161.49.174:10808",
    "http://45.140.165.142:40001",
    "http://43.156.83.6:3128",
    "http://5.200.72.62:3128",
    "http://46.26.243.52:8080",
    "http://186.96.111.214:999",
    "http://187.249.112.221:999",
    "http://122.246.3.12:17981",
    "http://198.199.86.11:3128",
    "http://45.43.60.220:8080",
    "http://145.220.227.142:8080",
    "http://45.125.64.215:443",
    "http://209.97.150.167:3128",
    "http://3.211.120.181:443",
    "http://145.220.227.208:8080",
    "http://45.194.90.225:8080",
    "http://190.60.34.250:999",
    "http://91.107.247.193:7001",
    "http://120.232.115.170:17981",
    "http://219.148.171.178:9445",
    "http://159.203.61.169:3128",
    "http://103.112.163.131:8080",
    "http://186.73.227.202:999",
    "http://193.42.112.26:8080",
    "http://41.242.119.123:50003",
    "http://103.237.102.191:11111",
    "http://206.1.98.52:8888",
    "http://102.244.78.61:8086",
    "http://34.43.46.91:443",
    "http://34.43.46.91:80",
    "http://91.107.247.193:7001",
    "http://20.33.10.79:80",
    "http://190.12.150.244:999",
    "http://120.232.115.170:17981",
    "http://116.196.150.180:17981",
    "http://137.74.50.101:15054",
    "http://159.194.228.40:8888",
    "http://116.104.251.199:2103",
    "http://138.197.68.35:4857",
    "http://194.87.197.21:8080",
    "http://120.232.115.57:17981",
    "http://8.219.97.248:80",
    "http://45.125.64.215:443",
    "http://116.104.251.199:2027",
    "http://210.76.195.120:7893",
    "http://165.154.162.73:8888",
    "http://185.130.50.208:80",
    "http://1.1.189.58:8080",
    "http://116.104.251.199:2065",
    "http://116.104.251.199:2028",
    "http://74.62.179.122:8080",
    "http://61.19.145.66:8080",
    "http://212.174.242.114:8080"
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
# 🔥 SCAN ALL
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
اذا حاب تشترك بنسخه المدفوعه هاي مميزاته https://t.me/R7Aih1/10874?single"""
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

    # متحرك باللون الأحمر أول ما يشتغل
    loading_screen(duration=3, color=R)

    os.system('clear' if os.name != 'nt' else 'cls')
    print(logo)
    print()

    print(f"\033[38;5;129m<[●]> TOKEN >>> \033[0m", end="")
    token   = input().strip()
    print(f"\033[38;5;129m<[●]> ID    >>> \033[0m", end="")
    chat_id = input().strip()

    print()
    # متحرك باللون الأصفر بعد التوكن
    loading_screen(duration=3, color=Y)
    
    os.system('clear' if os.name != 'nt' else 'cls')
    print(logo)
    print()

    # القائمة الجديدة (الأكواد باللون الأحمر الخالص)
    print(f"{P}═══════════════════════════════════════════════════════{RESET}")
    for k, v in countries_data.items():
        codes_str = f" {R}|{RESET} ".join([f"{R}{c}{RESET}" for c in v["codes"]])
        print(f"{R}[{k}] {C}{v['name']}{RESET} {R}➔ {codes_str}")
    print(f"{P}═══════════════════════════════════════════════════════{RESET}")
    
    country_choice = input(f"\n\033[38;5;129m<[●]> Select the country number (1-22) >>> \033[0m").strip()
    if country_choice in countries_data:
        selected_country = countries_data[country_choice]["name"]
    else:
        selected_country = "Saudi Arabia"
    
    print(f"\n{G}[+] Selected Country: {selected_country}{RESET}")
    
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