from aiogram import types

from loader import dp, bot

from utils import remove_background


@dp.message_handler(content_types=types.ContentTypes.ANY)
async def tt_handler(msg: types.Message):
    tiktok = msg.text
    new_tiktok = await remove_background(tiktok)
    await msg.answer_video(video=new_tiktok, caption=f'{msg.text} \n '' \n''📥 @ttsave_says_bot'


                           )
