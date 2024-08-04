from linebot.v3.webhooks import MessageEvent, TextMessageContent, StickerMessageContent
from core.linebot.services import TextMessageService
from core.linebot.services.template_message import TemplateMessageService
from core.linebot.services.location_message import LocationMessageService
from core.linebot.services.image_message import ImageMessageService
from core.linebot.services.sticker_message import StickerMessageService
from core.linebot.services.flex_message import FlexMessageService
from core.linebot.services.common_features import CommonFeaturesService

class MessageEventHandler():

    def __init__(self):
        ''' Services '''
        self.text_message_service = TextMessageService()
        self.template_message_service = TemplateMessageService()
        self.location_message_service = LocationMessageService()
        self.image_message_service = ImageMessageService()
        self.sticker_message_service = StickerMessageService()
        self.flex_message_service = FlexMessageService()

        ''' Params '''
        self.event_type = None
        self.event_source = None
        self.event_source_type = None
        self.event_source_user_id = None
        self.event_source_group_id = None
        self.event_timestamp = None
        self.event_webhook_event_id = None
        self.event_delivery_context = None
        self.event_delivery_context_is_redelivery = None
        
        self.event_reply_token = None
        self.event_message = None
        self.event_message_type = None
        self.event_message_id = None
        self.event_message_text = None
        self.event_message_emojis = None
        self.event_message_mention = None
        self.event_message_quote_token = None

    def handle_message(self, event):
        print("\n (TextMessageContent) event=", event)
        self.retrieve_event_attr(event)
        # print("self.msg_text=", self.msg_text)
        if self.event_message_text == "help":
            self.text_message_service.reply_text_message_with_resource(self.event_reply_token, "help.json")
        # elif "test TextMessageService" in self.event_message_text:
        #     print("start to test TextMessageService")
        #     self.text_message_service.reply_text_message_with_resource(self.event_reply_token, "test_text_message.json") 
        elif "test TextMessageService" in self.event_message_text:
            print("start to test TextMessageService")
            self.text_message_service.reply_text_message(self.event_reply_token, "這是我的測試而已") 
        elif "test TemplateMessageService" in self.event_message_text:
            self.template_message_service.show_test_confirm_template_message(self.event_reply_token)
        elif "test LocationMessageService" in self.event_message_text:
            print("start to test LocationMessageService")
            self.location_message_service.show_test_location_message(self.event_reply_token)
        elif "test ImageMessageService" in self.event_message_text:
            print("start to test ImageMessageService")
            self.image_message_service.show_sushi_image_message(self.event_reply_token)
        elif "test FlexMessageService" in self.event_message_text:
            print("start to test FlexMessageService")
            self.flex_message_service.show_carousel_flex_message_test(self.event_reply_token)
        # source_id = src_user_id if src_group_id is None else src_group_id
        # if msg_text == "h": 
        #     filename = "help.json"
        #     sms.show_test_sticker_message(reply_token)
        #     # stm.send_reply_message_with_resource(reply_token, filename)
        # elif msg_text == "sm":
        #     sms.show_test_sticker_message(reply_token)
        # elif msg_text == "t":
        #     tpms.show_test_confirm_template_message(reply_token)
        # elif msg_text == "r":
        #     tpms.show_test_buttons_template_message(reply_token)
        # elif msg_text == "e":
        #     tpms.show_test_carousel_template_message(reply_token)
        # elif msg_text == "w":
        #     tpms.show_test_imagecarousel_template_message(reply_token)
        # elif msg_text == "q":
        #     ims.show_sushi_image_message(reply_token)
        # elif msg_text == "y":
        #     fms.show_carousel_flex_message_test(reply_token)
        # elif msg_text == "u":
        #     cfs.show_test_common_message(reply_token)
        # elif msg_text == "menu":
        #     tpms.show_shushi_menu(reply_token)
        # elif msg_text == "我想要訂位預約":
        #     tpms.show_shushi_reservation_step1(reply_token)
        # elif msg_text == "我想看今日特餐":
        #     tms.show_test_text_message(reply_token) 
        # elif msg_text == "我想看菜單":
        #     tms.show_test_text_message(reply_token) 
        # elif msg_text == "我想知道店鋪位置":
        #     lms.show_test_location_message(reply_token)
        # else:
        #     tms.show_unkown(reply_token)

    def create_all_service(self):
        lms = LocationMessageService()
        sms = StickerMessageService()
        tms = TextMessageService()
        tpms = TemplateMessageService()
        ims = ImageMessageService()
        fms = FlexMessageService()
        cfs = CommonFeaturesService()
        return sms, lms, tms, tpms, ims, fms, cfs

    def retrieve_event_attr(self, event):

        self.event_type = getattr(event, 'type', None)
        self.event_source = getattr(event, 'source', None)
        self.event_source_type = getattr(event.source, 'type', None)
        self.event_source_user_id = getattr(event.source, 'user_id', None)
        self.event_source_group_id = getattr(event.source, 'group_id', None)
        self.event_timestamp = getattr(event, 'timestamp', None)
        self.event_webhook_event_id = getattr(event, 'webhook_event_id', None)
        self.event_delivery_context = getattr(event, 'delivery_context', None)
        self.event_delivery_context_is_redelivery = getattr(event.delivery_context, 'is_redelivery', None)
        
        self.event_reply_token = getattr(event, 'reply_token', None)
        self.event_message = getattr(event, 'message', None)
        self.event_message_type = getattr(event.message, 'type', None)
        self.event_message_id = getattr(event.message, 'id', None)
        self.event_message_text = getattr(event.message, 'text', None)
        self.event_message_emojis = getattr(event.message, 'emojis', None)
        self.event_message_mention = getattr(event.message, 'mention', None)
        self.event_message_quote_token = getattr(event.message, 'quote_token', None)
        # print(f"\n===> src_user_id={self.src_user_id}, src_group_id={self.src_group_id}, msg_text={self.msg_text}, reply_token={self.reply_token}")


