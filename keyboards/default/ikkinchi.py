from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ikki = ReplyKeyboardMarkup(
	keyboard=[
		[KeyboardButton(text="Мясо по-гречески"), KeyboardButton(text="Мясо по-французски")],
		[KeyboardButton(text="Бифштекс"), KeyboardButton(text="ORQAGA ↩️")],
		[KeyboardButton(text="Bosh Sahifa 🏠")]
	],
	resize_keyboard=True
)
