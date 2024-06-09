import os
import random
import threading
import platform
import shutil
from datetime import datetime
import time

import requests
from colorama import init, Fore, Style
import jwt

def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

clear()

RED = Fore.LIGHTRED_EX
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.LIGHTYELLOW_EX
MAGENTA = Fore.LIGHTMAGENTA_EX
RESET = Fore.RESET

BRIGHT = Style.BRIGHT
RESET_ALL = Style.RESET_ALL

init()

print(f"{BRIGHT}{GREEN}bot checker...{RESET}{RESET_ALL}")

while True:
    try:
        response = requests.get('https://raw.githubusercontent.com/nullowns/blockymods/main/bot.txt')
        bots = response.text.split('\n')
        break
    except requests.exceptions.ConnectionError:
        continue

clear()

version = "v𝟷.𝟷.𝟸"

commands = (
    f"\n      - start\n\n"
    f"      - bwlike\n"
    f"      - bwsub\n"
    f"      - like\n\n"
    f"      - chspam\n"
    f"      - clspam\n"
    f"      - frspam\n"
    f"      - ffspam\n"
    f"      - fspam\n\n"
    f"      - token\n"
    f"      - details\n"
    f"      - birthday\n"
    f"      - botdel"
)

columns = shutil.get_terminal_size().columns

line_1 = '-' * columns
line_2 = '═' * columns

start = f"""{Fore.BLUE}  _   _ _   _ _     _        _____        ___   _ ____  
 | \ | | | | | |   | |      / _ \ \      / / \ | / ___| 
 |  \| | | | | |   | |     | | | \ \ /\ / /|  \| \___ \ 
 | |\  | |_| | |___| |___  | |_| |\ V  V / | |\  |___) |
 |_| \_|\___/|_____|_____|  \___/  \_/\_/  |_| \_|____/ 
                                                        {RESET}
{BRIGHT}{line_1}
{GREEN}{version}{RESET}

     ʟɪsᴛ {YELLOW}{commands}{RESET}

{line_2}
{MAGENTA}Telegram: @nullowns{RESET}
{line_1}
{MAGENTA}GitHub: https://github.com/nullowns/blockymods{RESET}
{line_2}{RESET_ALL}\n"""

def banner(text):
    for character in text:
        print(character, end='', flush=True)
        time.sleep(0.002)

banner(start)

def region(text):
    return random.choice([part.strip() for part in text.split(',')])

def bwlike():
    while True:
        try:
            bot = random.choice(bots)
            bot_id, bot_token = bot.split(':')
        except ValueError:
            continue

        url = f"http://gw.sandboxol.com/bedwar/api/v1/thumbs-up?beneficiaryId={user_id}"

        headers = {
            'Access-Token': bot_token,
            'userId': bot_id
        }

        try:
            response = requests.post(url, headers=headers)
        except requests.exceptions.ConnectionError:
            continue

        data = response.json()
        message = data.get('message')

        if logs == "1":
            if message == "SUCCESS":
                print(f"{BRIGHT}{GREEN}SUCCESS{RESET}{RESET_ALL}")
            else:
                print(f"{BRIGHT}{RED}{message}{RESET}{RESET_ALL}")

        elif logs == "2":
            if message == "SUCCESS":
                print(f"{BRIGHT}{GREEN}SUCCESS{RESET}{RESET_ALL}")

def bwsub():
    while True:
        try:
            bot = random.choice(bots)
            bot_id, bot_token = bot.split(':')
        except ValueError:
            continue

        url = f"http://gw.sandboxol.com/bedwar/api/v1/follow/add?targetId={user_id}"

        headers = {
            'Access-Token': bot_token,
            'userId': bot_id
        }

        try:
            response = requests.get(url, headers=headers)
        except requests.exceptions.ConnectionError:
            continue

        data = response.json()
        message = data.get('message')

        if logs == "1":
            if message == "success":
                print(f"{BRIGHT}{GREEN}success{RESET}{RESET_ALL}")
            else:
                print(f"{BRIGHT}{RED}{message}{RESET}{RESET_ALL}")

        elif logs == "2":
            if message == "success":
                print(f"{BRIGHT}{GREEN}success{RESET}{RESET_ALL}")

