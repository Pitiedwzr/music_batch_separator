import os
import json
from settings import config


class InputFile:
    """Represents an audio file"""
    def __init__(self, file_path):
        self.path = file_path
        self.name = os.path.basename(file_path)
        self.binary = open(self.path, 'rb')
        self.status = ""
        self.hash = ""
        self.size = os.path.getsize(self.path)
        
class SeparatedFile:
    def __init__(self, datas, InputFile):
        if config.common.output_format == 0:
            format = ".mp3"
        elif config.common.output_format == 1:
            format = ".wav"
        elif config.common.output_format == 2:
            format = ".flac"
        elif config.common.output_format == 3:
            format = ".m4a"
        

        # Handle both cases: when datas is a list or when it's a dict with "files" key
        files_list = datas if isinstance(datas, list) else datas.get("files", [])
        
        self.files = []  # Store all files info
        for file_data in files_list:
            file_info = {
                "name": InputFile.name + "_" + file_data["type"] + format,
                "path": "./output/" + InputFile.name + "_" + file_data["type"] + format,
                "url": file_data["url"]
            }
            self.files.append(file_info)