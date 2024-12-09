# otpro8
OTPRO labs

# Telegram Email Bot

Этот бот позволяет отправлять письма на указанный email через Telegram. Он использует `aiogram` для работы с Telegram Bot API.

## Установка

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/LizzBizzLol/otpro8.git
   cd otpro8
   
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   
## Как запустить

1. Получите токен для Telegram-бота через BotFather.

2. Убедитесь, что у вас есть учетная запись электронной почты, поддерживающая SMTP (например, Yandex, Gmail):

Для Yandex: используйте SMTP-сервер smtp.yandex.ru и порт 465.
Для Gmail: используйте SMTP-сервер smtp.gmail.com и порт 465.

3. Создайте пароль для SMTP в своем почтовом ящике (Настройки - Безопасность - Пароли приложений - SMTP)
4. Запустите скрипт: `python smtp8.py`
5. Введите данные:
Токен Telegram-бота, E-mail и пароль для отправки писем.
6. Откройте чат с ботом в Telegram, отправьте /start, а затем следуйте инструкциям.
