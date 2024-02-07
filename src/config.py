from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_GUILD= int(os.getenv('BOT_GUILD'))
NOTIFY_CHANNEL_ID = int(os.getenv('NOTIFY_CHANNEL_ID'))
NOTIFY_USER_ID = int(os.getenv('NOTIFY_USER_ID'))
TARGET_BOT_ID = int(os.getenv('TARGET_BOT_ID'))
