import json
import os
# from ..services import text_message as stm
# static_url = "../../static"
static_url = "lineWebhookApp/static"

# def handle_text_file():

#     with open(static_url + ) as file:
class CommonUtil():

    def __init__(self):
        pass
    
    def handle_json_file(self, file_url, file_name):
        # file_url = ""
        # file_name = "test.json"
        # current_directory = os.getcwd()
        # print(f"current_directory{current_directory}")

        file_path = self.get_file_path(file_name)
        try:
            with open(file_path, encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f'File not found: {file_path}')

    # def get_event_attr(self, event):
    #     src_user_id = getattr(event.source, 'user_id', None)
    #     src_group_id = getattr(event.source, 'group_id', None)
    #     src_type = getattr(event.source, 'type', None)
    #     reply_token = getattr(event, 'reply_token', None)

    #     if (event.type == "join"):
    #         return src_user_id, src_group_id, reply_token
    #     if (event.type == "message"):
    #         raw_msg_text = getattr(event.message, 'text', None)
    #         msg_text = stm.preprocess_message(src_type, raw_msg_text)
    #         return src_user_id, src_group_id, msg_text, reply_token

    # def json2string(self, data):
    #     json_string = json.dumps(data)
    #     return json_string
    def get_file_path(self, filename):

        # 當前文件的目錄
        current_dir = os.path.dirname(__file__)

        # 向上移動一層
        parent_dir = os.path.dirname(current_dir)

        # 再向上移動一層
        grandparent_dir = os.path.dirname(parent_dir)

        return os.path.join(grandparent_dir, 'static/templates/text_messages', filename)
