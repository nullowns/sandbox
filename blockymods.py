import os
import platform
import random
import threading
from datetime import datetime

from colorama import init, Fore
import requests
import jwt

init()

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

clear()

RED = Fore.LIGHTRED_EX
GREEN = Fore.LIGHTGREEN_EX
RESET = Fore.RESET

version = "v𝟷.𝟷.𝟷"

commands = (
    f"\n      - {RED}bwlike{RESET}\n"
    f"      - {RED}bwsub{RESET}\n"
    f"      - {RED}like{RESET}\n\n"
    f"      - {RED}chspam{RESET}\n"
    f"      - {RED}clspam{RESET}\n"
    f"      - {RED}frspam{RESET}\n"
    f"      - {RED}ffspam{RESET}\n"
    f"      - {RED}fspam{RESET}\n\n"
    f"      - {RED}token{RESET}\n"
    f"      - {RED}details{RESET}\n"
    f"      - {RED}birthday{RESET}"
)

bot = "https://raw.githubusercontent.com/nullowns/blockymods/main/bot.txt"

print(f"{GREEN}bot checker...{RESET}")

while True:
    try:
        response = requests.get(bot)
        bot_lines = response.text.split('\n')
        break
    except requests.exceptions.ConnectionError:
        pass

clear()

print(f"""  _   _    _    ____ _  _______ ____  
 | | | |  / \  / ___| |/ / ____|  _ \ 
 | |_| | / _ \| |   | ' /|  _| | |_) |
 |  _  |/ ___ \ |___| . \| |___|  _ < 
 |_| |_/_/   \_\____|_|\_\_____|_| \_\
                                      
{RED}ＮＵＬＬ ＴＥＡＭ{RESET}
----------------
{RED}{version}{RESET}

     ʟɪsᴛ: {commands}

═══════════════════════════════════════
{RED}Telegram: @nullowns
----------------------------------------------
GitHub: https://github.com/nullowns/blockymods{RESET}
═══════════════════════════════════════""")

def region(text):
    return random.choice([part.strip() for part in text.split(',')])

def bwlike():
    while True:
        try:
            random_bot = random.choice(bot_lines)
            bot_id, bot_token = random_bot.split(':')
        except ValueError:
            continue

        try:
            url = f"http://gw.sandboxol.com/bedwar/api/v1/thumbs-up?beneficiaryId={user_id}"

            headers = {
                'Access-Token': bot_token,
                'userId': bot_id
            }

            response = requests.post(url, headers=headers)

            if response.status_code == 200:
                print(f"{GREEN}SUCCESS{RESET}")
            else:
                print(f"{RED}ERROR{RESET}")

        except requests.exceptions.ConnectionError:
            pass

def bwsub():
    while True:
        try:
            random_bot = random.choice(bot_lines)
            bot_id, bot_token = random_bot.split(':')
        except ValueError:
            continue

        try:
            url = f"http://gw.sandboxol.com/bedwar/api/v1/follow/add?targetId={user_id}"

            headers = {
                'Access-Token': bot_token,
                'userId': bot_id
            }

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                print(f"{GREEN}SUCCESS{RESET}")
            else:
                print(f"{RED}ERROR{RESET}")

        except requests.exceptions.ConnectionError:
            pass

def like():
    while True:
        try:
            random_bot = random.choice(bot_lines)
            bot_id, bot_token = random_bot.split(':')
        except ValueError:
            continue

        try:
            url_1 = "http://modsgs.sandboxol.com/friend/api/v1/friends"

            headers_1 = {
                'userId': bot_id,
                'Access-Token': bot_token,
                'User-Agent': 'okhttp/3.12.1'
            }

            data = {
                'friendId': user_id,
                'msg': ''
            }

            response = requests.post(url_1, headers=headers_1, json=data)

            url_2 = "http://modsgs.sandboxol.com/friend/api/v1/friends/requests/approve-all"

            headers_2 = {
                'userId': user_id,
                'Access-Token': user_token,
                'User-Agent': 'okhttp/3.12.1'
            }

            response = requests.post(url_2, headers=headers_2)

            url_3 = f"http://modsgs.sandboxol.com/friend/api/v1/popularity?friendId={user_id}"

            response = requests.post(url_3, headers=headers_1)

            if response.status_code == 200:
                print(f"{GREEN}SUCCESS{RESET}")
            else:
                print(f"{RED}ERROR{RESET}")

            url_4 = f"http://modsgs.sandboxol.com/friend/api/v1/friends?friendId={user_id}"

            response = requests.delete(url_4, headers=headers_1)

        except requests.exceptions.ConnectionError:
            pass

