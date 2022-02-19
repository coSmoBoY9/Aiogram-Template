from keyboards.default.baliq import baliqlar
from keyboards.default.ichimlik import Coke
from loader import dp
from aiogram import types
from states.kafe import StatesKafe
from aiogram.dispatcher import FSMContext


@dp.message_handler(state=StatesKafe.amount)
async def order(message: types.Message, state: FSMContext):
	amount = message.text
	await state.update_data({
		'amount': amount
	})
	data = await state.get_data()
	cat = data.get('cat')
	if cat == "Baliq 🐠":
		await message.answer("Savatchaga🛒 qo'shildi")
		await message.answer("Xo'sh davom etamizmi 😍?", reply_markup=baliqlar)
	elif cat == "Ichimliklar 🥤":
		await message.answer("Savatchaga🛒 qo'shildi")
		await message.answer("Xo'sh davom etamizmi 😍?", reply_markup=Coke)
	elif cat == "Ikkinchi ovqatlar 🍛":
		pass
	await StatesKafe.product.set()