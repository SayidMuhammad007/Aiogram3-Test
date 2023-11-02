from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from app.database.requests import *

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Katalog")
        ],
        [
            KeyboardButton(text="Kontakt")
        ]
    ], resize_keyboard=True, input_field_placeholder="Ttanlang"
)

async def categories():
    categories_kb = InlineKeyboardBuilder()
    categories = await get_categories()
    for category in categories:
        categories_kb.add(InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}"))
    return categories_kb.adjust(2).as_markup()

async def products(category_id):
    product_kb = InlineKeyboardBuilder()
    products = await get_products(category_id=category_id)
    for product in products:
        product_kb.add(InlineKeyboardButton(text=product.name, callback_data=f"product_{product.id}"))
    return product_kb.adjust(2).as_markup()