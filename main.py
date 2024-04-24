"""
This is a simple Youtube Downloader using pytube and PySide6
"""
import sys

from PySide6.QtWidgets import QApplication
from widget import YoutubeDownloader   

if __name__ == "__main__":    
    app = QApplication(sys.argv)
    widget = YoutubeDownloader()
    widget.show()
    sys.exit(app.exec())     