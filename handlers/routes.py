from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Эта команда реагирует только на /start")

@router.message()
async def all_message(message: Message):
    await message.answer("Эта команда реагирует на все сообщения")