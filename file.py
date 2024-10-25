import os
import json
from settings import config


class InputFile:
    """Represents an audio file"""
    def __init__(self, file_path):
        self.path = file_path
        self.name = os.path.basename(file_path)
        self.name_base = os.path.splitext(self.name)[0]
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
            
        # Get the files list from the nested structure
        files_list = []
        if isinstance(datas, dict):
            if 'data' in datas and 'files' in datas['data']:
                files_list = datas['data']['files']
            elif 'files' in datas:
                files_list = datas['files']
        elif isinstance(datas, list):
            files_list = datas

        self.files = []
        for file_data in files_list:
            file_info = {
                "name": InputFile.name_base + "_" + file_data["type"] + format,
                "path": os.path.join("./output", InputFile.name_base + "_" + file_data["type"] + format),
                "url": file_data["url"]
            }
            self.files.append(file_info)