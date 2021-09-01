from pyrogram import Client as Bot
from config import API_ID, API_HASH, BOT_TOKEN
from bot.start import start

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="bot"),
)

bot.start()
start()
