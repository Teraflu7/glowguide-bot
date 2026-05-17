import json
import os
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from bot.keyboards import main_keyboard

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


def load_skincare_data():
    try:
        with open("data/skincare.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: skincare.json not found")
        return {}
    except json.JSONDecodeError:
        print("Error: skincare.json has invalid format")
        return {}


skincare_data = load_skincare_data()


@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "Привет! ✨\n"
        "Я GlowGuide Bot.\n"
        "Выбери свой тип кожи 💖",
        reply_markup=main_keyboard
    )


@dp.message()
async def skin_type_handler(message: Message):
    text = message.text.lower()

    if "сух" in text:
        skin = skincare_data.get("dry")
    elif "жир" in text:
        skin = skincare_data.get("oily")
    elif "норм" in text:
        skin = skincare_data.get("normal")
    elif "комби" in text:
        skin = skincare_data.get("combination")
    elif "чувств" in text:
        skin = skincare_data.get("sensitive")
    else:
        await message.answer("Пожалуйста, выбери тип кожи с помощью кнопок 💖")
        return

    if not skin:
        await message.answer("Данные для этого типа кожи не найдены.")
        return

    response = (
        f"✨ {skin['name']}\n\n"
        f"📖 {skin['description']}\n\n"
        f"✅ Рекомендуется:\n- " + "\n- ".join(skin["recommended"]) +
        "\n\n❌ Избегать:\n- " + "\n- ".join(skin["avoid"]) +
        "\n\n🌞 Утренний уход:\n- " + "\n- ".join(skin["morning"]) +
        "\n\n🌙 Вечерний уход:\n- " + "\n- ".join(skin["evening"]) +
        "\n\n💡 Советы:\n- " + "\n- ".join(skin.get("tips", []))
    )

    await message.answer(response)


async def main():
    print("Bot started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())