from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import get_foods
from aiogram.utils.keyboard import InlineKeyboardBuilder

register_kb=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Register")]
        
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

phone_kb=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Phone",request_contact=True)]
        
    ],
    resize_keyboard=True,
    one_time_keyboard=True
) 
location_kb=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Location",request_location=True)]
        
    ],
    resize_keyboard=True,
    one_time_keyboard=True
) 

main_button = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋 Menu"), KeyboardButton(text="🛒 Buyurtmalar")],
            [KeyboardButton(text="📞 Aloqa"), KeyboardButton(text="⚙️ Sozlamalar")],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

def puls_minus_button(food_id, quantity=1):

    buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="➖",callback_data=f"minus_{quantity}_{food_id}"),
             InlineKeyboardButton(text=f"{quantity}",callback_data=f"quantity_{quantity}"),
             InlineKeyboardButton(text="➕",callback_data=f"plus_{quantity}_{food_id}")],
             [InlineKeyboardButton(text="↩️",callback_data="cancel_food"),
                InlineKeyboardButton(text="⏩",callback_data=f"next_food_{quantity}_{food_id}")]

            
        ]
    )
    return buttons


async def food_button():

    buttons = InlineKeyboardBuilder()

    for i in get_foods():
        buttons.add(InlineKeyboardButton(text=i[1],callback_data=f"food_{i[0]}"))
    return buttons.adjust(1).as_markup()

reg_text=(
         """
        Assalomu alaykum! 🍔
        Ro‘yxatdan o‘tish uchun quyidagi maʼlumotlarni yuboring:
        1) Ismingiz
        2) Telefon raqamingiz (📞)
        3) Yetkazib berish manzilingiz (📍)

        Barchasi tayyor bo‘lsa, davom etamiz!
        
        """
)
menu_text="""
       

        ✅ Siz muvaffaqiyatli ro‘yxatdan o‘tdingiz!

📋 Menu  
🍔🍕🥤 Barcha taomlar va ichimliklarni ko‘rish  

🛒 Order  
🧾 Buyurtma berish va savatni ko‘rish  

📞 Contact  
📲 Biz bilan bog‘lanish  

⚙️ Settings  
🌐 Til va boshqa sozlamalarni o‘zgartirish  

😋 Endi ochlikni yengish vaqti!

"""

admin_text="""
            📞 Biz bilan bog‘lanish

📲 Telefon: +998 99 235 55 55
✉️ Telegram: @islombek_ortiqov
📍 Manzil: Toshkent shahri, Chilonzor tumani, FastFood ko‘chasi 10-uy

⏰ Ish vaqti: 09:00 — 23:00
🍔 Buyurtmangizni tez va sifatli yetkazib beramiz!



    """



