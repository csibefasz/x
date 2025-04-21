from PyQt5.QtWidgets import (QGroupBox, QVBoxLayout, QHBoxLayout, 
                            QPushButton, QLabel, QComboBox)
from PyQt5.QtCore import Qt

class ConnectionPanel(QGroupBox):
    def __init__(self, machine):
        super().__init__("Kapcsolat")
        self.machine = machine
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        # Port választó
        port_layout = QHBoxLayout()
        port_layout.addWidget(QLabel("Port:"))
        self.port_combo = QComboBox()
        port_layout.addWidget(self.port_combo)
        layout.addLayout(port_layout)
        
        # Kapcsolódás gomb
        self.connect_btn = QPushButton("Kapcsolódás")
        layout.addWidget(self.connect_btn)
        
        self.setLayout(layout)
