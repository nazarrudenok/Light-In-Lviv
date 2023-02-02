import telebot
from telebot import types


bot = telebot.TeleBot('5822637815:AAGMVou-RLR-Hku-8-w8vwJTkg62s3OEwy0')

@bot.message_handler(commands = ['start', 'starting'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	first_group = types.KeyboardButton(text = '1️⃣')
	second_group = types.KeyboardButton(text = '2️⃣')
	third_group = types.KeyboardButton(text = '3️⃣')
	markup.add(first_group, second_group, third_group)

	bot.send_message(message.chat.id, 'Вітаю! Оберіть свою групу', reply_markup = markup)

@bot.message_handler(content_types = ['text'])
def text(message):
	if message.text == '1️⃣':
		markup2 = types.ReplyKeyboardMarkup(resize_keyboard = True)
		Monday = types.KeyboardButton(text = 'понеділок')
		Tuesday = types.KeyboardButton(text = 'вівторок')
		Wensday = types.KeyboardButton(text = 'середа')
		Thursday = types.KeyboardButton(text = 'Четвер')
		Friday = types.KeyboardButton(text = "п'ятниця")
		Saturday = types.KeyboardButton(text = 'субота')
		Sunday = types.KeyboardButton(text = 'неділя')
		markup2.add(Monday, Tuesday, Wensday, Thursday, Friday, Saturday, Sunday)

		bot.send_message(message.chat.id, 'Оберіть день тижня', reply_markup = markup2)
	if message.text == 'понеділок':
		bot.send_message(message.chat.id, 'Є енергія: з 5:00 по 9:00 та з 17:00 по 21:00\nНемає енергії: з 1:00 по 5:00 та з 13:00 по 17:00\nМожливе відключення: з 9:00 по 13:00 та з 21:00 по 1:00')
	elif message.text == 'вівторок':
		bot.send_message(message.chat.id, 'Є енергія: з 1:00 по 5:00 та з 13:00 по 17:00\nНемає енергії: з 9:00 по 13:00 та з 21:00 по 1:00\nМожливе відключення: з 5:00 по 9:00 та з 17:00 по 21:00')
	elif message.text == 'середа':
		bot.send_message(message.chat.id, 'Є енергія: з 9:00 по 13:00 та з 21:00 по 1:00\nНемає енергії: з 5:00 по 9:00 та з 17:00 по 21:00\nМожливе відключення: з 1:00 по 5:00 та з 13:00 по 17:00')
	elif message.text == 'четвер':
		bot.send_message(message.chat.id, 'Є енергія: з 5:00 по 9:00 та з 17:00 по 21:00\nНемає енергії: з 1:00 по 5:00 та з 13:00 по 17:00\nМожливе відключення: з 9:00 по 13:00 та з 21:00 по 1:00')
	elif message.text == "п'ятниця":
		bot.send_message(message.chat.id, 'Є енергія: з 1:00 по 5:00 та з 13:00 по 17:00\nНемає енергії: з 9:00 по 13:00 та з 21:00 по 1:00\nМожливе відключення: з 5:00 по 9:00 та з 17:00 по 21:00')
	elif message.text == 'субота':
		bot.send_message(message.chat.id, 'Є енергія: з 9:00 по 13:00 та з 21:00 по 1:00\nНемає енергії: з 5:00 по 9:00 та з 17:00 по 21:00\nМожливе відключення: з 1:00 по 5:00 та з 13:00 по 17:00')
	elif message.text == 'неділя':
		bot.send_message(message.chat.id, 'Є енергія: з 5:00 по 9:00 та з 17:00 по 21:00\nНемає енергії: з 1:00 по 5:00 та з 13:00 по 17:00\nМожливе відключення: з 9:00 по 13:00 та з 21:00 по 1:00')


	if message.text == '2️⃣':
		markup3 = types.ReplyKeyboardMarkup(resize_keyboard = True)
		Monday = types.KeyboardButton(text = 'Пoнеділок')
		Tuesday = types.KeyboardButton(text = 'Вiвторок')
		Wensday = types.KeyboardButton(text = 'Сeреда')
		Thursday = types.KeyboardButton(text = 'Чeтвер')
		Friday = types.KeyboardButton(text = "П`ятниця")
		Saturday = types.KeyboardButton(text = 'Сyбота')
		Sunday = types.KeyboardButton(text = 'Недiля')
		markup3.add(Monday, Tuesday, Wensday, Thursday, Friday, Saturday, Sunday)

		bot.send_message(message.chat.id, 'Оберіть день тижня', reply_markup = markup3)
	if message.text == 'Пoнеділок':
		bot.send_message(message.chat.id, 'Є енергія: з 1:00 по 5:00 та з 13:00 по 17:00\nНемає енергії: з 9:00 по 13:00 та з 21:00 по 1:00\nМожливе відключення: з 5:00 по 9:00 та з 17:00 по 21:00')
	elif message.text == 'Вiвторок':
		bot.send_message(message.chat.id, 'Є енергія: з 9:00 по 13:00 та з 21:00 по 1:00\nНемає енергії: з 5:00 по 9:00 та з 17:00 по 21:00\nМожливе відключення: з 1:00 по 5:00 та з 13:00 по 17:00')
	elif message.text == 'Сeреда':
		bot.send_message(message.chat.id, 'Є енергія: з 5:00 по 9:00 та з 17:00 по 21:00\nНемає енергії: з 1:00 по 5:00 та з 13:00 по 17:00\nМожливе відключення: з 9:00 по 13:00 та з 21:00 по 1:00')
	elif message.text == 'Чeтвер':
		bot.send_message(message.chat.id, 'Є енергія: з 1:00 по 5:00 та з 12:00 по 17:00\nНемає енергії: з 9:00 по 13:00 та з 21:00 по 1:00\nМожливе відключення: з 5:00 по 9:00 та з 17:00 по 21:00')
	elif message.text == "П`ятниця":
		bot.send_message(message.chat.id, 'Є енергія: з 9:00 по 13:00 та з 21:00 по 1:00\nНемає енергії: з 5:00 по 9:00 та з 17:00 по 21:00\nМожливе відключення: з 1:00 по 5:00 та з 13:00 по 17:00')
	elif message.text == 'Сyбота':
		bot.send_message(message.chat.id, 'Є енергія: з 5:00 по 9:00 та з 17:00 по 21:00\nНемає енергії: з 1:00 по 5:00 та з 13:00 по 17:00\nМожливе відключення: з 9:00 по 13:00 та з 21:00 по 1:00')
	elif message.text == 'Недiля':
		bot.send_message(message.chat.id, 'Є енергія: з 1:00 по 5:00 та з 13:00 по 17:00\nНемає енергії: з 9:00 по 13:00 та з 21:00 по 1:00\nМожливе відключення: з 5:00 по 9:00 та з 17:00 по 21:00')

	if message.text == '3️⃣':
		markup4 = types.ReplyKeyboardMarkup(resize_keyboard = True)
		Monday = types.KeyboardButton(text = 'Пoнеділoк')
		Tuesday = types.KeyboardButton(text = 'Вiвтоpoк')
		Wensday = types.KeyboardButton(text = 'Сeредa')
		Thursday = types.KeyboardButton(text = 'Чeтвеp')
		Friday = types.KeyboardButton(text = "П'ятниця")
		Saturday = types.KeyboardButton(text = 'Сyботa')
		Sunday = types.KeyboardButton(text = 'Нeдiля')
		markup4.add(Monday, Tuesday, Wensday, Thursday, Friday, Saturday, Sunday)

		bot.send_message(message.chat.id, 'Оберіть день тижня', reply_markup = markup4)
	if message.text == 'Пoнеділoк':
		bot.send_message(message.chat.id, 'Є енергія: з 9:00 по 13:00 та з 21:00 по 1:00\nНемає енергії: з 5:00 по 9:00 та з 17:00 по 21:00\nМожливе відключення: з 1:00 по 5:00 та з 13:00 по 17:00')
	elif message.text == 'Вiвтоpoк':
		bot.send_message(message.chat.id, 'Є енергія: з 5:00 по 9:00 та з 17:00 по 21:00\nНемає енергії: з 1:00 по 5:00 та з 13:00 по 17:00\nМожливе відключення: з 9:00 по 13:00 та з 21:00 по 1:00')
	elif message.text == 'Сeредa':
		bot.send_message(message.chat.id, 'Є енергія: з 1:00 по 5:00 та з 13:00 по 17:00\nНемає енергії: з 9:00 по 13:00 та з 21:00 по 1:00\nМожливе відключення: з 5:00 по 9:00 та з 17:00 по 21:00')
	elif message.text == 'Чeтвеp':
		bot.send_message(message.chat.id, 'Є енергія: з 9:00 по 13:00 та з 21:00 по 1:00\nНемає енергії: з 5:00 по 9:00 та з 17:00 по 21:00\nМожливе відключення: з 1:00 по 5:00 та з 13:00 по 17:00')
	elif message.text == "П'ятниця":
		bot.send_message(message.chat.id, 'Є енергія: з 5:00 по 9:00 та з 17:00 по 21:00\nНемає енергії: з 1:00 по 5:00 та з 13:00 по 17:00\nМожливе відключення: з 9:00 по 13:00 та з 21:00 по 1:00')
	elif message.text == 'Сyботa':
		bot.send_message(message.chat.id, 'Є енергія: з 1:00 по 5:00 та з 13:00 по 17:00\nНемає енергії: з 9:00 по 13:00 та з 21:00 по 1:00\nМожливе відключення: з 5:00 по 9:00 та з 17:00 по 21:00')
	elif message.text == 'Нeдiля':
		bot.send_message(message.chat.id, 'Є енергія: з 9:00 по 13:00 та з 21:00 по 1:00\nНемає енергії: з 5:00 по 9:00 та з 17:00 по 21:00\nМожливе відключення: з 1:00 по 5:00 та з 13:00 по 17:00')

bot.polling(none_stop = True)
