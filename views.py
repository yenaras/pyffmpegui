#!/usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QFileDialog
from collections import deque
from pathlib import Path

from window import Ui_Window

FILTERS = ";;".join(
    (
        "MP4 Files (*.mp4)",
        "MKV Files (*.mkv)",
        "GIF Files (*.gif)",
    )
)


class Window(QWidget, Ui_Window):
    def __init__(self):
        super().__init__()
        self.files = deque()
        self.files_count = len(self.files)
        self._setupUI()
        self._connectSignalsSlots()

    def _setupUI(self):
        self.setupUi(self)

    def _connectSignalsSlots(self):
        # connect load files
        self.loadFilesButton.clicked.connect(self.load_files)

    def load_files(self):
        self.dstFileList.clear()

        # if text in Source Directory prompt, open file explorer in that directory
        if self.dirEdit.text():
            init_dir = self.dirEdit.text()

        # else open file explorer in home directory
        else:
            init_dir = str(Path.home())

        files, filters = QFileDialog.getOpenFileNames(
            self, "Choose Files to Convert", init_dir, filter=FILTERS
        )

        if len(files) > 0:
            fileExtension = filter[filter.index("*"): -1]
            self.source_extension = fileExtension
            self.dest_extension = self.formatList
            src_dir_name = str(Path(files[0]).parent)
            self.dirEdit.setText(src_dir_name)
            for file in files:
                self.files.append(Path(file))
                self.srcFileList.addItem(file)
            self.files_count = len(self.files)
