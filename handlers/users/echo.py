from aiogram import types, Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hcode

echo_router = Router()

@echo_router.message(F.text, StateFilter(None))
async def bot_echo(message: types.Message):
    """
    Foydalanuvchi hech qanday holatda (state) bo‘lmaganda yuborgan matnli xabarga javob beradi.
    Xabar foydalanuvchining yuborgan matnini qaytaradi.
    """
    text = [
        "🎈 Salom Siz hech qanday holatda emassiz!",
        "📩 Sizning xabaringiz:",
        f"{hcode(message.text)}"
    ]
    await message.answer("\n".join(text), parse_mode="Markdown")

@echo_router.message(F.text)
async def bot_echo_all(message: types.Message, state: FSMContext):
    """
    Foydalanuvchi biron holatda (state) bo‘lganda yuborgan matnli xabarga javob beradi.
    Xabar foydalanuvchining holatini va yuborgan matnini ko‘rsatadi.
    """
    state_name = await state.get_state() or "Noma'lum"
    text = [
        f" Salom! Siz hozir {hcode(state_name)} holatidasiz!",
        "📬 Sizning xabaringiz:",
        f"{hcode(message.text)}"
    ]
    await message.answer("\n".join(text), parse_mode="Markdown")