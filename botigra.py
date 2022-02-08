import json
import telebot
import types
import random

##Это дз по спецкурсу - телеграм-бот с игрой в наперстки.Ссылка на него - https://t.me/oldmangamebot
##Для работы программы нужно pipoм установить модуль pyTelegramBotAPI
##Имя только буквенное, т.к. я плохо знаю, как в строке распознавать буквы(если можете с этим помочь, то, пожалуйста,помогите)
##Также бот пока не работает с JSON-файлом, т.к. я почему-то никак не могу понять, как нормально загружать данные типа {user_id: { 'Name': ... , 'Balance': ..., 'Balance of old man': ...} } в него и как доставать из него такие же данные, чтобы их изменять(помогите пж с этим)

bot = telebot.TeleBot('5257196019:AAHKVEF_a-XbvAPNxzWznnSoPi8w8g1kmZI')

x = 5500
y = 0
z = 0
l = 0
vrot = 'Деньги поставлены !'
rarkup = telebot.types.InlineKeyboardMarkup()
rarkup.add(telebot.types.InlineKeyboardButton(text = 'Начнем же игру !', callback_data = 'igra'))

@bot.message_handler(commands = ['start'])
def welcome_message(message):
  ##with open('users.json') as users_data:
    ##data = json.load(users_data)
  ##if str(message.chat.id) in data:
    ##bot.send_message(message.chat.id, 'Снова приветствую тебя ,')
  ##else:
  markup = telebot.types.InlineKeyboardMarkup()
  markup.add(telebot.types.InlineKeyboardButton(text = 'Да, хочу (Зарегистрироваться)', callback_data = 1))
  markup.add(telebot.types.InlineKeyboardButton(text = 'Расскажи мне побольше про эту игру', callback_data = 2))
  bot.send_message(message.chat.id, 'Здравствуй, путник, хочешь сыграть в игру 🃏?', reply_markup = markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
	
	global rarkup
	global vrot
	global x
	global y
	global z
	
	varkup = telebot.types.InlineKeyboardMarkup()
	jom = telebot.types.InlineKeyboardButton(text = 'Играть снова', callback_data = 4)
	hom = telebot.types.InlineKeyboardButton(text = 'Проверить кошель', callback_data = 3)
	varkup.row(jom, hom)
	bot.answer_callback_query(callback_query_id =call.id, text = 'Action done')
	answer = ' '
	if call.data == '1':
		answer = 'Отлично..Присаживайся и скажи мне своё имя(Только буквенное)'
		bot.send_message(call.message.chat.id, answer)
	if call.data == '2':
		answer = 'Игра очень проста: ты ставишь свои деньги на то,что угадаешь,где находится монетка, и если угадываешь, то сумма твоя удваивается. Однако если ты не угадаешь, я забираю все деньги себе.Ну что же, сыграем ?'
		makeup = telebot.types.InlineKeyboardMarkup()
		makeup.add(telebot.types.InlineKeyboardButton(text = 'Давай! ', callback_data = 1))
		bot.send_message(call.message.chat.id, answer, reply_markup = makeup)
	if call.data == '3':
		otv = 'В кошеле лежит ' + str(x)+ ' $'
		jarkup = telebot.types.InlineKeyboardMarkup()
		jarkup.add(telebot.types.InlineKeyboardButton(text = 'Показать их старцу', callback_data = 4))
		bot.send_message(call.message.chat.id, otv, reply_markup = jarkup)
	if call.data == '4':
		vet = ' '
		garkup = telebot.types.InlineKeyboardMarkup(row_width = 2)
		a = telebot.types.InlineKeyboardButton(text = '10 $', callback_data = 5)
		b = telebot.types.InlineKeyboardButton(text = '50 $', callback_data = 6)
		c = telebot.types.InlineKeyboardButton(text = '100 $', callback_data = 7)
		d = telebot.types.InlineKeyboardButton(text = '200 $', callback_data = 8)
		e = telebot.types.InlineKeyboardButton(text = '300 $', callback_data = 9)
		f = telebot.types.InlineKeyboardButton(text = '400 $', callback_data = 10)
		g = telebot.types.InlineKeyboardButton(text = '500 $', callback_data = 11)
		h = telebot.types.InlineKeyboardButton(text = '1000 $', callback_data = 12)
		i = telebot.types.InlineKeyboardButton(text = '2000 $', callback_data = 13)
		k = telebot.types.InlineKeyboardButton(text = '3000 $', callback_data = 14)
		j = telebot.types.InlineKeyboardButton(text = '4000 $', callback_data = 15)
		l = telebot.types.InlineKeyboardButton(text = '5000 $', callback_data = 16)
		m = telebot.types.InlineKeyboardButton(text = 'Назову сумму сам', callback_data = 17)
		n = telebot.types.InlineKeyboardButton(text = 'Все мои деньги !', callback_data = 18)
		garkup.row(a, b, c, d, e, f)
		garkup.row(g,h,i,k,j,l)
		garkup.row(m, n)
		if x != 0:
			if x > 5500:
				vet = 'Ого, я смотрю ты уже подзаработал! Сколько хочешь поставить в этот раз ?'
			if x == 5500:
				vet = 'Отлично, ровно столько, сколько нужно. Сколько хочешь поставить в этот раз ?'
			if x < 5500 and x > 10:
				vet = 'Я думаю, этих денег тебе хватит.Сколько хочешь поставить в этот раз ?'
			bot.send_message(call.message.chat.id,vet, reply_markup = garkup)
		else:
			vet = 'Прости, но у тебя недостаточно денег для игры'
			bot.send_message(call.message.chat.id,vet)
	if call.data == '5':
		z = 10
		x -= z
		y += z
		bot.send_message(call.message.chat.id, vrot, reply_markup = rarkup)
	if call.data == '6':
		z = 50
		x -= z
		y += z
		bot.send_message(call.message.chat.id, vrot, reply_markup = rarkup)
		
	if call.data == '7':
		z = 100
		x -= z
		y += z
		bot.send_message(call.message.chat.id, vrot, reply_markup = rarkup)
		
	if call.data == '8':
		z = 200
		x -= z
		y += z
		bot.send_message(call.message.chat.id, vrot, reply_markup = rarkup)
		
	if call.data == '9':
		z = 300
		x -= z
		y += z
		bot.send_message(call.message.chat.id, vrot, reply_markup = rarkup)
		
	if call.data == '10':
		z = 400
		x -= z
		y += z
		bot.send_message(call.message.chat.id, vrot, reply_markup = rarkup)
		
	if call.data == '11':
		z = 500
		x -= z
		y += z
		bot.send_message(call.message.chat.id, vrot, reply_markup = rarkup)
		
	if call.data == '12':
		z = 1000
		x -= z
		y += z
		bot.send_message(call.message.chat.id, vrot, reply_markup = rarkup)
		
	if call.data == '13':
		z = 2000
		x -= z
		y += z
		bot.send_message(call.message.chat.id, vrot, reply_markup = rarkup)
		
	if call.data == '14':
		z = 3000
		x -= z
		y += z
		bot.send_message(call.message.chat.id, vrot, reply_markup = rarkup)
		
	if call.data == '15':
		z = 4000
		x -= z
		y += z
		bot.send_message(call.message.chat.id, vrot, reply_markup = rarkup)
		
	if call.data == '16':
		z = 5000
		x -= z
		y += z
		bot.send_message(call.message.chat.id, vrot, reply_markup = rarkup)
		
	if call.data == '17':
		bot.send_message(call.message.chat.id, 'Напишите сумму, которую хотите поставить')
	if call.data == '18':
		bot.send_message(call.message.chat.id,'Вау, ты смел и азартен')
		z = x
		y += z
		x -= z
		bot.send_message(call.message.chat.id, vrot, reply_markup = rarkup)
		##bot.send_message(call.message.chat.id, vrot, reply_markup = rarkup)
		
	if call.data == 'igra':
		bot.send_message(call.message.chat.id, '*Старец крутит наперстки*')
		carkup = telebot.types.InlineKeyboardMarkup()
		nom1 = telebot.types.InlineKeyboardButton(text = 'Первый наперсток', callback_data = random.randint(19,20))
		nom2 = telebot.types.InlineKeyboardButton(text = 'Второй наперсток', callback_data = random.randint(19,20))
		nom3 = telebot.types.InlineKeyboardButton(text = 'Третий наперсток', callback_data = random.randint(19,20))
		carkup.row(nom1, nom2, nom3)
		bot.send_message(call.message.chat.id, "Выбери наперсток", reply_markup = carkup)
		
	if call.data == '19':
		bot.send_message(call.message.chat.id, '*Под наперстком пусто* Мне жаль, но ты проиграл. Хочешь сыграть снова ?', reply_markup = varkup)
		
	if call.data == '20':
		bot.send_message(call.message.chat.id,'*Под наперстком монетка* Что же,поздравляю, ты выиграл. Хочешь сыграть снова ?')
		y -= 2*z
		x += 2*z
		sh = 'Баланс увеличился на ' + str(2*z) + '$'
		bot.send_message(call.message.chat.id, sh, reply_markup = varkup)
		
@bot.message_handler(content_types = ['text'])
def text_handle(message):
	global x
	global y
	global z
	global l
	global vrot
	global rarkup
	global vpok
	if l == 1:
		if any(map(str.isdigit, message.text)):
			if int(message.text) > 10:
				z = int(message.text)
				x -= z
				y += z
				vpok = 'С баланса снялось '+ str(z)+ '$'
				bot.send_message(message.chat.id, vrot, reply_markup = rarkup)
				bot.send_message(message.chat.id, vpok)
			elif int(message.text) > 0:
				bot.send_message(message.chat.id, 'Введена сумма меньше минимальной ставки, напишите новую сумму')
			else:
				bot.send_message(message.chat.id, 'Ставка не может быть отрицательной, напишите новую сумму')
			
	if l == 0:
		data_of_user = {str(message.chat.id): {'Name': message.text, 'Balance': x, 'Balance of Old man': y}}
		json.dumps(data_of_user)
		tes = 'Хорошо, ' + message.text + ', теперь проверь свой кошель, там должны были остаться деньги'
		mukeup = telebot.types.InlineKeyboardMarkup()
		mukeup.add(telebot.types.InlineKeyboardButton(text = 'Проверить кошель', callback_data = 3))
		bot.send_message(message.chat.id, tes,reply_markup = mukeup)
		l += 1
		
		
bot.infinity_polling()