# import tkinter as tk

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QApplication
from pytube import YouTube
from tkinter import filedialog

class YoutubeDownloader(QWidget):
    """This is the main widget for the Youtube Downloader"""

    def __init__(self):
        """Initizing"""

        super().__init__()
        self.setWindowTitle("PySide6 Youtube Downloader")
        self.init_ui()

    def init_ui(self):
        """This method initialize all the main variables of the will 
        be used to con build the structure of the widget"""

        # Url elements
        self.url_label = QLabel("URL")
        self.url_field = QLineEdit()

        # Folder elements
        self.download_folder_label = QPushButton("Download Folder")
        self.download_folder_label.clicked.connect(lambda:self.download_folder_field.setText(filedialog.askdirectory()))

        self.download_folder_field = QLineEdit()

        # Buttons elements
        self.download_button = QPushButton("Download")
        self.download_button.clicked.connect(self.download_video(self.url_field.text(), 
                                                                 self.download_folder_field.text()))
        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(lambda:QApplication.exit())

        # Layout elements
        self.url_layout = QHBoxLayout()
        self.folder_layout = QHBoxLayout()
        self.button_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        # Layout connections
        self.url_layout.addWidget(self.url_label)
        self.url_layout.addWidget(self.url_field)

        self.folder_layout.addWidget(self.download_folder_label)
        self.folder_layout.addWidget(self.download_folder_field)

        self.button_layout.addWidget(self.exit_button)
        self.button_layout.addWidget(self.download_button)

        self.v_layout.addLayout(self.url_layout)
        self.v_layout.addLayout(self.folder_layout)
        self.v_layout.addLayout(self.button_layout)

        # Setting the main layout
        self.setLayout(self.v_layout)

    def download_video(self, url, filepath):
        
        video_url = "https://www.youtube.com/watch?v=UY7ZP0KbBfI"
        yt = YouTube(video_url)
        stream_list = yt.streams
        
        for stream in stream_list:
            print(stream)
        
class StreamSelection(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 Youtube Downloader")
        self.init_ui()

    def init_ui(self):
        pass



    
    
    
        


        