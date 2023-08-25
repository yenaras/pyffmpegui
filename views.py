#!/usr/bin/env python3
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QWidget, QFileDialog
from collections import deque
from pathlib import Path
from convert import Converter
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
        self.updateStateWhenNoFiles()

    def updateStateWhenNoFiles(self):
        self.files_count = len(self.files)
        self.loadFilesButton.setEnabled(True)
        self.loadFilesButton.setFocus(True)
        self.convertButton.setEnabled(False)

    def _connectSignalsSlots(self):
        # connect load files
        self.loadFilesButton.clicked.connect(self.load_files)
        self.convertButton.clicked.connect(self.convert_files)

    def load_files(self):
        self.dstFileList.clear()

        # if text in Source Directory prompt, open file explorer in that directory
        if self.dirEdit.text():
            init_dir = self.dirEdit.text()

        # else open file explorer in home directory
        else:
            init_dir = str(Path.home())

        files, filter = QFileDialog.getOpenFileNames(
            self, "Choose Files to Convert", init_dir, filter=FILTERS
        )

        if len(files) > 0:
            fileExtension = filter[filter.index("*"): -1]
            self.source_extension = fileExtension
            src_dir_name = str(Path(files[0]).parent)
            self.dirEdit.setText(src_dir_name)
            for file in files:
                self.files.append(Path(file))
                self.srcFileList.addItem(file)
            self.files_count = len(self.files)
            self.updateStateWhenFilesLoaded()

    def updateStateWhenFilesLoaded(self):
        self.convertButton.setEnabled(True)
        self.convertButton.setFocus(True)

    def convert_files(self):
        self.run_convert_thread()

    def run_convert_thread(self):
        dest_extension = str(self.formatList.currentText())
        self.thread = QThread()
        self.converter = Converter(
            files=tuple(self.files),
            dest_extension=dest_extension,
        )
        self.converter.moveToThread(self.thread)
        # convert files with ffmpeg
        self.thread.started.connect(self.converter.convert_files)
        # update state
        self.converter.converted_file.connect(self.updateStateWhenFileConverted)
        self.converter.progressed.connect(self.update_progress_bar)
        self.converter.finished.connect(self.updateStateWhenNoFiles)
        # clean up
        self.converter.finished.connect(self.thread.quit)
        self.converter.finished.connect(self.converter.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # run the thread
        self.thread.start()

    def updateStateWhenFileConverted(self, new_file):
        self.files.popleft()
        self.srcFileList.takeItem(0)
        self.dstFileList.addItem(str(new_file))

    def update_progress_bar(self, file_number):
        progress_percent = int(file_number / self.files_count * 100)
        self.progressBar.setValue(progress_percent)
