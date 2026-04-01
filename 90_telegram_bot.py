import asyncio
import logging
import yt_dlp
import os

from aiogram import Bot, Dispatcher, types
from aiogram.types import FSInputFile
from aiogram.filters import CommandStart

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("👋 Salom!\nLink yubor (TikTok / Instagram / YouTube)\nMen video yoki rasmni yuklab beraman 🚀")


@dp.message()
async def download_handler(message: types.Message):
    url = message.text.strip()

    await message.answer("⏳ Yuklanmoqda...")

    try:
        ydl_opts = {
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'format': 'best',
            'quiet': True,
            'noplaylist': True
        }

        os.makedirs("downloads", exist_ok=True)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

            # FILE NAME olish
            filename = ydl.prepare_filename(info)

        # 🔥 FILE TYPE aniqlash
        if filename.endswith(".mp4") or filename.endswith(".mkv"):
            await message.answer_video(video=FSInputFile(filename))

        elif filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            await message.answer_photo(photo=FSInputFile(filename))

        else:
            # boshqa formatlar (masalan audio yoki unknown)
            await message.answer_document(document=FSInputFile(filename))

        # 🧹 Faylni o‘chirish (server to‘lib ketmasin)
        os.remove(filename)

    except Exception as e:
        await message.answer(f"❌ Xatolik:\n{e}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())