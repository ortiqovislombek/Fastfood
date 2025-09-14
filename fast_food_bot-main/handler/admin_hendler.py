from aiogram.types import Message,CallbackQuery
from aiogram.filters import Command
from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup,State

from database import is_admin,is_new_foods,is_progress_foods,update_order
from .buttons import register_kb
from .admin_button import admin_munu_text,admin_menu,order_button,new_order_food,progress_order_food


admin_router = Router()


@admin_router.message(Command("admin"))
async def start_admin(message:Message):
    chat_id = message.from_user.id

    user = is_admin(chat_id)

    if user:
        if user[-1]:
           
           await message.answer(text=admin_munu_text,reply_markup=admin_menu)
        else:
            await message.answer("Siz admin emassiz!!! 🙃")
    else:

        await message.answer("Siz Ro'yhatdan o'tmagansiz, Ro'yhatdan o'ting: ",reply_markup=register_kb)


@admin_router.message(F.text =="🧾 Buyurtmalar")
async def show_order(message: Message):
    text="""📦 Buyurtmalar bo‘limi:\nKerakli turini tanlang 👇"""

    await message.answer(text=text,reply_markup=order_button)


@admin_router.message(F.text =="🆕 New")
async def new_order(message:Message):
    foods = is_new_foods()

    for i in foods:
        await message.answer(
                text=f"🍽 Taom: {i[1]}\n"
                     f"👤 Foydalanuvchi: {i[2]}\n"
                     f"📦 Miqdor: {i[3]} ta\n"
                     f"💵 Narx: {i[4]} so'm\n"
                     f"💵 Umumiy narx: {i[5]:,} so‘m\n"
                     f"🆕 New\n",
                     reply_markup=new_order_food(i[0])
            )



@admin_router.message(F.text =="⏳ In Progress")
async def progress_order(message:Message):
    foods = is_progress_foods()

    for i in foods:
        await message.answer(
                text=f"🍽 Taom: {i[1]}\n"
                     f"👤 Foydalanuvchi: {i[2]}\n"
                     f"📦 Miqdor: {i[3]} ta\n"
                     f"💵 Narx: {i[4]} so'm\n"
                     f"💵 Umumiy narx: {i[5]:,} so‘m\n"
                     f"🆕 In Progress\n",
                     reply_markup=progress_order_food(i[0])
            )


@admin_router.callback_query(F.data.startswith("new_cancel"))
async def cancel_order(call:CallbackQuery):
    order_id = int(call.data.split("_")[-1])
    update_order(order_id)
  
    

    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.edit_text(text="success")


    
  




