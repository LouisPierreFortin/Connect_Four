import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from demo_ui import Ui_MainWindow  # Importer la classe UI générée

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Créer une instance de la class UI
        self.ui.setupUi(self)  # Préparer la classe UI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
