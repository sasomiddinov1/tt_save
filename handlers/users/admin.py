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
                             caption="⏰ Kunlik 2-3 soat vaqtingizni halol pul ishlashga sarflang!\n"

                                     "— Zamonaviy sohalarga qiziqasizmi?\n"
                                     "— Qo'shimcha oylik 300$-1.000$ daromadni istaysizmi?\n\n"
                                     "— Faqatgina halol daromadnichi?\n"

                                     "🚀 Unda \"saytlar orqali daromad\" kursimiz aynan siz uchun!\n"

                                     '📌 Bizning kursimizda:\n'
                                     '✅ Halol pul ishlash usuli!\n'
                                     '✅ Tezkor daromad imkoni!\n'
                                     '✅ Real natija va fikrlar!\n'
                                     '✅ 1,5 yillik tajribaga ega ustozlar!\n'
                                     '✅ Professional darajada ta\'lim!\n'

                                     '💰 Bizning daromadlarimiz\n'
                                     '👉 @BSNATIJALAR kanalida!\n'

                                     '⏰ Kurs davomiyligi: 10 kun;\n'
                                     '🔗 Platforma: videokurslar orqali telegramda o\'rgatiladi;\n'

                                     '⚠Diqqat: xech qanday treyding, qimor(1XBET), franshiza yoki shunga o\'xshagan harom ishlarga aralashmaymiz!\n'

                                     '❌ Kursimiz narxi: 400.000 so\'m\n'
                                     '🎁 -63% chegirmada: 149.000 so\'m\n'

                                     '✍️ Ma\'lumot uchun: @bsadminuz\n'
                                     '📞 Telefon: +998991707849\n')
        await asyncio.sleep(0.05)

@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")