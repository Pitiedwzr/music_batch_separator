import os


class AudioFile:
    """Represents an audio file"""
    def __init__(self, file_path):
        self.path = file_path
        self.name = os.path.basename(file_path)
        self.binary = open(self.path, 'rb')
        self.status = ""
        self.hash = ""
        self.size = os.path.getsize(self.path)