def like():
    token = jwt.decode(user_token, options={"verify_signature": False})
    user_id = token.get('jti')
    while True:
        try:
            bot = random.choice(bots)
            bot_id, bot_token = bot.split(':')
        except ValueError:
            continue

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

        try:
            response = requests.post(url_1, headers=headers_1, json=data)
        except requests.exceptions.ConnectionError:
            continue

        url_2 = "http://modsgs.sandboxol.com/friend/api/v1/friends/requests/approve-all"

        headers_2 = {
            'userId': user_id,
            'Access-Token': user_token,
            'User-Agent': 'okhttp/3.12.1'
        }

        try:
            response = requests.post(url_2, headers=headers_2)
        except requests.exceptions.ConnectionError:
            continue

        url_3 = f"http://modsgs.sandboxol.com/friend/api/v1/popularity?friendId={user_id}"

        try:
            response = requests.post(url_3, headers=headers_1)
        except requests.exceptions.ConnectionError:
            continue

        data = response.json()
        message = data.get('message')

        if logs == "1":
            if message == "SUCCESS":
                print(f"{BRIGHT}{GREEN}SUCCESS{RESET}{RESET_ALL}")
            else:
                print(f"{BRIGHT}{RED}{message}{RESET}{RESET_ALL}")

        elif logs == "2":
            if message == "SUCCESS":
                print(f"{BRIGHT}{GREEN}SUCCESS{RESET}{RESET_ALL}")

        url_4 = f"http://modsgs.sandboxol.com/friend/api/v1/friends?friendId={user_id}"

        try:
            response = requests.delete(url_4, headers=headers_1)
        except requests.exceptions.ConnectionError:
            continue

def chspam():
    while True:
        try:
            bot = random.choice(bots)
            bot_id, bot_token = bot.split(':')
        except ValueError:
            continue

        url = f"http://modsgs.sandboxol.com/msg/api/v1/msg/group/chat/apply?groupId={group_id}&msg={group_msg}"

        headers = {
            'userId': bot_id,
            'Access-Token': bot_token,
            'User-Agent': 'okhttp/3.12.1'
        }

        try:
            response = requests.post(url, headers=headers)
        except requests.exceptions.ConnectionError:
            continue

        data = response.json()
        message = data.get('message')

        if logs == "1":
            if message == "SUCCESS":
                print(f"{BRIGHT}{GREEN}SUCCESS{RESET}{RESET_ALL}")
            else:
                print(f"{BRIGHT}{RED}{message}{RESET}{RESET_ALL}")

        elif logs == "2":
            if message == "SUCCESS":
                print(f"{BRIGHT}{GREEN}SUCCESS{RESET}{RESET_ALL}")

        time.sleep(5)

def clspam():
    while True:
        try:
            bot = random.choice(bots)
            bot_id, bot_token = bot.split(':')
        except ValueError:
            continue

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

        try:
            response = requests.post(url, headers=headers, json=data)
        except requests.exceptions.ConnectionError:
            continue

        data = response.json()
        message = data.get('message')

        if logs == "1":
            if message == "SUCCESS":
                print(f"{BRIGHT}{GREEN}SUCCESS{RESET}{RESET_ALL}")
            else:
                print(f"{BRIGHT}{RED}{message}{RESET}{RESET_ALL}")

        elif logs == "2":
            if message == "SUCCESS":
                print(f"{BRIGHT}{GREEN}SUCCESS{RESET}{RESET_ALL}")

        time.sleep(5)

def frspam():
    while True:
        try:
            bot = random.choice(bots)
            bot_id, bot_token = bot.split(':')
        except ValueError:
            continue

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

        try:
            response = requests.post(url, headers=headers, json=data)
        except requests.exceptions.ConnectionError:
            continue

        data = response.json()
        message = data.get('message')

        if logs == "1":
            if message == "SUCCESS":
                print(f"{BRIGHT}{GREEN}SUCCESS{RESET}{RESET_ALL}")
            else:
                print(f"{BRIGHT}{RED}{message}{RESET}{RESET_ALL}")

        elif logs == "2":
            if message == "SUCCESS":
                print(f"{BRIGHT}{GREEN}SUCCESS{RESET}{RESET_ALL}")

        time.sleep(5)

