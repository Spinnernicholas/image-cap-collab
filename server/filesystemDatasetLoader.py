import os
from baseDatasetLoader import BaseDatasetLoader
from typing import List
class FilesystemDatasetLoader(BaseDatasetLoader):
    DefaultExtensions = ['.jpg', '.png']

    def __init__(self, path: str, extensions: List[str] = None):
        self.path = path
        if extensions is None:
            extensions = FilesystemDatasetLoader.DefaultExtensions
        else:
            self.extensions = extensions
        self.files = None
        self.nextIndex = 0

    def load_dataset(self):
        if self.files is not None:
            return
        self.files = []
        for file in os.listdir(self.path):
            if file.endswith(tuple(self.extensions)):
                self.files.append(file)

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.nextIndex >= len(self.files):
            raise StopIteration
        file = self.files[self.nextIndex]
        self.nextIndex += 1
        return file
