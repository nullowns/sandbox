import os
import random
import threading
import requests

commands = f"\n      - \033[91mfamily_spam\033[0m"

def banner():
	print("""  _   _    _    ____ _  _______ ____  
 | | | |  / \  / ___| |/ / ____|  _ \ 
 | |_| | / _ \| |   | ' /|  _| | |_) |
 |  _  |/ ___ \ |___| . \| |___|  _ < 
 |_| |_/_/   \_\____|_|\_\_____|_| \_\
                                      """, f"\n\033[91mＮＵＬＬ ＴＥＡＭ\033[0m\n\n     ʟɪsᴛ: {commands}")

banner()
t = int(input("\nthreads: "))
os.system('clear')

print("downloading bots...")
bot = 'https://raw.githubusercontent.com/nullowns/Blocky-Mods/main/bot.txt'
response = requests.get(bot)

bot_list = response.text
bot_lines = bot_list.split('\n')
os.system('clear')

banner()
commands = input("\nᴄᴏᴍᴍᴀɴᴅ: ")

def family_spam():
	if commands.lower() == 'family_spam':
		os.system('clear')
		while True:
			random_bot = random.choice(bot_lines)
			bot_id, bot_token = random_bot.split(':')

			API_1 = "http://modsgs.sandboxol.com/friend/api/v1/family/recruit"

			headers_1 = {'userId': bot_id, 'Access-Token': bot_token, 'User-Agent': 'okhttp/3.12.1'}

			response = requests.delete(API_1, headers=headers_1)

			age = random.randint(9, 200)
			memberType = random.randint(1, 4)
			ownerType = random.randint(1, 4)

			data_1 = {'age': age, 'memberType': memberType, 'ownerType': ownerType}

			headers_2 = {'userId': bot_id, 'Access-Token': bot_token, 'appVersion': '4971', 'userLanguage': 'ru_RU', 'User-Agent': 'okhttp/3.12.1'}

			response = requests.post(API_1, headers=headers_2, json=data_1)
			print(response.text)

threads = []
for i in range(t):
	thread = threading.Thread(target=family_spam)
	threads.append(thread)
	thread.start()

for thread in threads:
	thread.join()