def ffspam():
    while True:
        try:
            bot = random.choice(bots)
            bot_id, bot_token = bot.split(':')
        except ValueError:
            continue

        url = "http://modsgs.sandboxol.com/friend/api/v1/family/apply"

        headers = {
            'userId': bot_id,
            'Access-Token': bot_token,
            'User-Agent': 'okhttp/3.12.1'
        }

        data = {
            'age': 0,
            'msg': spam_msg,
            'ownerId': user_id,
            'sex': 0
        }

        try:
            response = requests.post(url, headers=headers, json=data)
        except requests.exceptions.ConnectionError:
            continue

        data = response.json()
        message = data.get('message')

        if logs == "1":
            if message == "success":
                print(f"{BRIGHT}{GREEN}success{RESET}{RESET_ALL}")
            else:
                print(f"{BRIGHT}{RED}{message}{RESET}{RESET_ALL}")

        elif logs == "2":
            if message == "success":
                print(f"{BRIGHT}{GREEN}success{RESET}{RESET_ALL}")

        time.sleep(5)

def fspam():
    processed_region = region(region_set)
    while True:
        random_region = region(region_set)
        try:
            bot = random.choice(bots)
            bot_id, bot_token = bot.split(':')
        except ValueError:
            continue

        url = "http://modsgs.sandboxol.com/friend/api/v1/family/recruit"

        headers_1 = {
            'userId': bot_id,
            'Access-Token': bot_token,
            'User-Agent': 'okhttp/3.12.1'
        }

        response = requests.delete(url, headers=headers_1)

        headers_2 = {
            'userId': bot_id,
            'Access-Token': bot_token,
            'appVersion': '4991',
            'userLanguage': random_region,
            'User-Agent': 'okhttp/3.12.1'
        }

        age = random.randint(0, 200)
        member_type = random.randint(1, 4)
        owner_type = random.randint(1, 4)

        data = {
            'age': age,
            'memberType': member_type,
            'ownerType': owner_type
        }

        try:
            response = requests.post(url, headers=headers_2, json=data)
        except requests.exceptions.ConnectionError:
            continue

        data = response.json()
        message = data.get('message')

        if logs == "1":
            if message == "success":
                print(f"{BRIGHT}{GREEN}success{RESET}{RESET_ALL}")
            else:
                print(f"{BRIGHT}{RED}{message}{RESET}{RESET_ALL}")

        elif logs == "2":
            if message == "success":
                print(f"{BRIGHT}{GREEN}success{RESET}{RESET_ALL}")

        time.sleep(5)

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
    token = jwt.decode(user_token, options={"verify_signature": False})
    user_id = token.get('jti')

    url = "http://modsgs.sandboxol.com/user/api/v1/user/info"

    headers = {
        'userId': user_id,
        'Access-Token': user_token,
        'User-Agent': 'okhttp/3.12.1'
    }

    data = {'details': details_set}

    try:
        response = requests.put(url, headers=headers, json=data)
    except requests.exceptions.ConnectionError:
        pass

    data = response.json()
    message = data.get('message')

    if message == "SUCCESS":
        print(f"{BRIGHT}{GREEN}SUCCESS{RESET}{RESET_ALL}")
    else:
        print(f"{BRIGHT}{RED}{message}{RESET}{RESET_ALL}")

def birthday():
    token = jwt.decode(user_token, options={"verify_signature": False})
    user_id = token.get('jti')

    url = "http://modsgs.sandboxol.com/user/api/v1/user/info"

    headers = {
        'userId': user_id,
        'Access-Token': user_token,
        'User-Agent': 'okhttp/3.12.1'
    }

    data = {'birthday': birthday_set}

    try:
        response = requests.put(url, headers=headers, json=data)
    except requests.exceptions.ConnectionError:
        pass

    data = response.json()
    message = data.get('message')

    if message == "SUCCESS":
        print(f"{BRIGHT}{GREEN}SUCCESS{RESET}{RESET_ALL}")
    else:
        print(f"{BRIGHT}{RED}{message}{RESET}{RESET_ALL}")

