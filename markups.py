from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mainMenu = InlineKeyboardMarkup(row_width=2)
btnRandom = InlineKeyboardButton(text="๐ค ะะฑัะฐัะธัััั", callback_data="btnRandom")
btnUrl = InlineKeyboardButton(text="โ Wildberries", url="https://www.wildberries.ru/seller/404946")

supportMenu = InlineKeyboardMarkup(row_width=2)
btnBack = InlineKeyboardButton(text="โฌ๏ธ ะะตัะฝัััั", callback_data="btnBack")

mainMenu.insert(btnRandom)
mainMenu.insert(btnUrl)

supportMenu.insert(btnBack)