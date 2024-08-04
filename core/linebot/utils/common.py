import json
import os

class CommonUtil():

    def __init__(self):
        pass
    
    def handle_json_file(self, fileurl, filename):
        # current_directory = os.getcwd()
        # print(f"current_directory{current_directory}")
        # 'static/templates/text_messages'
        file_path = self.assemble_file_path(fileurl, filename)
        print(f"file_path={file_path}")
        try:
            with open(file_path, encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f'File not found: {file_path}')

    def assemble_file_path(self, fileurl, filename):
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.dirname(current_dir)
        grandparent_dir = os.path.dirname(parent_dir)
        return os.path.join(os.path.dirname(grandparent_dir), fileurl, filename)
    
    def json2string(self, data):
        json_string = json.dumps(data)
        return json_string