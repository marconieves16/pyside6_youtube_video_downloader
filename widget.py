from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
from pytube import YouTube

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
        self.download_folder_label.clicked.connect(self.select_download_folder())

        self.download_folder_field = QLineEdit()

        # Buttons elements
        self.download_button = QPushButton("Download")
        self.download_button.clicked.connect(self.download_video(self.url_field.text(), 
                                                                 self.download_folder_field.text()))
        self.quit_button = QPushButton("Quit")

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

        self.button_layout.addWidget(self.quit_button)
        self.button_layout.addWidget(self.download_button)

        self.v_layout.addLayout(self.url_layout)
        self.v_layout.addLayout(self.folder_layout)
        self.v_layout.addLayout(self.button_layout)

        # Setting the main layout
        self.setLayout(self.v_layout)

    def download_video(self, url, filepath):
        """
        video_url = "https://www.youtube.com/watch?v=UY7ZP0KbBfI"
        yt = YouTube(video_url)
        stream_list = yt.streams
        
        for stream in stream_list:
            print(stream)
        """

    def select_download_folder(self):
        pass
        


        