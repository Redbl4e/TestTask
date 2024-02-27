import json

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from aggregate.main import aggregate_main
from const.router import invalid_value, hello

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    username = message.from_user.username
    await message.answer(hello.format(username))


@router.message(F.text)
async def aggregate_data(message: Message):
    try:
        data_dict = json.loads(message.text)
        result = aggregate_main(data_dict)
        await message.answer(json.dumps(result))
    except json.decoder.JSONDecodeError:
        await message.answer(invalid_value)