def chspam():
    while True:
        try:
            random_bot = random.choice(bot_lines)
            bot_id, bot_token = random_bot.split(':')
        except ValueError:
            continue

        try:
            url = f"http://modsgs.sandboxol.com/msg/api/v1/msg/group/chat/apply?groupId={group_id}&msg={group_msg}"

            headers = {
                'userId': bot_id,
                'Access-Token': bot_token,
                'User-Agent': 'okhttp/3.12.1'
            }

            response = requests.post(url, headers=headers)

            if response.status_code == 200:
                print(f"{GREEN}SUCCESS{RESET}")
            else:
                print(f"{RED}ERROR{RESET}")

        except requests.exceptions.ConnectionError:
            pass

def clspam():
    while True:
        try:
            random_bot = random.choice(bot_lines)
            bot_id, bot_token = random_bot.split(':')
        except ValueError:
            continue

        try:
            url = "http://modsgs.sandboxol.com/clan/api/v1/clan/tribe/member"

            headers = {
                'userId': bot_id,
                'Access-Token': bot_token,
                'User-Agent': 'okhttp/3.12.1'
            }

            data = {
                'clanId': clan_id,
                'msg': clan_msg
            }

            response = requests.post(url, headers=headers, json=data)

            if response.status_code == 200:
                print(f"{GREEN}SUCCESS{RESET}")
            else:
                print(f"{RED}ERROR{RESET}")

        except requests.exceptions.ConnectionError:
            pass

def frspam():
    while True:
        try:
            random_bot = random.choice(bot_lines)
            bot_id, bot_token = random_bot.split(':')
        except ValueError:
            continue

        try:
            url = "http://modsgs.sandboxol.com/friend/api/v1/friends"

            headers = {
                'userId': bot_id,
                'Access-Token': bot_token,
                'User-Agent': 'okhttp/3.12.1'
            }

            data = {
                'friendId': user_id,
                'msg': ''
            }

            response = requests.post(url, headers=headers, json=data)

            if response.status_code == 200:
                print(f"{GREEN}SUCCESS{RESET}")
            else:
                print(f"{RED}ERROR{RESET}")

        except requests.exceptions.ConnectionError:
            pass

def ffspam():
    while True:
        try:
            random_bot = random.choice(bot_lines)
            bot_id, bot_token = random_bot.split(':')
        except ValueError:
            continue

        try:
            url = "http://modsgs.sandboxol.com/friend/api/v1/family/apply"

            headers = {
                'userId': bot_id,
                'Access-Token': bot_token,
                'User-Agent': 'okhttp/3.12.1'
            }

            data = {
                'age': spam_age,
                'msg': spam_msg,
                'ownerId': user_id,
                'sex': 0
            }

            response = requests.post(url, headers=headers, json=data)

            if response.status_code == 200:
                print(f"{GREEN}SUCCESS{RESET}")
            else:
                print(f"{RED}ERROR{RESET}")

        except requests.exceptions.ConnectionError:
            pass

def fspam():
    while True:
        random_region = region(region_set)
        try:
            random_bot = random.choice(bot_lines)
            bot_id, bot_token = random_bot.split(':')
        except ValueError:
            continue

        try:
            url = "http://modsgs.sandboxol.com/friend/api/v1/family/recruit"

            headers_1 = {
                'userId': bot_id,
                'Access-Token': bot_token,
                'User-Agent': 'okhttp/3.12.1'
            }

            response = requests.delete(url, headers=headers_1)

            age = random.randint(0, 200)
            member_type = random.randint(1, 4)
            owner_type = random.randint(1, 4)

            headers_2 = {
                'userId': bot_id,
                'Access-Token': bot_token,
                'appVersion': '4983',
                'userLanguage': random_region,
                'User-Agent': 'okhttp/3.12.1'
            }

            data = {
                'age': age,
                'memberType': member_type,
                'ownerType': owner_type
            }

            response = requests.post(url, headers=headers_2, json=data)

            if response.status_code == 200:
                print(f"{GREEN}SUCCESS{RESET}")
            else:
                print(f"{RED}ERROR{RESET}")

        except requests.exceptions.ConnectionError:
            pass

