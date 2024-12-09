import asyncio
from aiogram import Bot, Dispatcher, types, Router
from aiogram.types import Message
from aiogram.filters import Command
import smtplib
from email.mime.text import MIMEText

# Функция отправки письма
async def send_email(smtp_server, smtp_port, email, password, recipient, message):
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(email, password)
            msg = MIMEText(message, "plain")
            msg["Subject"] = "Сообщение от Telegram-бота"
            msg["From"] = email
            msg["To"] = recipient
            server.sendmail(email, recipient, msg.as_string())
        return "Письмо успешно отправлено!"
    except smtplib.SMTPException as e:
        return f"Произошла ошибка при отправке письма: {e}"

async def main():
    # Запрос токена, email и пароля у пользователя
    print("Введите необходимые данные для запуска бота.")
    tg_token = input("Токен Телеграм-бота: ").strip()
    smtp_email = input("Электронная почта (SMTP): ").strip()
    smtp_password = input("Пароль от почты: ").strip()

    print("\nПроверяем данные и запускаем бота...")

    # Создаем экземпляр бота и диспетчера
    bot = Bot(token=tg_token)
    dp = Dispatcher()
    router = Router()  # Создаем Router для маршрутизации

    # Обработчик команды /start
    @router.message(Command("start"))
    async def start_handler(message: Message):
        await message.answer("Привет! Пожалуйста, отправь свой email для отправки сообщения.")

    # Обработчик email
    @router.message(lambda msg: "@" in msg.text and "." in msg.text)
    async def email_handler(message: Message):
        user_email = message.text.strip()
        await message.answer(f"Спасибо! Теперь отправь текст сообщения для отправки на {user_email}.")

        # Вложенный обработчик для текста сообщения
        @router.message(lambda msg: True)
        async def text_handler(msg: Message):
            user_message = msg.text.strip()
            response = await send_email("smtp.yandex.ru", 465, smtp_email, smtp_password, user_email, user_message)
            await msg.answer(response)
            await msg.answer("Можешь отправить новый email или текст сообщения.")

        router.message.register(text_handler)

    # Подключаем маршрутизатор к диспетчеру
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    print("Бот успешно запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
