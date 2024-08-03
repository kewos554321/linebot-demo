from linebot.v3.webhooks import MessageEvent, TextMessageContent, StickerMessageContent
from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)
from linebot.v3.messaging import Configuration
import os
from dotenv import load_dotenv

from core.linebot.handlers import MessageEventHandler

# 加載.env文件中的環境變量
load_dotenv()

# 獲取環境變量中的LINE_CHANNEL_ACCESS_TOKEN和LINE_CHANNEL_SECRET
LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')

handler = WebhookHandler(LINE_CHANNEL_SECRET)
configuration = Configuration(access_token=LINE_CHANNEL_ACCESS_TOKEN)

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    MessageEventHandler().handle_message(event)