def botdel():
    while True:
        bot = random.choice(bots)
        bot_id, bot_token = bot.split(':')

        url = f"http://modsgs.sandboxol.com/friend/api/v1/friends?friendId={user_id}"

        headers = {
            'userId': bot_id,
            'Access-Token': bot_token,
            'User-Agent': 'okhttp/3.12.1'
        }

        try:
            response = requests.delete(url, headers=headers)
        except requests.exceptions.ConnectionError:
            continue

        data = response.json()
        message = data.get('message')

        if logs == "1":
            if message == "SUCCESS":
                print(f"{BRIGHT}{GREEN}SUCCESS{RESET}{RESET_ALL}")
            else:
                print(f"{BRIGHT}{RED}{message}{RESET}{RESET_ALL}")

        elif logs == "2":
            if message == "SUCCESS":
                print(f"{BRIGHT}{GREEN}SUCCESS{RESET}{RESET_ALL}")

        time.sleep(5)

while True:
    command = ' '.join(input("\nᴄᴏᴍᴍᴀɴᴅ: ").lower().split())

    if commands == "start":
        clear()
        banner(start)

    elif command == "bwlike":
        clear()
        user_id = ' '.join(input("ID: ").split())
        clear()
        logs = ' '.join(input("logs: ").split())
        clear()
        threads = []
        for i in range(1000):
            thread = threading.Thread(target=bwlike)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    elif command == "bwsub":
        clear()
        user_id = ' '.join(input("ID: ").split())
        clear()
        logs = ' '.join(input("logs: ").split())
        clear()
        threads = []
        for i in range(1000):
            thread = threading.Thread(target=bwsub)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    elif command == "like":
        clear()
        user_token = ' '.join(input("Access-Token: ").split())
        clear()
        logs = ' '.join(input("logs: ").split())
        clear()
        threads = []
        for i in range(20):
            thread = threading.Thread(target=like)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    elif command == "chspam":
        clear()
        group_id = ' '.join(input("ID: ").split())
        clear()
        group_msg = ' '.join(input("MESSAGE: ").split())
        clear()
        logs = ' '.join(input("logs: ").split())
        clear()
        threads = []
        for i in range(5):
            thread = threading.Thread(target=chspam)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    elif command == "clspam":
        clear()
        clan_id = ' '.join(input("ID: ").split())
        clear()
        clan_msg = ' '.join(input("MESSAGE: ").split())
        clear()
        logs = ' '.join(input("logs: ").split())
        clear()
        threads = []
        for i in range(5):
            thread = threading.Thread(target=clspam)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    elif command == "frspam":
        clear()
        user_id = ' '.join(input("ID: ").split())
        clear()
        logs = ' '.join(input("logs: ").split())
        clear()
        threads = []
        for i in range(5):
            thread = threading.Thread(target=frspam)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    elif command == "ffspam":
        clear()
        user_id = ' '.join(input("ID: ").split())
        clear()
        spam_msg = ' '.join(input("MESSAGE: ").split())
        clear()
        logs = ' '.join(input("logs: ").split())
        clear()
        threads = []
        for i in range(20):
            thread = threading.Thread(target=ffspam)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    elif command == "fspam":
        clear()
        region_set = ' '.join(input("REGION: ").split())
        clear()
        logs = ' '.join(input("logs: ").split())
        clear()
        threads = []
        for i in range(20):
            thread = threading.Thread(target=fspam)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    elif command == "token":
        clear()
        user_token = input("Access-Token: ")
        clear()
        token()

    elif command == "details":
        clear()
        user_token = ' '.join(input("Access-Token: ").split())
        clear()
        details_set = ' '.join(input("details: ").split())
        clear()
        details()

    elif command == "birthday":
        clear()
        user_token = ' '.join(input("Access-Token: ").split())
        clear()
        birthday_set = input("birthday: ")
        clear()
        birthday()

    elif command == "botdel":
        clear()
        user_id = ' '.join(input("ID: ").split())
        clear()
        logs = ' '.join(input("logs: ").split())
        clear()
        threads = []
        for i in range(20):
            thread = threading.Thread(target=botdel)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
