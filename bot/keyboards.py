from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
keyboard=[
[
KeyboardButton(text="💧 Сухая кожа"),
KeyboardButton(text="✨ Жирная кожа")
],
[
KeyboardButton(text="🌿 Нормальная кожа"),
KeyboardButton(text="🌗 Комбинированная кожа")
],
[
KeyboardButton(text="🌸 Чувствительная кожа")
]
],
resize_keyboard=True
)