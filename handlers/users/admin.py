from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from filters.admin import AdminFilter

admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.message(CommandStart())
async def admin_start(message: Message):
    welcome_message = [
        f"🔐 *Xush kelibsiz, {message.from_user.first_name or 'Admin'}!",
    ]


    await message.answer("\n".join(welcome_message), parse_mode="Markdown")