from aiogram import Router, F
from aiogram import types
from aiogram.filters import CommandStart

import app.keyboard.reply.btn as btn

router = Router()

@router.message(CommandStart())
async def cmd_start(message:types.Message):
    await message.answer("Hello", reply_markup=btn.main)

@router.message(F.text=="Katalog")
async def catalog(message:types.Message):
    await message.answer("Tanlang!", reply_markup=await btn.categories())

@router.callback_query(F.data.startswith("category_"))
async def category_selected(callback:types.CallbackQuery):
    category_id = callback.data.split('_')[1]
    await callback.message.answer(f"Tovarlar", reply_markup=await btn.products(category_id))

