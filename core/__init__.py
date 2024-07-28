from linebot.v3 import WebhookHandler
from linebot.v3.messaging import Configuration
import os
from dotenv import load_dotenv

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


# 加載.env文件中的環境變量
load_dotenv()

# 獲取環境變量中的LINE_CHANNEL_ACCESS_TOKEN和LINE_CHANNEL_SECRET

LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')

handler = WebhookHandler(LINE_CHANNEL_SECRET)
configuration = Configuration(access_token=LINE_CHANNEL_ACCESS_TOKEN)

# from . import function_app
# from core.routes import function_app_t1