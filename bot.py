import vk_api
import time
import random
import datetime

start_time = datetime.datetime.now()
vk = vk_api.VkApi(login='+########',password='########')
vk.auth()

def set_status():
	time = datetime.datetime.now()
	uptime = (datetime.datetime.now() - start_time).total_seconds()
	hours, remainder = divmod(uptime,3600)
	minutes, seconds = divmod(remainder,60)
	vk.method('status.set',{'text':f"💻 PC | 📅 {str(time).split()[0]} | ⌚ {str(time).split()[1][:5]} | ♻ Вечный онлайн: {'%02d:%02d:%02d'%(hours, minutes, seconds)}"})

def friends_remove():
	requests = vk.method('friends.getRequests',{'extended':0, 'need_mutual':0, 'out':1})
	if not requests:
		return
	for user_id in requests["items"]:
		vk.method('account.ban',{'owner_id':user_id})
def friends_accept():
	requests = vk.method('friends.getRequests',{'out':0,'need_viewed':0})
	if not requests:
		return
	for user_id in requests["items"]:
		vk.method('friends.add',{'user_id':user_id})
def online():
	vk.method('account.setOnline')
while True:
	set_status()
	friends_remove()
	friends_accept()
	online()
	time.sleep(120)