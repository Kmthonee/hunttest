import telethon
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import base64
import datetime
from payment import *
from help import *
from checktele import *
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
# -

sython.start()
c = requests.session()

y = datetime.datetime.now().year
m = datetime.datetime.now().month
dayy = datetime.datetime.now().day
day = datetime.datetime.now().strftime("%A")
m9zpi = f"{y}-{m}-{dayy}"
sec = time.time()

LOGS = logging.getLogger(__name__)

DEVS = [
   5739596428,
]
DEL_TIME_OUT = 10
normzltext = "1234567890"
namerzfont = normzltext
name = "Profile Photos"
time_name = ["off"]
time_bio = ["off"]


async def join_channel():
    try:
        await sython(JoinChannelRequest("@x_xxax"))
    except BaseException:
        pass




@sython.on(events.NewMessage(outgoing=True, pattern=r"\.الاوامر"))
async def _(event):
    await event.edit(commands)

@sython.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
**ᴄʜᴇᴄᴋᴇʀ ɪs ʀᴜɴɪɴɢ ♕
𝙿ᴏɴɢ ↬ `{ms}`
ᴅᴀᴛᴇ ↬ `{m9zpi}`
user ɪᴅ ↬ `{event.sender_id}`
ᴅᴇᴠ ᴄʜᴇᴄᴋᴇʀ ↬ - @L_xLL **
''')


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.م1"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec1)


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.م2"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec2)

    
ownerhson_id = 5739596428
@sython.on(events.NewMessage(outgoing=False, pattern='علوش'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        await event.reply('هنا يمك علوش ابشر  @L_xLL')

@sython.on(events.NewMessage(outgoing=True, pattern=r"\.اعادة تشغيل"))
async def update(event):
    await event.edit("• جارِ اعادة تشغيل السورس ..\n• انتضر 1-2 دقيقة  .")
    await sython.disconnect()
    await sython.send_message("me", "`اكتملت اعادة تشغيل السورس !`")



LOGS = logging.getLogger(__name__)

logging.basicConfig(
    format="[%(levelname)s- %(asctime)s]- %(name)s- %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)

async def join_channel():
    try:
        await sython(JoinChannelRequest("@x_xxax"))
    except BaseException:
        pass
 
 
GCAST_BLACKLIST = [
    -1001884452589,
    -1001884452589,
]

DEVS = [
    5739596428,
]
 
    
@sython.on(events.NewMessage(outgoing=True, pattern=".سورس"))
async def _(event):
      await event.reply("""السـورس يعمـل |ᴀʟᴏѕʜ ᴄʜᴇᴄᴋᴇʀ
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍


- سورس بسيط يحتوي على الاوامر المهمة التي تحتاجها
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍""")

@sython.on(events.NewMessage(outgoing=True, pattern=".مطور"))
async def _(event):
      await event.edit("""ᴀʟᴏѕʜ ᴄʜᴇᴄᴋᴇʀ : @L_xLL"""
)

print("- sython Userbot Running ..")
sython.run_until_disconnected()
