from aiogram.filters import Command
from aiogram.types import Message

# Future handlers for GlowGuide Bot

async def start_message(message: Message):
    await message.answer(
        "Привет! ✨\n"
        "Выбери тип кожи ниже 💖"
    )