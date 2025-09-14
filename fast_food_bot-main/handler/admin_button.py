from aiogram.types import ReplyKeyboardMarkup,KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup
from database import get_foods
from aiogram.utils.keyboard import InlineKeyboardBuilder



admin_menu = ReplyKeyboardMarkup(
    keyboard=[
       
         [
            KeyboardButton(text="🧾 Buyurtmalar"),
            KeyboardButton(text="🍱 Menu")
        ],
        [
            KeyboardButton(text="👥 Foydalanuvchilar"),
            KeyboardButton(text="⚙️ Sozlamalar")
        ]
    
    ], 
    resize_keyboard= True,
    one_time_keyboard=True
)


order_button= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🆕 New")],
        [KeyboardButton(text="⏳ In Progress")],
        [KeyboardButton(text="✅ Finished")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True

)


def new_order_food(order_id):

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="❌ Cancel",callback_data=f"new_cancel_{order_id}"),
                InlineKeyboardButton(text="✅ In Progress",callback_data=f"new_send_{order_id}")]
        ]
    )

def progress_order_food(order_id):

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="❌ Cancel",callback_data=f"new_cancel_{order_id}"),
                InlineKeyboardButton(text="🏁 Finished",callback_data=f"progress_send_{order_id}")]
        ]
    )
    

admin_munu_text = """
✅ Siz muvaffaqiyatli Admin panelga kirdingiz!
Bu bo‘lim orqali siz quyidagi amallarni bajarishingiz mumkin:

🍔 Yangi taom qo‘shish

✏️ Taomlarni tahrirlash yoki o‘chirish

📊 Buyurtmalarni ko‘rish va boshqarish

👥 Foydalanuvchilarni kuzatish

⚙️ Iltimos, kerakli bo‘limni tanlang:"""
