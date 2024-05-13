import os
import random
import threading

import requests

print("""  ____  _            _            __  __           _     
 | __ )| | ___   ___| | ___   _  |  \/  | ___   __| |___ 
 |  _ \| |/ _ \ / __| |/ / | | | | |\/| |/ _ \ / _` / __|
 | |_) | | (_) | (__|   <| |_| | | |  | | (_) | (_| \__ \
 |____/|_|\___/ \___|_|\_\\__, | |_|  |_|\___/ \__,_|___/
                          |___/                          """, "\n\033[95mby NULL TEAM\033[0m", "\n\nLIST:", "\n - \033[95mfamily_spam\033[0m")
commands = input("\ncommand: ")

class bot_list:
        def bot(self):
        	response = requests.get('https://raw.githubusercontent.com/nullowns/BlockyMods/main/bot.txt')
        	bot_lines = response.text.splitlines()
        	random_bot = random.choice(bot_lines).strip()
        	bot_id, bot_token = random_bot.split(':')
        	return bot_id, bot_token

def family_spam():
	if commands.lower() == 'family_spam':
		os.system('clear')
		while True:
			class_bot = bot_list()
			bot_id, bot_token = class_bot.bot()

			API_1 = "http://modsgs.sandboxol.com/friend/api/v1/family/recruit"

			headers_1 = {'userId': bot_id, 'Access-Token': bot_token, 'User-Agent': 'okhttp/3.12.1'}

			response = requests.delete(API_1, headers=headers_1)

			memberType = random.choice([1, 2, 3, 4])
			ownerType = random.choice([1, 2, 3, 4])
			age = random.randint(9, 200)

			data_1 = {'age': age, 'memberType': memberType, 'ownerType': ownerType}

			headers_2 = {'userId': bot_id, 'Access-Token': bot_token, 'appVersion': '4971', 'userLanguage': 'ru_RU', 'User-Agent': 'okhttp/3.12.1'}

			response = requests.post(API_1, headers=headers_2, json=data_1)
			print(response.text)

threads = []
for i in range(5):
    thread = threading.Thread(target=family_spam)
    threads.append(thread)
    thread.start()

for thread in threads:
	thread.join()
