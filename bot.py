# شرط VIP مباشر
def check_vip_override(message):
    if str(message.from_user.id) == "7156811419":
        return True
    return False

import telebot,os
import re,json
import requests
import telebot,time,random
import random
import string
from telebot import types
from gatet import *
from reg import reg
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading
from bs4 import BeautifulSoup
q='https://t.me/PLO_erf'
stopuser = {}
token = '8488601298:AAEC8HGiWbriEuYazjceO9v7hT_poMOS1VU'
bot=telebot.TeleBot(token,parse_mode="HTML")
admin= 7156811419
command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}	
@bot.message_handler(commands=["start"])
def start(message):
	def my_function():
		gate=''
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
		if BL == '𝗙𝗥𝗘𝗘':	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ المطور  ✨", url="https://t.me/PLO_erf")
			keyboard.add(contact_button)
			random_number = random.randint(33, 82)
			photo_url = f'https://t.me/bkddgfsa/{random_number}'
			bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''<b> {name}
اهلن بيك عزيزي المستخدم {BL}</b>
اسعار vip في هذا البوت
سبوع-3دولار
شهر-5دولار
سنه-7دولار
سورس البوت-15دولار
للشراء @PLO_erf
لعرض الوامر 
/cmd

	''',reply_markup=keyboard)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ المطور ✨", url="https://t.me/PLO_erf")
		keyboard.add(contact_button)
		username = message.from_user.first_name
		photo_url = 'https://t.me/aksnxnwndj/4'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption='''هلوو
		اهلن بيك في بوتنا المتواضع
بوت فحص فيزات✅🔥
لعرض الوامر
/cmd''',reply_markup=keyboard)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["cmd"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='𝗙𝗥𝗘𝗘'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"✨ {BL}  ✨",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text=f'''<b> 
ماذا يمكن للبوت فعله
فحص برنتري اوث
🔥✅<code>/cc </code> 𝗻𝘂𝗺𝗯𝗲𝗿|𝗺𝗺|𝘆𝘆|𝗰𝘃𝗰
«»»»»»»»»»»»»»»»»»»»»»»»»9

تحقق 3D
لفحص البطاقه فيه تحقق اولا🤍
<code>/vbv </code> 𝗻𝘂𝗺𝗯𝗲𝗿|𝗺𝗺|𝘆𝘆|𝗰𝘃𝗰

سوف يتم تحديث البوت وضافه عدد اكبر من البوابات

</b>
''',reply_markup=keyboard)
@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
		if BL == '𝗙𝗥𝗘𝗘':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ المطور  ✨", url="https://t.me/PLO_erf")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>{name}
اهلن بيك عزيزي المستخدم {BL}</b>
اسعار vip في هذا البوت
سبوع-3دولار
شهر-5دولار
سنه-7دولار
سورس البوت-15دولار
للشراء @PLO_erf
لعرض الوامر 
/cmd
</b>
''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ المطور  ✨", url="https://t.me/PLO_erf")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>{name}
اهلن بيك عزيزي المستخدم {BL}</b>
اسعار vip في هذا البوت
سبوع-3دولار
شهر-5دولار
سنه-7دولار
سورس البوت-15دولار
للشراء @PLO_erf
لعرض الوامر 
/cmd
</b>
''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ المطور  ✨", url="https://t.me/PLO_erf")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>انت غير مشترك بل بوت او اتم ايقاف تفعيلك🪪</b>
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text=f"🏴‍☠️ برنتري اوث 🏴‍☠️",callback_data='br')
		sw = types.InlineKeyboardButton(text=f"المطور @PLO_erf",url='https://t.me/PLO_erf')
		keyboard.add(contact_button)
		keyboard.add(sw)
		bot.reply_to(message, text=f'جاري الفحص💍',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)
@bot.callback_query_handler(func=lambda call: call.data == 'br')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='برنتري اوث'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "جاري الفحص...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='البوت شغال بواسطه ➜ @PLO_erf')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(Tele(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"[🟩 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅]🟩 ➜ [ {live} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"⃣[• 𝘾𝘾𝙉 ☑️] ➜ [ {ccnn} ] •]⃣", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"🟥[• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌]🟥 ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"🔰[• 𝙍𝙄𝙎𝙆 🏴‍☠️ ➜ [ {riskk} ] •]🔰", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 🆘𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''رجاء
					  تحله بل صبر فن الصبر جميل
					  المصدر@PLO_erf''', reply_markup=mes)
					
					msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
