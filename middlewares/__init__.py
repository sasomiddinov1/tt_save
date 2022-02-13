from aiogram import Dispatcher

from loader import dp
from .checksub import BigBrother
from .throttling import ThrottlingMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(BigBrother())
