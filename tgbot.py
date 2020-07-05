import config
import logging

from aiogram import Bot, Dispatcher, executor, types

from sqlighter import SQLighter

# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

db = SQLighter('db.db')


# команда активации подписки
@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    if not db.subscriber_exists(message.from_user.id):
        # если нет юзера в базе, добавить.
        db.add_subscriber(message.from_user.id)
    else:
        # если он уже есть, то обновляем статус подписки
        db.update_subscription(message.from_user.id, True)
    await message.answer("Вы успешно подписались на рассылку ОГРА!\nЖдите обновлений")


# команда отписки
@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    if not db.subscriber_exists(message.from_user.id):
        # если юзера нет в базе, добавляем его с неактивной подпиской (запоминаем)
        db.add_subscriber(message.from_user.id, False)
        await message.answer("Вы не были подписаны")
    else:
        # если он уже есть, то обновляем статус подписки
        db.update_subscription(message.from_user.id, False)
        await message.answer("Вы успешно отписаны от рассылки")


# запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
