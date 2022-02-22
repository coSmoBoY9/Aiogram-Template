from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cats = ReplyKeyboardMarkup(
	keyboard=[
		[KeyboardButton(text="Baliq 🐠"), KeyboardButton(text="Ichimliklar 🥤")],
		[KeyboardButton(text="Ikkinchi ovqatlar 🍛"), KeyboardButton(text="ORQAGA ↩️")]
	],
	resize_keyboard=True
)
wolves = ReplyKeyboardMarkup(
	keyboard=[
		[KeyboardButton(text="Coca-Cola (1,5 L)"), KeyboardButton(text="Fanta (1,5 L)")],
		[KeyboardButton(text="Sprite (1,5 L)"), KeyboardButton(text="ORQAGA ↩️")]
],
	resize_keyboard=True
)
foxes = ReplyKeyboardMarkup(
	keyboard=[
		[KeyboardButton(text="Мясо по-гречески"), KeyboardButton(text="Мясо по-французски")],
		[KeyboardButton(text="Бифштекс"), KeyboardButton(text="ORQAGA ↩️")],
],
	resize_keyboard=True
)