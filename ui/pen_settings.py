from PyQt5.QtWidgets import QDialog, QVBoxLayout, QSlider, QLabel

class PenSettings(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Toll Beállítások")
        
        layout = QVBoxLayout()
        
        # Toll nyomás szabályzó
        self.pressure_slider = QSlider(Qt.Horizontal)
        self.pressure_slider.setRange(0, 300)
        layout.addWidget(QLabel("Toll nyomás:"))
        layout.addWidget(self.pressure_slider)
        
        self.setLayout(layout)
