

import asyncio
import base64
import os
import random        
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from Deepak.resources.data import RAID, REPLYRAID, DEEPAK
from Deepak.main import tgbot 
from config import SUDO_USERS, OWNER_ID

lol = '/'

que = {}



@tgbot.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % lol))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage)
        Deepak = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(Deepak) == 2:
            user = str(Deepak[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in Deepak:
                text = f"I can't raid on @OFFICIALHACKERERA's Owner"
                await e.reply(text)
            elif int(g) == OWNER_ID:
                text = f"This guy is a owner Of this Tgbots."
                await e.reply(text)
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text) 
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(Deepak[0])
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.5)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in DEEPAK:
                text = f"I can't raid on @OFFICIALHACKERERA's Owner"
                await e.reply(text)
            elif int(g) == OWNER_ID:
                text = f"This guy is a owner Of this Tgbots."
                await e.reply(text)
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text)
            else:
                c = b.first_name
                counter = int(Deepak[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)




@tgbot.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(REPLYRAID)),
            reply_to=event.message.id,
        )



@tgbot.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % lol))
async def _(e):
    global que
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>."
    if e.sender_id in SUDO_USERS:
        Deepak = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        SAMx = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(Deepak[0])
            a = await e.client.get_entity(message)
            user_idd = a.id
            user_id = int(user_idd)
            if int(user_id) in Deepak:
                text = f" can't raid on @OFFICIALHACKERERA's Owner."
                await e.reply(text)
            elif int(user_id) == OWNER_ID:
                text = f"This guy is a owner Of this Tgbots."            
                await event.reply(text)
            elif int(user_id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text)
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"Activated replyraid"
                await e.reply(text)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            umser = await e.client.get_entity(a.sender_id)
            user_idd = umser.id
            user_id = int(user_idd)
            if int(user_id) in DEEPAK:
                text = f" can't raid on @OFFICIALHACKERERA's Owner."
                await e.reply(text)
            elif int(user_id) == OWNER_ID:
                text = f"This guy is a owner Of this Tgbots."
                await event.reply(text)
            elif int(user_id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text)
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"Activated Replyraid"
                await e.reply(text)
        else:
            await e.reply(usage)



@tgbot.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % lol))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    global que    
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage)
        Deepak = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(Deepak[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text)
        else:
            await e.reply(usage)
    

@tgbot.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % lol))
async def _(event):
   usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗘𝗟𝗔𝗬𝗥𝗔𝗜𝗗\n\nCommand:\n\n.delayraid <delay> <count> <Username of User>\n\n.delayraid <delay> <count> <reply to a User>\n\nCount and Sleeptime must be a integer."        
   if event.sender_id in SUDO_USERS:
         if event.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
         Deepak = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
         if len(Deepak) == 3:
             user = str(Deepak[2])
             a = await event.client.get_entity(user)
             e = a.id
             if int(e) in DEEPAK:
                    text = f"I can't raid on @OFFICIALHACKERERA's Owner"
                    await event.reply(text)
             elif int(e) == OWNER_ID:
                text = f"This guy is a owner Of this Bots."
                await event.reply(text)
             elif int(e) in SUDO_USERS:
                    text = f"This guy is a sudo user."
                    await event.reply(text)
             else:
                 c = a.first_name
                 username = f"[{c}](tg://user?id={e})"
                 counter = int(Deepak[1])
                 sleeptimet = sleeptimem = float(Deepak[0])
                 for _ in range(counter):
                      reply = random.choice(RAID)
                      caption = f"{username} {reply}"
                      async with event.client.action(event.chat_id, "typing"):
                          await event.client.send_message(event.chat_id, caption)
                          await asyncio.sleep(sleeptimem)
         elif event.reply_to_msg_id:
               a = await event.get_reply_message()
               b = await event.client.get_entity(a.sender_id)
               e = b.id
               if int(e) in DEEPAK:
                       text = f"I can't raid on @OFFICIALHACKERERA's Owner"
                       await event.reply(text)
               elif int(e) == OWNER_ID:
                       text = f"This guy is a owner Of this Bots."
                       await event.reply(text)
               elif int(e) in SUDO_USERS:
                       text = f"This guy is a sudo user."
                       await event.reply(text)
               else:
                   c = b.first_name
                   username = f"[{c}](tg://user?id={e})"
                   sleeptimet = sleeptimem = float(Deepak[0])
                   counter = int(Deepak[1])
                   for _ in range(counter):
                        reply = random.choice(RAID)
                        caption = f"{username} {reply}"
                        async with event.client.action(event.chat_id, "typing"):
                             await event.client.send_message(event.chat_id, caption)
                             await asyncio.sleep(sleeptimem)
         else:
            await event.reply(usage)
