from aiogram.types import Message,ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from database.query import is_register
from .buttons import register_kb,phone_kb,reg_text,location_kb
from .filters import check_phone,check_uzb_location

user_router = Router()

class Register(StatesGroup):
    fullname=State()
    phone=State()
    location=State()   
    

@user_router.message(CommandStart())
async def start(message: Message):
    if is_register(message.from_user.id) is None:
    
        await message.answer(text=reg_text,reply_markup=register_kb )
    else:
        await message.answer("Siz avval royhatdan otgansiz")

@user_router.message(F.text=="Register")   
async def register_handler(message:Message,state:FSMContext):
    await state.set_state(Register.fullname)
    
    await  message.answer("F.I.SH kirting",reply_markup=ReplyKeyboardRemove())
    
@user_router.message(Register.fullname)
async def get_fullname(message:Message,state:FSMContext):
        await state.update_data(fullname=message.text)
        await state.set_state(Register.phone)
        
        await message.answer("Telefon raqamingizni kirting",reply_markup=phone_kb)        
        
@user_router.message(Register.phone)
async def get_phone(message:Message,state:FSMContext):
    if message.contact or check_phone(message.text):
        if message.contact:
            phone=message.contact.phone_number
        else:
            phone=message.text
            
        await state.update_data(phone=phone)
        await  state.set_state(Register.location) 
        await message.answer("Location yuboring: ",reply_markup=location_kb)   
    else:
        await message.answer("Telefon raqam notogri kirtldi",reply_markup=phone_kb)
           
       
  
  
@user_router.message(Register.location)
async def get_loction(message:Message,state:FSMContext):
                if message.location:
                   if check_uzb_location(message.location.latitude,message.location.longitude):
                        await message.answer("Registratsiya muvofaqiyatli ")
                else:
                     await message.answer("Menyu orqali yuboring",reply_markup=location_kb)         