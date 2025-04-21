from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from ui.connection_panel import ConnectionPanel
from ui.drawing_canvas import DrawingCanvas

class MainWindow(QMainWindow):
    def __init__(self, machine, state):
        super().__init__()
        self.machine = machine
        self.state = state
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        layout.addWidget(ConnectionPanel(self.machine))
        layout.addWidget(DrawingCanvas(self.machine))
        
        central_widget.setLayout(layout)
        self.setWindowTitle("Rajzoló Robot")
