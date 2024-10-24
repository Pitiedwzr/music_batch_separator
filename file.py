import os


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
    def __init__(self, result):
        self.size = 
        self.url = ""
        self.name = ""