from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove


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