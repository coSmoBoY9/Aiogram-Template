from loader import dp
from aiogram import types
from keyboards.default.amount import miqdorlar
from states.kafe import StatesKafe


@dp.message_handler(text="Sazan (300g)", state=StatesKafe.product)
async def get_menu(message: types.Message):
	await message.answer_photo(photo="https://ibb.co/dD5k1PQ", caption = "Sazan (300g)\n\nNarxi: 45000 so'm")
	await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼", reply_markup=miqdorlar)
	await StatesKafe.next()


@dp.message_handler(text="Sudak (300g)", state=StatesKafe.product)
async def get_menu(message: types.Message):
	await message.answer_photo(photo="https://ibb.co/c6bQbbv", caption = "Sudak (300g)\n\nNarxi: 48000 so'm")
	await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼", reply_markup=miqdorlar)
	await StatesKafe.next()


@dp.message_handler(text="Sous 300ml", state=StatesKafe.product)
async def get_menu(message: types.Message):
	await message.answer_photo(photo="https://ibb.co/HB6v52C", caption = "Sous 300ml\n\nNarxi: 7000 so'm")
	await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼", reply_markup=miqdorlar)
	await StatesKafe.next()



@dp.message_handler(text="Coca-Cola (1,5 L)", state=StatesKafe.product)
async def get_menu(message: types.Message):
	await message.answer_photo(photo="https://ibb.co/sV0V5sH", caption = "Coca-Cola (1,5 L)\n\nNarxi: 12000 so'm")
	await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼", reply_markup=miqdorlar)
	await StatesKafe.next()

@dp.message_handler(text="Fanta (1,5 L)", state=StatesKafe.product)
async def get_menu(message: types.Message):
	await message.answer_photo(photo="https://ibb.co/1zSQtGF", caption = "Fanta (1,5 L)\n\nNarxi: 12000 so'm")
	await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼", reply_markup=miqdorlar)
	await StatesKafe.next()


@dp.message_handler(text="Sprite (1,5 L)", state=StatesKafe.product)
async def get_menu(message: types.Message):
	await message.answer_photo(photo="https://ibb.co/NrCZ1Mb", caption = "Sprite (1,5 L)\n\nNarxi: 12000 so'm")
	await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼", reply_markup=miqdorlar)
	await StatesKafe.next()


@dp.message_handler(text="Мясо по-гречески", state=StatesKafe.product)
async def get_menu(message: types.Message):
	await message.answer_photo(photo="https://ibb.co/NrCZ1Mb", caption = "Мясо по-гречески\n\nNarxi: 28000 so'm")
	await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼", reply_markup=miqdorlar)
	await StatesKafe.next()
