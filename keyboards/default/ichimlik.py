from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Coke = ReplyKeyboardMarkup(
	keyboard=[
		[KeyboardButton(text="Coca-Cola (1,5 L)"), KeyboardButton(text="Fanta (1,5 L)")],
		[KeyboardButton(text="Sprite (1,5 L)"), KeyboardButton(text="ORQAGA ↩️")]
	],
	resize_keyboard=True
)
