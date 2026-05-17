from aiogram.filters import Command
from aiogram.types import Message

# Future handlers for GlowGuide Bot

async def start_message(message: Message):
    await message.answer(
        "Привет! ✨\n"
        "Выбери тип кожи ниже 💖"
    )
    async def help_message(message: Message):
        await message.answer(
"GlowGuide Bot ✨\n\n"
"Используй кнопки, чтобы выбрать тип кожи 💖\n\n"
"Бот показывает:\n"
"- skincare рекомендации\n"
"- утренний уход\n"
"- вечерний уход\n"
"- полезные советы"
)