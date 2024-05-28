import os
import platform
import random
import threading

from colorama import init, Fore
import requests

init()

def clear():
	if platform.system() == "Windows":
		os.system("cls")
	else:
		os.system("clear")

clear()

RED = Fore.LIGHTRED_EX
RESET = Fore.RESET

commands = f"\n      - {RED}bwlike{RESET}\n      - {RED}bwsub{RESET}\n      - {RED}like{RESET}\n\n      - {RED}chspam{RESET}\n      - {RED}clspam{RESET}\n      - {RED}frspam{RESET}\n      - {RED}ffspam{RESET}\n      - {RED}fspam{RESET}\n\n      - {RED}region{RESET}"

def banner():
	print("""  _   _    _    ____ _  _______ ____  
 | | | |  / \  / ___| |/ / ____|  _ \ 
 | |_| | / _ \| |   | ' /|  _| | |_) |
 |  _  |/ ___ \ |___| . \| |___|  _ < 
 |_| |_/_/   \_\____|_|\_\_____|_| \_\
                                      """, f"\n{RED}ＮＵＬＬ ＴＥＡＭ{RESET}\n-----------------\n{RED}v１.１.０{RESET}\n\n     ʟɪsᴛ: {commands}")

print(f"{Fore.LIGHTGREEN_EX}downloading bots...{RESET}")

bot = "https://raw.githubusercontent.com/nullowns/blockymods/main/bot.txt"

while True:
    try:
        response = requests.get(bot)
        response.raise_for_status()
        bot_lines = response.text.split('\n')
        break
    except requests.exceptions.ConnectionError:
        pass

clear()

banner()

def region(text):
	items = text.split(',')
	region_items = [item.strip().strip('"').strip("'") for item in items]
	return region_items

def bwlike():
	while True:
		try:
			random_bot = random.choice(bot_lines)
			bot_id, bot_token = random_bot.split(':')
		except ValueError:
			continue
		try:
			API_1 = f"http://gw.sandboxol.com/bedwar/api/v1/thumbs-up?beneficiaryId={bwlike_id}"

			headers_1 = {'Access-Token': bot_token, 'userId': bot_id}

			response = requests.post(API_1, headers=headers_1)
			
			if response.status_code == 200:
				print(f"{Fore.LIGHTGREEN_EX}SUCCESS{RESET}")
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
			API_2 = f"http://gw.sandboxol.com/bedwar/api/v1/follow/add?targetId={bwsub_id}"

			headers_2 = {'Access-Token': bot_token, 'userId': bot_id}

			response = requests.get(API_2, headers=headers_2)

			if response.status_code == 200:
				print(f"{Fore.LIGHTGREEN_EX}SUCCESS{RESET}")
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
			API_3 = "http://modsgs.sandboxol.com/friend/api/v1/friends"

			data_1 = {'friendId': like_id, 'msg': 'let\'s be friends!', 'type': 2}

			headers_3 = {'userId': bot_id, 'Access-Token': bot_token, 'User-Agent': 'okhttp/3.12.1'}

			response = requests.post(API_3, headers=headers_3, json=data_1)

			API_4 = "http://modsgs.sandboxol.com/friend/api/v1/friends/requests/approve-all"

			headers_4 = {'userId': like_id, 'Access-Token': like_token, 'User-Agent': 'okhttp/3.12.1'}

			response = requests.post(API_4, headers=headers_4)

			API_5 = f"http://modsgs.sandboxol.com/friend/api/v1/popularity?friendId={like_id}"

			headers_5 = {'userId': bot_id, 'Access-Token': bot_token, 'User-Agent': 'okhttp/3.12.1'}

			response = requests.post(API_5, headers=headers_5)

			if response.status_code == 200:
				print(f"{Fore.LIGHTGREEN_EX}SUCCESS{RESET}")
			else:
				print(f"{RED}ERROR{RESET}")

			API_6 = f"http://modsgs.sandboxol.com/friend/api/v1/friends?friendId={like_id}"

			headers_6 = {'userId': bot_id, 'Access-Token': bot_token, 'User-Agent': 'okhttp/3.12.1'}

			response = requests.delete(API_6, headers=headers_6)

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
			API_7 = f"http://modsgs.sandboxol.com/msg/api/v1/msg/group/chat/apply?groupId={chspam_id}&msg={chspam_details}"

			headers_7 = {'userId': bot_id, 'Access-Token': bot_token, 'User-Agent': 'okhttp/3.12.1'}

			response = requests.post(API_7, headers=headers_7)

			if response.status_code == 200:
				print(f"{Fore.LIGHTGREEN_EX}SUCCESS{RESET}")
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
			API_8 = "http://modsgs.sandboxol.com/clan/api/v1/clan/tribe/member"

			data_2 = {'clanId': clan_id, 'msg': details_clan}
			
			headers_8 = {'userId': bot_id, 'Access-Token': bot_token, 'User-Agent': 'okhttp/3.12.1'}

			response = requests.post(API_8, headers=headers_8, json=data_2)

			if response.status_code == 200:
				print(f"{Fore.LIGHTGREEN_EX}SUCCESS{RESET}")
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
			API_9 = "http://modsgs.sandboxol.com/friend/api/v1/friends"
			
			data_3 = {'friendId': frspam_id, 'msg': 'let\'s be friends!', 'type': 2}
			
			headers_9 = {'userId': bot_id, 'Access-Token': bot_token, 'User-Agent': 'okhttp/3.12.1'}
			
			response = requests.post(API_9, headers=headers_9, json=data_3)

			if response.status_code == 200:
				print(f"{Fore.LIGHTGREEN_EX}SUCCESS{RESET}")
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
			API_10 = "http://modsgs.sandboxol.com/friend/api/v1/family/apply"

			data_4 = {'age': ffspam_age, 'msg': ffspam_details, 'ownerId': ffspam_id, 'sex': 0, 'type': 1}

			headers_10 = {'userId': bot_id, 'Access-Token': bot_token, 'User-Agent': 'okhttp/3.12.1'}

			response = requests.post(API_10, headers=headers_10, json=data_4)

			if response.status_code == 200:
				print(f"{Fore.LIGHTGREEN_EX}SUCCESS{RESET}")
			else:
				print(f"{RED}ERROR{RESET}")

		except requests.exceptions.ConnectionError:
			pass

