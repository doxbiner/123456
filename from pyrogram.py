import pyrogram
from pyrogram.api import functions as fn

api_id = ...
api_hash = '...'
phone_number = '+...'

app = pyrogram.Client(
    "my_account",
    api_id=api_id,
    api_hash=api_hash,
    phone_number=phone_number
)

app.start()

# send message to self
app.send_message("me", "12")

async def search(chats):
    result = {}

    result["chats"] = []

    for chat in chats:
        async for dialog in app.iter_dialogs():
            if dialog.chat.title == chat or dialog.chat.username == chat:
                r = {}
                r["chat_id"] = dialog.chat.id
                result["chats"].append(r)
    return result

async def message(chat_name, message):
    result = await search([chat_name])

    for chat in result["chats"]:
        chat_id = chat["chat_id"]
        message = {"message": message}

        # Send message
        await app.send(fn.messages.SendMessage(chat_id=chat_id,message=message))

app.stop()
