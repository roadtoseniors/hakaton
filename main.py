import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import StateFilter
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

import gpt
import ex1.statesform
import form
import keyboards
from ex1.statesform import StepsForm

logging.basicConfig(level=logging.INFO)
bot = Bot(token="6490044113:AAHXpAUHwnfIrNeTKdmU-v6_2t4XKenYyXg")
dp = Dispatcher()
dp.message.register(form.get_fio, StepsForm.GET_FIO)
dp.message.register(form.get_opi, StepsForm.GET_OPI)
dp.message.register(form.get_best, StepsForm.GET_BEST)
dp.message.register(form.get_nonnrav, StepsForm.GET_NONRAV)
dp.message.register(form.get_end, StepsForm.GET_END, bot)


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(text="Доброго времени суток, это бот созданный для описания с помощью искуственного итеолекта"
                         "Жизни вашего предка", reply_markup=keyboards.main_kb)


@dp.callback_query()
async def cmd_callback(call: types.CallbackQuery, state: FSMContext):
    await call.answer()

    if call.data == "help":
        await call.message.answer("Вашу ошибку.")
        await state.set_state(ex1.statesform.HelpForm.Text)
    elif call.data == "form":
        await call.message.answer(f'Начинаем опрос.\n Как звали вашего близского?')
        await state.set_state(ex1.statesform.StepsForm.GET_FIO)
    elif call.data == "reset":
        await call.message.answer("Начинаем опрос.\n Введите вашего родсвеника ФИО")
        await state.set_state(ex1.statesform.StepsForm.GET_FIO)


@dp.message(StateFilter(ex1.statesform.HelpForm.Text))
async def helptext(message: types.Message, state: FSMContext):
    await state.set_state()
    await bot.send_message(chat_id=511800914, text=f"Новая жалоба:\n{message.text}")

@dp.message(Command('help'))
async def start(message: types.Message,state: FSMContext):
    await message.answer("Напишите вашу ошибку.")
    await state.set_state(ex1.statesform.HelpForm.Text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())