def fspam():
	while True:
		random_region = random.choice(processed_region)
		try:
			random_bot = random.choice(bot_lines)
			bot_id, bot_token = random_bot.split(':')
		except ValueError:
			continue
		try:
			API_11 = "http://modsgs.sandboxol.com/friend/api/v1/family/recruit"

			headers_11 = {'userId': bot_id, 'Access-Token': bot_token, 'User-Agent': 'okhttp/3.12.1'}

			response = requests.delete(API_11, headers=headers_11)

			age = random.randint(9, 200)
			memberType = random.randint(1, 4)
			ownerType = random.randint(1, 4)

			data_5 = {'age': age, 'memberType': memberType, 'ownerType': ownerType}

			headers_12 = {'userId': bot_id, 'Access-Token': bot_token, 'appVersion': '4981', 'userLanguage': random_region, 'User-Agent': 'okhttp/3.12.1'}

			response = requests.post(API_11, headers=headers_12, json=data_5)

			if response.status_code == 200:
				print(f"{Fore.LIGHTGREEN_EX}SUCCESS{RESET}")
			else:
				print(f"{RED}ERROR{RESET}")

		except requests.exceptions.ConnectionError:
			pass

while True:
	commands = input("\nᴄᴏᴍᴍᴀɴᴅ: ").lower()

	if commands == 'bwlike':
		clear()
		bwlike_id = input("ID: ")
		clear()
		t = int(input("threads: "))
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
		bwsub_id = input("ID: ")
		clear()
		t = int(input("threads: "))
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
		like_id = input("ID: ")
		clear()
		like_token = input("Access-Token: ")
		clear()
		t = int(input("threads: "))
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
		chspam_id = input("CHAT ID: ")
		clear()
		chspam_details = input("details: ")
		clear()
		t = int(input("threads: "))
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
		details_clan = input("details: ")
		clear()
		t = int(input("threads: "))
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
		frspam_id = input("ID: ")
		clear()
		t = int(input("threads: "))
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
		ffspam_id = input("ID: ")
		clear()
		ffspam_age = input("(0-999999999) age: ")
		clear()
		ffspam_details = input("details: ")
		clear()
		t = int(input("threads: "))
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
		region_give = input("region: ")
		clear()
		t = int(input("threads: "))
		clear()
		processed_region = region(region_give)
		threads = []
		for i in range(t):
			thread = threading.Thread(target=fspam)
			threads.append(thread)
			thread.start()

		for thread in threads:
			thread.join()

	elif commands == 'region':
		clear()
		print("zh_CN, en_US, de_DE, es_ES, fr_FR, hi_IN, in_ID, it_IT, ja_JP, ko_KR, pl_PL, pt_PT, ru_RU, th_TH, tr_TR, uk_UA, vi_VN", "\n\nzh_CN 🇨🇳\nen_US 🇺🇸\nde_DE 🇩🇪\nes_ES 🇪🇸\nfr_FR 🇫🇷\nhi_IN 🇮🇳\nin_ID 🇮🇩\nit_IT 🇮🇹\nja_JP 🇯🇵\nko_KR 🇰🇷\npl_PL 🇵🇱\npt_PT 🇵🇹\nru_RU 🇷🇺\nth_TH 🇹🇭\ntr_TR 🇹🇷\nuk_UA 🇺🇦\nvi_VN 🇻🇳")
