from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from ui.connection_panel import ConnectionPanel
from ui.drawing_canvas import DrawingCanvas
from core.serial_connection import SerialConnection  # Új import

class MainWindow(QMainWindow):
    def __init__(self, machine, state):
        super().__init__()
        self.machine = machine
        self.state = state
        self.serial = SerialConnection()  # Új sor
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        layout.addWidget(ConnectionPanel(self.machine))
        layout.addWidget(DrawingCanvas(self.machine, self.serial))  # Javított sor
        
        central_widget.setLayout(layout)
