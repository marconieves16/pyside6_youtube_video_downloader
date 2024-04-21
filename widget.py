from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout

class YoutubeDownloader(QWidget):


    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 Youtube Downloader")
        self.init_ui()

    def init_ui(self):

        # Url elements
        self.url_label = QLabel("URL")
        self.url_field = QLineEdit()

        # Folder elements
        self.download_folder_label = QLabel("Download Folder")
        self.download_folder_field = QLineEdit()

        # Buttons elements
        self.download_button = QPushButton("Download")
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


        