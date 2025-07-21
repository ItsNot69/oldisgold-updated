from bot import Bot
import asyncio
from pyrogram import idle


async def main():
    app = Bot()

    await app.start()
    await idle()
    await app.stop()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())