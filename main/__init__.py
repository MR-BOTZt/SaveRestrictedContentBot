#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 20869850
API_HASH = "b9d94e303d86df2a2b32679e50ccfb43"
BOT_TOKEN = "5713314297:AAEV5vDP5rQPOMdX3QUHugoCYJ4_EDe1mhY"
SESSION = "AQBPUMVJICRDJOb-oGUlTACu6CF3XbLmZ85NjcwHapyW-1bo6sozw9fKpNJ25xeEAEVlRjqCqdQsuZzFp4wYIfDkL8caLL7WlI1hFDLcybQB1aqpDZCTZNz21aBW2ClT_yhydAs1l4Lq7xU4ctjlHty2ttJdj1BurhNDjUpnp7sOE_jxyrdJ8g5E72-EPD1EOnLzREbT87394PvH-G9QRfUbIs-uZtrA1ixRBADbl6dhF1185wJX7BxaHm8wOUqVIKxHfF3br5bUOqXcLCOyBidyuWUCDsk44_p6JIe8456ADWqJb2AwalK4aJeWnoF-nQpYrF9AbAHLCBjshYxRjsG5AAAAAVLxVIIA"
FORCESUB = "forcesubbbbbbbbdkkd"
AUTH = 5531461861

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
