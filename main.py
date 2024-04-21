from PySide6.QtWidgets import QApplication
from widget import YoutubeDownloader   

import sys

if __name__ == "__main__":    
    app = QApplication(sys.argv)
    widget = YoutubeDownloader()
    widget.show()
    sys.exit(app.exec())