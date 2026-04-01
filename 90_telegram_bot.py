import asyncio
import logging
import yt_dlp
import os
import requests

from aiogram import Bot, Dispatcher, types
from aiogram.types import FSInputFile
from aiogram.filters import CommandStart

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)


# 📥 IMAGE DOWNLOAD
def download_image(url, filename):
    r = requests.get(url)
    with open(filename, "wb") as f:
        f.write(r.content)


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("👋 Salom!\nTikTok link yubor\nMen video yoki rasmlarni yuklab beraman 🚀")


@dp.message()
async def download_handler(message: types.Message):
    url = message.text.strip()

    if "tiktok.com" not in url:
        await message.answer("❌ Hozir faqat TikTok ishlaydi")
        return

    await message.answer("⏳ Yuklanmoqda...")

    try:
        os.makedirs("downloads", exist_ok=True)

        # 🔥 1. TikTok API orqali rasm tekshiramiz
        api = f"https://www.tikwm.com/api/?url={url}"
        res = requests.get(api).json()

        images = res.get("data", {}).get("images", [])

        # 📸 AGAR PHOTO BO‘LSA
        if images:
            for i, img in enumerate(images):
                filename = f"downloads/photo_{i}.jpg"
                download_image(img, filename)
                await message.answer_photo(photo=FSInputFile(filename))
                os.remove(filename)
            return

        # 🎥 AGAR VIDEO BO‘LSA (yt-dlp)
        ydl_opts = {
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'format': 'best',
            'quiet': True,
            'noplaylist': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        await message.answer_video(video=FSInputFile(filename))
        os.remove(filename)

    except Exception as e:
        await message.answer(f"❌ Xatolik:\n{e}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())