def token():
    token_info = jwt.decode(user_token, options={"verify_signature": False})

    user_id = token_info.get('jti')
    created_set = token_info.get('iat')
    expires_set = token_info.get('exp')

    created = datetime.utcfromtimestamp(created_set).strftime('%Y-%m-%d %H:%M:%S')
    expires = datetime.utcfromtimestamp(expires_set).strftime('%Y-%m-%d %H:%M:%S')

    print(f""" • ID: {RED}{user_id}{RESET}
 • Created: {RED}{created}{RESET}
 • Expires: {RED}{expires}{RESET}\n\n""")

    url = "http://modsgs.sandboxol.com/user/api/v2/user/details/info"

    headers = {
        'userId': user_id,
        'Access-Token': user_token,
        'User-Agent': 'okhttp/3.12.1'
    }

    response = requests.get(url, headers=headers)

    response = response.json()

    nickName = response['data']['nickName']
    picUrl = response['data']['picUrl']
    email = response['data']['email']
    birthday = response['data']['birthday']
    gDiamonds = response['data']['gDiamonds']
    account = response['data']['account']
    country = response['data']['country']
    clientIp = response['data']['clientIp']
    registerTime = response['data']['registerTime']
    vipLv = response['data']['vipLv']
    vipExp = response['data']['vipExp']
    vipMaxExp = response['data']['vipMaxExp']
    vipIcon = response['data']['vipIcon']
    actualCountry = response['data']['actualCountry']

    register = datetime.utcfromtimestamp(registerTime).strftime('%Y-%m-%d %H:%M:%S')

    print(f""" • nickname: {RED}{nickName}{RESET}
 • picUrl: {RED}{picUrl}{RESET}
 • email: {RED}{email}{RESET}
 • birthday: {RED}{birthday}{RESET}
 • GCUBES: {RED}{gDiamonds}{RESET}
 • username: {RED}{account}{RESET}
 • country: {RED}{country}{RESET}
 • IP: {RED}{clientIp}{RESET}
 • register: {RED}{register}{RESET}
 • vipLv: {RED}{vipLv}{RESET}
 • vipExp: {RED}{vipExp}{RESET}
 • vipMaxExp: {RED}{vipMaxExp}{RESET}
 • vipIcon: {RED}{vipIcon}{RESET}
 • actualCountry: {RED}{actualCountry}{RESET}""")

def details():
    try:
        url = "http://modsgs.sandboxol.com/user/api/v1/user/info"

        headers = {
            'userId': user_id,
            'Access-Token': user_token,
            'User-Agent': 'okhttp/3.12.1'
        }

        data = {'details': details_set}

        response = requests.put(url, headers=headers, json=data)

        if response.status_code == 200:
            print(f"{GREEN}SUCCESS{RESET}")
        else:
            print(f"{RED}ERROR{RESET}")

    except requests.exceptions.ConnectionError:
        pass

def birthday():
    try:
        url = "http://modsgs.sandboxol.com/user/api/v1/user/info"

        headers = {
            'userId': user_id,
            'Access-Token': user_token,
            'User-Agent': 'okhttp/3.12.1'
        }

        data = {'birthday': birthday}

        response = requests.put(url, headers=headers, json=data)

        if response.status_code == 200:
            print(f"{GREEN}SUCCESS{RESET}")
        else:
            print(f"{RED}ERROR{RESET}")

    except requests.exceptions.ConnectionError:
        pass

