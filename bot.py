import re
import requests
import datetime
import urllib
import time


SQUEEZE_URL = "http://isthesqueezesquoze.com/"

BOT_TOKEN = "[TOKEN]"
CHANNEL_ID = "[CHANNEL_ID]"


BOT_SEND_TEXT_REQUEST = "https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&parse_mode=MarkdownV2&text={text}"


RE_SQUOZE = "<u>not</u>"


def send_message(text):
	text = urllib.parse.quote(text)
	request_url = BOT_SEND_TEXT_REQUEST.format(bot_token=BOT_TOKEN, chat_id=CHANNEL_ID, text=text)	
	reponse = requests.get(request_url)


def spam_update():
	for i in range(10):
		send_message("SQUEEZE HAS SQUOZE\\! \U0001F680\U0001F680")

def check_squeeze():
	data = requests.get(SQUEEZE_URL)
	if len(re.findall(RE_SQUOZE, data.text)) < 1:
		return True
	else:
		return False

def write_log(time):
	time = time.strftime("%d/%m/%Y, %H:%M:%S")
	with open("/tmp/squeeze_bot_log", "a") as log:
		log.write("%s - Still running\r\n" % time)


squoze = False
hour = False
log_minute = False
while 1:
	squoze = check_squeeze()
	if squoze:
		spam_update()
		squoze = True
# Once an hour was getting annoying
#	else:
#		now = datetime.datetime.now()
#		if now.minute == 0:
#			if hour == False:				
#					send_message("Hourly update: Not Squoze \U0001F48E\U0001F64F")
#					hour = True
#		else:
#			hour = False
#		if now.second == 0:
#			if log_minute == False:
#				write_log(now)
#				log_minute = True
#		else:
#			log_minute = False
	time.sleep(1)




