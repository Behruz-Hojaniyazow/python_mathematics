import asyncio
import logging
import yt_dlp
import os

from aiogram import Bot, Dispatcher, types
from aiogram.types import FSInputFile
from aiogram.filters import CommandStart

# TOKEN Railway Variables'dan olinadi
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("👋 Salom!\nLink yubor (YouTube / TikTok / Instagram)\nMen video yuklab beraman 🎬")


@dp.message()
async def download_video(message: types.Message):
    url = message.text

    if not url or "http" not in url:
        await message.answer("❌ Iltimos link yubor!")
        return

    await message.answer("⏳ Yuklanmoqda...")

    try:
        ydl_opts = {
            'outtmpl': 'video.%(ext)s',
            'format': 'best',
            'quiet': True,
            'noplaylist': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        file_name = None
        for file in os.listdir():
            if file.startswith("video."):
                file_name = file
                break

        if not file_name:
            await message.answer("❌ Video topilmadi!")
            return

        video = FSInputFile(file_name)
        await message.answer_video(video)

        os.remove(file_name)

    except Exception as e:
        await message.answer(f"❌ Xatolik: {e}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())