# otpro8
OTRPO labs

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
4. В папке с репозиторием запустите скрипт: `python smtp8.py`
5. Введите данные:
Токен Telegram-бота, E-mail и пароль для отправки писем.
6. Откройте чат с ботом в Telegram, отправьте /start, а затем следуйте инструкциям.

[Скриншот с примером работы](https://sun9-57.userapi.com/s/v1/ig2/YOoc_656Vkk5uMXXTfyOJ4D2IOeNk_JVGYnrFxuaQVtonH4IWfLTGJGBvL08u8N7EL0L5YCMPL6psl3BewmBHR3K.jpg?quality=95&as=32x20,48x30,72x45,108x68,160x100,240x151,360x226,480x301,540x339,640x401,720x452,1080x678,1280x803&from=bu&u=ZaNnLoR1sIhYwI4Dn2GBVYmvc0gYs2deA2qxaUZ8O28&cs=1280x803)
