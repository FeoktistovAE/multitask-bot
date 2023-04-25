## Описание:

multitask-bot - это многозадачный Телеграм бот, который уммет:

1. Получать текущую погоду (c помощью OpenWeatherMap API) в выбранном городе
и отправлять краткую метеосводку пользователю
2. Вычислять обменный курс (с помощью Exchange Rates API) выбранных валют,
производить перерасчет указанной суммы и отправлять эту информацию пользователю
3. Отправлять пользователю произвольную милую фотографию животного
(с помощью Unsplash API)
4. Создавать опрос с помощью введённой пользователем информации и отправлять его
в указанный чат,используя chat_id 

## Stack:

* Aiogram
* Asyncio
* pymorphy2
* environs
* Open

### Установка:

Склонируйте репозиторий:
```bash
git clone https://github.com/FeoktistovAE/multitask-bot
```

Войдите в корневую папку:
```bash
cd multitask-bot
```

Установите зависимости c помощью Poetry:
```bash
make install
```

Измените имя файла .env.sample на .env:
```bash
mv .env.sample .env
```

Добавьте все необходимые переменные окружения в файл .env:
```bash
BOT_TOKEN=Telegram Token
WEATHER_TOKEN=OpenWeatherMap Api Key
EXCHANGE_RATES_TOKEN=Exchange Rates API
ANIMAL_PICTURES_TOKEN=Unsplash API
```

Запустите бота:
```bash
python bot.py
```




