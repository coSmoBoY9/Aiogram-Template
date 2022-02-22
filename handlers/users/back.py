
from keyboards.default.ikkinchi import ikki
from loader import dp
from aiogram import types
from states.kafe import StatesKafe
from keyboards.default.asosiy import menu
from keyboards.default.category import cats, wolves
from keyboards.default.baliq import baliqlar
from keyboards.default.ichimlik import Coke
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="ORQAGA ↩️", state=StatesKafe.category)
async def back_cat(message: types.Message, state: FSMContext):
	await message.answer("Sahifani tanlang 😊", reply_markup=menu)
	await state.finish()

@dp.message_handler(text="ORQAGA ↩️", state=StatesKafe.product)
async def back_prod(message: types.Message):
	await message.answer("Taomlarga o'tish uchun sahifani tanlang...", reply_markup=cats)
	await StatesKafe.category.set()

@dp.message_handler(text="ORQAGA ↩️", state=StatesKafe.amount)
async def back_amount(message: types.Message, state: FSMContext):
	data = await state.get_data()
	cat = data.get('cat')
	if cat == "Baliq 🐠":
		await message.answer("Batafsil ma'lumot uchun taomni tanlang", reply_markup=baliqlar)
	elif cat == "Ichimliklar 🥤":
		await message.answer("Batafsil ma'lumot uchun taomni tanlang", reply_markup=Coke)
	elif cat == "Ikkinchi ovqatlar 🍛":
		await message.answer("Batafsil ma'lumot uchun taomni tanlang", reply_markup=ikki)
	await StatesKafe.product.set()
	
@dp.message_handler(text="Bosh Sahifa 🏠", state=StatesKafe)
async def back_amount(message: types.Message, state: FSMContext):
	await message.answer("Buyurtma berishni boshlaymizmi?", reply_markup=menu)
	await state.finish()
