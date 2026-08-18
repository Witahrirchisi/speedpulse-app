import os
import sys
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtGui import QIcon, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineSettings, QWebEngineProfile

def get_asset_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

class SpeedPulseMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SpeedPulse — Real-Time Network Speed")
        self.resize(430, 890)
        self.setMinimumSize(380, 700)
        
        # Set icon
        ico_path = get_asset_path("speedpulse.ico")
        if os.path.exists(ico_path):
            self.setWindowIcon(QIcon(ico_path))

        # Central WebEngine View
        self.browser = QWebEngineView(self)
        self.setCentralWidget(self.browser)

        # Configure Settings
        settings = self.browser.settings()
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.Accelerated2dCanvasEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.WebGLEnabled, True)

        # Background color
        self.setStyleSheet("background-color: #050608;")

        # Load HTML
        html_path = get_asset_path("index.html")
        if os.path.exists(html_path):
            self.browser.setUrl(QUrl.fromLocalFile(html_path))
        else:
            print("HTML file not found:", html_path)

def main():
    # Enable High DPI scaling
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    
    app = QApplication(sys.argv)
    app.setApplicationName("SpeedPulse")
    
    ico_path = get_asset_path("speedpulse.ico")
    if os.path.exists(ico_path):
        app.setWindowIcon(QIcon(ico_path))

    window = SpeedPulseMainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
