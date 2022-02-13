from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import CHANNELS
from keyboards.inline.obuna_tugmasi import check_button
from utils.misc import obuna_kanal
from loader import dp, db, bot
import sqlite3
from data.config import ADMINS

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)

    channels_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        # logging.info(invite_link)
        channels_format += f'👉🏻 <a href="{invite_link}">{chat.title}</a>\n'
    await message.answer(f"<b>Пожалуйста, подпишись на наш канал, мы для вас \n стараемся.</b>\n"' \n'"Поддержите подпиской на канал и затем нажмите кнопку «Проверить подписку 🔄» чтобы получить видео."
                         f'{channels_format}',
                         reply_markup=check_button,
                         disable_web_page_preview=True
                         )


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await obuna_kanal.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"<b>{channel.title}</b> kanaliga obuna bo'lgansiz✅\n\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"<b>{channel.title}</b> kanaliga obuna bo'lmagansiz🚫 "
                       f"<a href='{invite_link}'>Obuna bo'ling)</a>\n\n")

    await call.message.answer(result, disable_web_page_preview=True)





#
# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     name = message.from_user.full_name
#     # Foydalanuvchini bazaga qo'shamiz
#     try:
#         db.add_user(id=message.from_user.id,
#                     name=name)
#     except sqlite3.IntegrityError as err:
#         await bot.send_message(chat_id=ADMINS[0], text=err)
#     # Adminga xabar beramiz
#     count = db.count_users()[0]
#     msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
#     await bot.send_message(chat_id=ADMINS[0], text=msg)

















































