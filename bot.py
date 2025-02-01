from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, ChatMemberUpdated
import asyncio
import json
import logging

from commands import *
from data import datamanager
from utils import utils

settings = {}
with open('data/config.json', 'r', encoding='UTF-8') as f:
    settings = json.load(f)    

logging.basicConfig(level=logging.INFO)
bot = Bot(settings['token'])
dp = Dispatcher()
    

@dp.startup()
async def on_startup(dp):
    print('Bot started!')
    # Bot startupp


@dp.message(F.text)
async def MessageHandle(message: Message):
    if message.from_user.is_bot: return
    # Every people message


@dp.chat_member()
async def on_user_joined(event: ChatMemberUpdated):
    if event.new_chat_member.status == 'member':
        pass 
        # New member event


@dp.callback_query()
async def CallbackHandler(callback: CallbackQuery):
    pass
    # Handle callbacks

    
async def start():
    await dp.start_polling(bot)

asyncio.run(start())