💳𝘾𝙖𝙧𝙙 >>>>>  <code>{cc}</code>
📟𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 >>>>>  {last}
📱𝙂𝙖𝙩𝙚𝙬𝙖𝙮 >>>>>  {gate}		
📃𝙄𝙣𝙛𝙤 >>>>>  {card_type} - {brand}
🔧𝘾𝙤𝙪𝙣𝙩𝙧𝙮 >>>>>  {country} - {country_flag} 
🗒𝘽𝙞𝙣 >>>>>  {cc[:6]}
🛡𝙄𝙨𝙨𝙪𝙚𝙧 >>>>>  {bank}
⏲️𝙏𝙞𝙢𝙚 >>>>>  {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @PLO_erf</b>'''
					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
					elif 'CVV' in last:
						ccnn+=1
					else:
						dd += 1
					time.sleep(4)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='البوت شغال بواسطه @PLO_erf')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'sq')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝗦𝗤𝗨𝗔𝗥𝗘 𝗔𝗨𝗧𝗛'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "جاري الفحص...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @PLO_erf')
						return
					try:
						data = requests.get('https://binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(sq(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝙍𝙄𝙎𝙆 🏴‍☠️ ➜ [ {riskk} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @PLO_erf''', reply_markup=mes)
					
					msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
💳𝘾𝙖𝙧𝙙 >>>>>  <code>{cc}</code>
📟𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 >>>>>  {last}
📱𝙂𝙖𝙩𝙚𝙬𝙖𝙮 >>>>>  {gate}		
📃𝙄𝙣𝙛𝙤 >>>>>  {card_type} - {brand}
🔧𝘾𝙤𝙪𝙣𝙩𝙧𝙮 >>>>>  {country} - {country_flag} 
🗒𝘽𝙞𝙣 >>>>>  {cc[:6]}
🛡𝙄𝙨𝙨𝙪𝙚𝙧 >>>>>  {bank}
⏲️𝙏𝙞𝙢𝙚 >>>>>  {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @PLO_erf</b>'''
					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
					elif 'CVV' in last:
						ccnn+=1
					else:
						dd += 1
					time.sleep(20)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='البوت شغال بواسطه ➜ @PLO_erf')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.cc') or message.text.lower().startswith('/cc'))
def respond_to_vbv(message):
	gate='برنتري اوث '
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ المطور  ✨", url="https://t.me/PLO_erf")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>{name}
اهلن بيك عزيزي المستخدم {BL}</b>
اسعار vip في هذا البوت
سبوع-3دولار
شهر-5دولار
سنه-7دولار
سورس البوت-15دولار
للشراء @PLO_erf
لعرض الوامر 
/cmd
</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ المطور  ✨", url="https://t.me/PLO_erf")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>{name}
اهلن بيك عزيزي المستخدم {BL}</b>
اسعار vip في هذا البوت
سبوع-3دولار
شهر-5دولار
سنه-7دولار
سورس البوت-15دولار
للشراء @PLO_erf
لعرض الوامر 
/cmd
</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ المطور  ✨", url="https://t.me/PLO_erf")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>انت غير مشترك بل بوت او اتم ايقاف تفعيلك🪪</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "جاري الفحص...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(Tele(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
💳𝘾𝙖𝙧𝙙 >>>>>  <code>{cc}</code>
📟𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 >>>>>  {last}
📱𝙂𝙖𝙩𝙚𝙬𝙖𝙮 >>>>>  {gate}		
📃𝙄𝙣𝙛𝙤 >>>>>  {card_type} - {brand}
🔧𝘾𝙤𝙪𝙣𝙩𝙧𝙮 >>>>>  {country} - {country_flag} 
🗒𝘽𝙞𝙣 >>>>>  {cc[:6]}
🛡𝙄𝙨𝙨𝙪𝙚𝙧 >>>>>  {bank}
⏲️𝙏𝙞𝙢𝙚 >>>>>  {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @PLO_erf</b>'''
	msgd=f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌
			
💳𝘾𝙖𝙧𝙙 >>>>>  <code>{cc}</code>
📟𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 >>>>>  {last}
📱𝙂𝙖𝙩𝙚𝙬𝙖𝙮 >>>>>  {gate}		
📃𝙄𝙣𝙛𝙤 >>>>>  {card_type} - {brand}
🔧𝘾𝙤𝙪𝙣𝙩𝙧𝙮 >>>>>  {country} - {country_flag} 
🗒𝘽𝙞𝙣 >>>>>  {cc[:6]}
🛡𝙄𝙨𝙨𝙪𝙚𝙧 >>>>>  {bank}
⏲️𝙏𝙞𝙢𝙚 >>>>>  {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @PLO_erf</b>'''
	if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.key') or message.text.lower().startswith('/key'))
def respond_to_vbv(message):
	def my_function():
		global stop
		try:
			re=message.text.split(' ')[1]
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			timer=(json_data[re]['time'])
			typ=(json_data[f"{re}"]["plan"])
			json_data[f"{message.from_user.id}"]['timer'] = timer
			json_data[f"{message.from_user.id}"]['plan'] = typ
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			with open('data.json', 'r') as json_file:
				data = json.load(json_file)
			del data[re]
			with open('data.json', 'w') as json_file:
				json.dump(data, json_file, ensure_ascii=False, indent=4)
			msg=f'''<b> مبروك لك الان
كلشي متاح لك واو🔥🔥🔥
 تم تفعيل الVIP🔥🔥
 𝗜𝗡 ➜ {timer}🌹
𝗧𝗬𝗣 ➜ {typ}</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,'<b> تحقق من اتصالك او عد المحاول بغير كود🪪 </b>',parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["vip"])
def start(message):
	def my_function():
		id=message.from_user.id
		if not id ==admin:
			return
		try:
			h=float(message.text.split(' ')[1])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			characters = string.ascii_uppercase + string.digits
			pas ='ABUAIL-'+''.join(random.choices(characters, k=6))+'»'+''.join(random.choices(characters, k=9))+'$'+''.join(random.choices(characters, k=2))+'%'+''.join(random.choices(characters, k=10))
			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan='𝗩𝗜𝗣'
			parts = str(ig).split(':')
			ig = ':'.join(parts[:2])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			msg=f'''<b>مبروك لك الان كلشي لك متاح لفتره زمنيه🔥🚀
		
𝗣𝗟𝗔𝗡 ➜ {plan}🔥
𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {ig}✅
𝗞𝗘𝗬 ➜ <code>{pas}</code>🟩
		
𝗨𝗦𝗘 /key [الكود]🔥</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.vbv') or message.text.lower().startswith('/vbv'))
def respond_to_vbv(message):
	id=message.from_user.id
	name = message.from_user.first_name
	gate='3𝑫𝑺 𝑳𝒐𝒐𝒌𝒖𝒑'
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	try:BL=(json_data[str(id)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		BL='𝗙𝗥𝗘𝗘'
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ المطور  ✨", url="https://t.me/PLO_erf")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>{name}
اهلن بيك عزيزي المستخدم {BL}</b>
اسعار vip في هذا البوت
سبوع-3دولار
شهر-5دولار
سنه-7دولار
سورس البوت-15دولار
للشراء @PLO_erf
لعرض الوامر 
/cmd
</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ المطور  ✨", url="https://t.me/PLO_erf")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>{name}
اهلن بيك عزيزي المستخدم {BL}</b>
اسعار vip في هذا البوت
سبوع-3دولار
شهر-5دولار
سنه-7دولار
سورس البوت-15دولار
للشراء @PLO_erf
لعرض الوامر 
/cmd
</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ المطور  ✨", url="https://t.me/PLO_erf")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>انت غير مشترك بل بوت او اتم ايقاف تفعيلك🪪</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	ko = (bot.reply_to(message, "جاري الفحص...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		response = requests.post(
		f'https://binlist.net/={cc}')
		last=(response.json()['result'])
		if 'result not found' in last:
			last='Authenticate Frictionless Failed'
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝙋𝙖𝙨𝙨𝙚𝙙 ✅
			
𝘾𝙖𝙧𝙙 >>>>>  <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 >>>>>  {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 >>>>>  {gate}		
𝙄𝙣𝙛𝙤 >>>>>  {card_type} - {brand}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 >>>>>  {country} - {country_flag} 
𝘽𝙞𝙣 >>>>>  {cc[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 >>>>>  {bank}
𝙏𝙞𝙢𝙚 >>>>>  {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @PLO_erf</b>'''
	msgd=f'''<b>𝗥𝗲𝗷𝗲𝗰𝘁𝗲𝗱 ❌
			
𝘾𝙖𝙧𝙙 >>>>>  <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 >>>>>  {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 >>>>>  {gate}		
𝙄𝙣𝙛𝙤 >>>>>  {card_type} - {brand}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 >>>>>  {country} - {country_flag} 
𝘽𝙞𝙣 >>>>>  {cc[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 >>>>>  {bank}
𝙏𝙞𝙢𝙚 >>>>>  {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @PLO_erf</b>'''
	if 'Authenticate Attempt Successful' in last or 'Authenticate Successful' in last or 'authenticate_successful' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'
print("تم تشغيل البوت")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"حدث خطأ: {e}")