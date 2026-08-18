import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineSettings
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QIcon, QDesktopServices

def get_asset_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

class CustomWebEnginePage(QWebEnginePage):
    def acceptNavigationRequest(self, url, nav_type, is_main_frame):
        url_str = url.toString()
        if "t.me" in url_str or (url_str.startswith("http") and not "speed.cloudflare.com" in url_str):
            QDesktopServices.openUrl(url)
            return False
        return super().acceptNavigationRequest(url, nav_type, is_main_frame)

class SpeedPulseMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SpeedPulse Pro — Multi-Scanner & Telemetry Suite")
        self.resize(430, 880)
        self.setMinimumSize(380, 700)

        # Set Icon
        ico_path = get_asset_path("speedpulse.ico")
        if os.path.exists(ico_path):
            self.setWindowIcon(QIcon(ico_path))

        # Setup WebEngineView
        self.browser = QWebEngineView()
        self.page = CustomWebEnginePage(self.browser)
        self.browser.setPage(self.page)

        # Enable features
        settings = self.browser.settings()
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalStorageEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.AllowRunningInsecureContent, True)

        html_path = get_asset_path("index.html")
        self.browser.load(QUrl.fromLocalFile(html_path))
        self.setCentralWidget(self.browser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ico_path = get_asset_path("speedpulse.ico")
    if os.path.exists(ico_path):
        app.setWindowIcon(QIcon(ico_path))

    window = SpeedPulseMainWindow()
    window.show()
    sys.exit(app.exec())
