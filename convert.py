#!/usr/bin/env python3
from pathlib import Path
from PyQt5.QtCore import QObject, pyqtSignal
import ffmpeg


class Converter(QObject):
    # Define custom signals
    progressed = pyqtSignal(int)
    converted_files = pyqtSignal(Path)
    finished = pyqtSignal()

    def __init__(self, files, src_extension, dest_extension):
        super().__init__()
        self.files = files
        self.src_extension = src_extension
        self.dest_extension = dest_extension

    # TODO: convert files with ffmpeg based on suffix and convert option
    def convertFiles(self):
        ...
