import asyncio

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot
from aiogram.types import InputFile

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    print(users[0][0])
    await message.answer(users)

@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        photo_file = InputFile(path_or_bytesio="photo/photo_2022-02-13_13-59-03.jpg")
        await bot.send_photo(chat_id=user_id, photo=photo_file,
                             caption="β° Kunlik 2-3 soat vaqtingizni halol pul ishlashga sarflang!\n"

                                     "β Zamonaviy sohalarga qiziqasizmi?\n"
                                     "β Qo'shimcha oylik 300$-1.000$ daromadni istaysizmi?\n\n"
                                     "β Faqatgina halol daromadnichi?\n"

                                     "π Unda \"saytlar orqali daromad\" kursimiz aynan siz uchun!\n"

                                     'π Bizning kursimizda:\n'
                                     'β Halol pul ishlash usuli!\n'
                                     'β Tezkor daromad imkoni!\n'
                                     'β Real natija va fikrlar!\n'
                                     'β 1,5 yillik tajribaga ega ustozlar!\n'
                                     'β Professional darajada ta\'lim!\n'

                                     'π° Bizning daromadlarimiz\n'
                                     'π @BSNATIJALAR kanalida!\n'

                                     'β° Kurs davomiyligi: 10 kun;\n'
                                     'π Platforma: videokurslar orqali telegramda o\'rgatiladi;\n'

                                     'β Diqqat: xech qanday treyding, qimor(1XBET), franshiza yoki shunga o\'xshagan harom ishlarga aralashmaymiz!\n'

                                     'β Kursimiz narxi: 400.000 so\'m\n'
                                     'π -63% chegirmada: 149.000 so\'m\n'

                                     'βοΈ Ma\'lumot uchun: @bsadminuz\n'
                                     'π Telefon: +998991707849\n')
        await asyncio.sleep(0.05)

@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")