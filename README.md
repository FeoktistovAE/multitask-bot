## Описание:
Телеграм бот, выполненный в качестве тестового задания на позицию 
"Разработчик Python для написания автоматизаций и чат-ботов (удаленная работа)".


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




