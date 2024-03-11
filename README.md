# Телеграм-бот для сповіщення про початок стріму на YouTube

Даний проект є простим телеграм-ботом, який сповіщає про початок стріму на каналі YouTube. Бот перевіряє статус стріму на заданому каналі YouTube та надсилає повідомлення у Телеграм, якщо стрім активний.

## Встановлення

1. Спершу склонуйте цей репозиторій на ваш комп'ютер:
```
git clone https://github.com/kozhydlo/YouTube-Stream-Notifier.git
```

2. Встановіть необхідні бібліотеки Python, використовуючи `pip`


## Використання

1. Отримайте API ключ для YouTube Data API. Для цього відвідайте [Google Cloud Console](https://console.cloud.google.com/), створіть новий проект, активуйте YouTube Data API та отримайте ключ API.

2. Отримайте токен вашого телеграм бота. Для цього створіть бота через [BotFather](https://t.me/BotFather) та отримайте токен.

3. Створіть канал у Телеграмі, до якого будуть надсилатися повідомлення про стріми. Отримайте ідентифікатор каналу (chat_id).

4. Відкрийте файл `main.py` та встановіть згадані раніше ключі API та ідентифікатори каналів у відповідних змінних:

```python
YOUTUBE_API_KEY = "YOUR_YOUTUBE_API_KEY"
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHANNEL_ID = "YOUR_TELEGRAM_CHANNEL_ID"
```

Запустіть програму:
```
python main.py
```

# Де отримати ключі API
YOUTUBE_API_KEY: Ви можете отримати ключ для YouTube Data API, створивши проект на Google Cloud Console, активувавши YouTube Data API та створивши ключ API.

TELEGRAM_BOT_TOKEN: Ви можете отримати токен бота, створивши його через BotFather у Телеграмі.

TELEGRAM_CHANNEL_ID: Для отримання ідентифікатора каналу, використайте бота userinfobot у Телеграмі, або скористайтеся бібліотекою python-telegram-bot для отримання ідентифікатора каналу.

YOUTUBE_CHANNEL_ID: Ідентифікатор вашого каналу на YouTube, до якого ви хочете надсилати сповіщення про стріми.

