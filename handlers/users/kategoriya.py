from loader import dp
from aiogram import types
from keyboards.default.baliq import baliqlar
from keyboards.default.ichimlik import Coke
from states.kafe import StatesKafe
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="Baliq 🐠", state=StatesKafe.category)
async def get_fish(message: types.Message, state: FSMContext):
	cat = message.text
	await state.update_data(
		{'cat': cat}
	)
	await message.answer("Batafsil ma'lumot uchun taomni tanlang", reply_markup=baliqlar)
	await StatesKafe.next()

@dp.message_handler(text="Ichimliklar 🥤", state=StatesKafe.category)
async def get_coke(message:types.Message, state: FSMContext):
	cat = message.text
	await state.update_data(
		{'cat': cat}
	)
	await message.answer("Batafsil ma'lumot uchun ichimlikni tanlang", reply_markup=Coke)
	await StatesKafe.next()