while True:
    commands = input("\nᴄᴏᴍᴍᴀɴᴅ: ").lower()

    if commands == 'bwlike':
        clear()
        user_id = input("ID: ")
        clear()
        print(f"Speed >>> {RED}500{RESET}")
        t = int(input("\nthreads: "))
        clear()
        threads = []
        for i in range(t):
            thread = threading.Thread(target=bwlike)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    elif commands == 'bwsub':
        clear()
        user_id = input("ID: ")
        clear()
        print(f"Speed >>> {RED}500{RESET}")
        t = int(input("\nthreads: "))
        clear()
        threads = []
        for i in range(t):
            thread = threading.Thread(target=bwsub)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    elif commands == 'like':
        clear()
        user_id = input("ID: ")
        clear()
        print(f"Tutorial in Telegram {RED}@nullowns{RESET}\n")
        user_token = input("Access-Token: ")
        clear()
        print(f"Speed >>> {RED}20{RESET}")
        t = int(input("\nthreads: "))
        clear()
        threads = []
        for i in range(t):
            thread = threading.Thread(target=like)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    elif commands == 'chspam':
        clear()
        group_id = input("GROUP ID: ")
        clear()
        group_msg = input("SPAM MESSAGE: ")
        clear()
        print(f"Speed >>> {RED}5{RESET}")
        t = int(input("\nthreads: "))
        clear()
        threads = []
        for i in range(t):
            thread = threading.Thread(target=chspam)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    elif commands == 'clspam':
        clear()
        clan_id = input("CLAN ID: ")
        clear()
        clan_msg = input("SPAM MESSAGE: ")
        clear()
        print(f"Speed >>> {RED}5{RESET}")
        t = int(input("\nthreads: "))
        clear()
        threads = []
        for i in range(t):
            thread = threading.Thread(target=clspam)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    elif commands == 'frspam':
        clear()
        user_id = input("ID: ")
        clear()
        print(f"Speed >>> {RED}5{RESET}")
        t = int(input("\nthreads: "))
        clear()
        threads = []
        for i in range(t):
            thread = threading.Thread(target=frspam)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    elif commands == 'ffspam':
        clear()
        user_id = input("ID: ")
        clear()
        spam_age = input("(0-999999999) AGE: ")
        clear()
        spam_msg = input("SPAM MESSAGE: ")
        clear()
        print(f"Speed >>> {RED}20{RESET}")
        t = int(input("\nthreads: "))
        clear()
        threads = []
        for i in range(t):
            thread = threading.Thread(target=ffspam)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    elif commands == 'fspam':
        clear()
        print("zh_CN 🇨🇳\nen_US 🇺🇸\nde_DE 🇩🇪\nes_ES 🇪🇸\nfr_FR 🇫🇷\nhi_IN 🇮🇳\nin_ID 🇮🇩\nit_IT 🇮🇹\nja_JP 🇯🇵\nko_KR 🇰🇷\npl_PL 🇵🇱\npt_PT 🇵🇹\nru_RU 🇷🇺\nth_TH 🇹🇭\ntr_TR 🇹🇷\nuk_UA 🇺🇦\nvi_VN 🇻🇳\n\nzh_CN, en_US, de_DE, es_ES, fr_FR, hi_IN, in_ID, it_IT, ja_JP, ko_KR, pl_PL, pt_PT, ru_RU, th_TH, tr_TR, uk_UA, vi_VN")
        region_set = input("\n\nregion: ")
        clear()
        print(f"Speed >>> {RED}20{RESET}\n")
        t = int(input("threads: "))
        clear()
        processed_region = region(region_set)
        threads = []
        for i in range(t):
            thread = threading.Thread(target=fspam)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    elif commands == 'token':
        clear()
        print(f"Tutorial in Telegram {RED}@nullowns{RESET}\n")
        user_token = input("Access-Token: ")
        clear()
        token()

    elif commands == 'details':
        clear()
        user_id = input("ID: ")
        clear()
        print(f"Tutorial in Telegram {RED}@nullowns{RESET}\n")
        user_token = input("Access-Token: ")
        clear()
        details_set = input("details: ")
        clear()
        details()

    elif commands == 'birthday':
        clear()
        user_id = input("ID: ")
        clear()
        print(f"Tutorial in Telegram {RED}@nullowns{RESET}\n")
        user_token = input("Access-Token: ")
        clear()
        details_set = input("details: ")
        clear()
        birthday()
