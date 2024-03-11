import requests
import json
import time


YOUTUBE_API_KEY = "YOUTUBE_API"
TELEGRAM_BOT_TOKEN = "TOKEN_BOT"
TELEGRAM_CHANNEL_ID = "CHANNEL_ID"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {"chat_id": TELEGRAM_CHANNEL_ID, "text": message}
    try:
        response = requests.post(url, json=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Telegram: {e}")


def check_youtube_stream_status(channel_id):
    url = f"https://www.googleapis.com/youtube/v3/search?key={YOUTUBE_API_KEY}&channelId={channel_id}&eventType=live&type=video"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if 'items' in data:
            return len(data['items']) > 0
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error checking YouTube stream status: {e}")
        return False

# Основний код програми
def main():
    youtube_channel_id = "YOUTUBE_CHANNEL_ID"

    while True:
        if check_youtube_stream_status(youtube_channel_id):
            message = f"🎥 Вітання! Стрім активний! Приєднуйтесь: https://www.youtube.com/channel/{youtube_channel_id}/live"
            send_telegram_message(message)
            time.sleep(600)  
        else:
            
            time.sleep(600)  

if __name__ == "__main__":
    main()
