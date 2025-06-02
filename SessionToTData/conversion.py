import asyncio
from telethon.sync import TelegramClient
from opentele.td import TDesktop

async def session_to_tdata(session_name, api_id, api_hash):
    client = TelegramClient(session_name, api_id, api_hash)
    await client.start()

    if not await client.is_user_authorized():
        print("Ошибка: требуется авторизация.")
        return

    tdesk = await client.ToTDesktop()
    tdata_folder = f"TData/{session_name.split('.')[0]}"
    tdesk.SaveTData(tdata_folder)

    print(f"TData для {session_name} создан! Можно войти в Telegram Desktop.")

    await client.disconnect()

api_id = 27354344  # Замени на свои данные
api_hash = "50b30e7d885e9ea8718e4dba2dda6424" # Замени на свои данные
asyncio.run(session_to_tdata("sessions/example.session", api_id, api_hash))
