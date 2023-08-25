#!/usr/bin/env python3
from pathlib import Path
from PyQt5.QtCore import QObject, pyqtSignal
import ffmpeg


class Converter(QObject):
    # Define custom signals
    progressed = pyqtSignal(int)
    converted_file = pyqtSignal(Path)
    finished = pyqtSignal()

    def __init__(self, files, dest_extension):
        super().__init__()
        self.files = files
        self.dest_extension = dest_extension

    # TODO: convert files with ffmpeg based on suffix and convert option
    def convert_files(self):
        for file_number, file in enumerate(self.files, 1):
            new_file = file.parent.joinpath(
                f"{file.with_suffix(self.dest_extension)}"
            )
            ffmpeg.input(str(file)).output(str(new_file)).run()
            self.progressed.emit(file_number)
            self.converted_file.emit(new_file)
        self.progressed.emit(0)
        self.finished.emit()
