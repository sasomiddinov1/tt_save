from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

check_button = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Подписаться на канал ✅', url='https://t.me/ttsave_says'),
                ],
        [
            InlineKeyboardButton(text='Проверить подписку 🔄', callback_data='check_subs')
        ],

    ]
)