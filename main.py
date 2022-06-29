import logging
import os
os.system("pip install aiogram")
from random import randint
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentTypes
from aiogram.types.message import ContentType
import markups as nav
waiting = 0
TOKEN = "5577758465:AAE3GrJxGq0MDg6HOHSbyIVULywe7yQXtTA"
ADMIN_ID = "1764135502"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(ADMIN_ID, "{0.username} написал(а) /start".format(message.from_user), parse_mode="HTML")
    global waiting
    waiting = 0
    if message.chat.type == 'private':
        print("ID " + str(message.from_user.id) + " написал(а) /start")
        await bot.send_message(message.from_user.id, "✅ Здравствуйте, *{0.first_name}*!\nВы находитесь в оффицальной поддержке магазина «*Lemada*».\nКакой у Вас вопрос❓".format(message.from_user), parse_mode= 'Markdown', reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        global waiting
        if waiting == 0:
            if message.text == "/support":
                print("ID " + str(message.from_user.id) + " описывает проблему")
                await bot.send_message(ADMIN_ID, "{0.username} описывает проблему".format(message.from_user).format(message.from_user), parse_mode="HTML")
                await bot.send_message(message.from_user.id, "✍️ *{0.first_name}* , опишите вашу проблему".format(message.from_user), parse_mode= 'Markdown', reply_markup=nav.supportMenu)
                waiting = 1
            else:
                print("ID " + str(message.from_user.id) + " написал(а) " + message.text)
                await bot.send_message(ADMIN_ID, "{0.username} написал(а) " + message.text.format(message.from_user), parse_mode="HTML")
                await bot.send_message(message.from_user.id, "🤔 Я не знаю, что ответить на «*" + message.text +"*».\nПерепроверьте команду и напишите её снова.".format(message.from_user), parse_mode= 'Markdown')
                await bot.send_message(message.from_user.id, "✅ Здравствуйте, *{0.first_name}*!\nВы находитесь в оффицальной поддержке магазина «*Lemada*».\nКакой у Вас вопрос❓".format(message.from_user), parse_mode= 'Markdown', reply_markup=nav.mainMenu)
        else:
            waiting = 0
            print("ID " + str(message.from_user.id) + " описал(а) проблему")
            await bot.send_message(ADMIN_ID, "{0.username} описал(а) проблему " .format(message.from_user), parse_mode="HTML")
            await bot.send_message(message.from_user.id, "*{0.first_name}*, Ваше сообщение успешно отправленно.\nСкоро вам ответят, ожидайте!".format(message.from_user), parse_mode= 'Markdown')
            await bot.send_message(ADMIN_ID,  "✍️: " + str(message.html_text) + "\n🆔: " + str(message.from_user.id), parse_mode="HTML")


            

@dp.callback_query_handler(text="btnRandom")
async def randomize(message: types.Message):
    print("ID " + str(message.from_user.id) + " описывает проблему")
    await bot.send_message(ADMIN_ID, "{0.username} описывает проблему ".format(message.from_user), parse_mode="HTML")
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "✍️ *{0.first_name}* , опишите вашу проблему".format(message.from_user), parse_mode= 'Markdown', reply_markup=nav.supportMenu)
    global waiting
    waiting = 1



@dp.callback_query_handler(text="btnBack")
async def back(message: types.Message):
    global waiting
    waiting = 0
    print("ID " + str(message.from_user.id) + " вернулся(ась) в /start")
    await bot.send_message(ADMIN_ID, "{0.username} вернулся(ась) в /start".format(message.from_user), parse_mode="HTML")
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "✅ Здравствуйте, *{0.first_name}*!\nВы находитесь в оффицальном чате поддержки магазина «*LadyWow*».\nКакой у Вас вопрос❓".format(message.from_user), parse_mode= 'Markdown', reply_markup=nav.mainMenu)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)

