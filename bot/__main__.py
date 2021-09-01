from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from bot.videoplayer import start

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="bot"),
)

bot.start()
start()
