import vk_api
import time
import random
import datetime

start_time = datetime.datetime.now()
vk = vk_api.VkApi(login='+####',password='#####')
vk.auth()
message = '🎃Бот - "Botprofcon"🎃'


def set_status(message):
	time = datetime.datetime.now()
	uptime = (datetime.datetime.now() - start_time).total_seconds()
	hours, remainder = divmod(uptime,3600)
	minutes, seconds = divmod(remainder,60)
	text = f"💻 PC | 📅 {str(time).split()[0]} | ⌚ {str(time).split()[1][:5]} | ♻ Вечный онлайн: {'%02d:%02d:%02d'%(hours, minutes, seconds)}"
	vk.method('status.set',{'text':text})
	message+=f'\n✅Статус установлен: {text}✅'
	return message

def friends_remove(message):
	requests = vk.method('friends.getRequests',{'extended':0, 'need_mutual':0, 'out':1})
	spis = ''
	if not requests:
		return
	for user_id in requests["items"]:
		vk.method('account.ban',{'owner_id':user_id})
		spis += f'\n[id{user_id}|Пользователь] - {user_id}'
	if spis == '' : spis = '\nСписок пуст'
	message += f'\n✅ЧС пополнен: {spis}✅'
	return message

def friends_accept(message):
	requests = vk.method('friends.getRequests',{'out':0,'need_viewed':0})
	spis = ''
	if not requests:
		return
	for user_id in requests["items"]:
		vk.method('friends.add',{'user_id':user_id})
		spis += f'\n[id{user_id}|Пользователь] - {user_id}'
	if spis == '' : spis = '\nСписок пуст'
	message += f'\n✅Заявки в друзья приняты: {spis}✅'
	return message

def online(message):
	vk.method('account.setOnline')
	message += '\n✅Онлайн установлен✅'
	return message

def message_otchet(message):
	message += '\n🎃Ваш персональный бот - "Botprofcon"🎃'
	vk.method('messages.send',{'user_id':408801395,'message':message})
	return None

while True:
	set_status_otchet = set_status(message)
	friends_remove_otchet = friends_remove(set_status_otchet)
	friends_accept_otchet = friends_accept(friends_remove_otchet)
	online_otchet = online(friends_accept_otchet)
	message_otchet(online_otchet)
	time.sleep(60)
	message = '🎃Бот🎃'
