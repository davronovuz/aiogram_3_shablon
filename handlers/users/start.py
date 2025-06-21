from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

user_router = Router()

@user_router.message(CommandStart())
async def user_start(message: Message):
    welcome_message = (
        "🎉 Salom, {username}! Botimizga xush kelibsiz! 😊\n"
        "Bu yerda sizga ko‘plab qiziqarli imkoniyatlar taqdim etamiz.\n"
        "🔥 Boshlash uchun /help buyrug‘ini sinab ko‘ring!"
    ).format(username=message.from_user.full_name or "do‘st")
    await message.reply(welcome_message)