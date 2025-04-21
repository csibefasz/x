from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, 
                             QPushButton, QLabel, QDoubleSpinBox, QSlider)
from PyQt5.QtCore import Qt

class ControlPanel(QWidget):
    def __init__(self, machine, serial_connection, parent=None):
        super().__init__(parent)
        self.machine = machine
        self.serial = serial_connection
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Mozgató gombok
        move_group = QGroupBox("Kézi vezérlés")
        move_layout = QVBoxLayout()
        
        # X tengely
        x_layout = QHBoxLayout()
        self.x_minus_btn = QPushButton("X-")
        self.x_minus_btn.clicked.connect(lambda: self.move_relative(-10, 0))
        x_layout.addWidget(self.x_minus_btn)
        
        self.x_plus_btn = QPushButton("X+")
        self.x_plus_btn.clicked.connect(lambda: self.move_relative(10, 0))
        x_layout.addWidget(self.x_plus_btn)
        move_layout.addLayout(x_layout)
        
        # Y tengely
        y_layout = QHBoxLayout()
        self.y_minus_btn = QPushButton("Y-")
        self.y_minus_btn.clicked.connect(lambda: self.move_relative(0, -10))
        y_layout.addWidget(self.y_minus_btn)
        
        self.y_plus_btn = QPushButton("Y+")
        self.y_plus_btn.clicked.connect(lambda: self.move_relative(0, 10))
        y_layout.addWidget(self.y_plus_btn)
        move_layout.addLayout(y_layout)
        
        move_group.setLayout(move_layout)
        layout.addWidget(move_group)
        
        # Toll vezérlés
        pen_group = QGroupBox("Toll vezérlés")
        pen_layout = QHBoxLayout()
        
        self.pen_up_btn = QPushButton("Toll fel")
        self.pen_up_btn.clicked.connect(self.pen_up)
        pen_layout.addWidget(self.pen_up_btn)
        
        self.pen_down_btn = QPushButton("Toll le")
        self.pen_down_btn.clicked.connect(self.pen_down)
        pen_layout.addWidget(self.pen_down_btn)
        
        pen_group.setLayout(pen_layout)
        layout.addWidget(pen_group)
        
        # Pontos pozícionálás
        precision_group = QGroupBox("Pontos pozícionálás")
        precision_layout = QVBoxLayout()
        
        # X pozíció
        x_pos_layout = QHBoxLayout()
        x_pos_layout.addWidget(QLabel("X:"))
        self.x_pos_spin = QDoubleSpinBox()
        self.x_pos_spin.setRange(0, self.machine.max_x)
        self.x_pos_spin.setSuffix(" mm")
        x_pos_layout.addWidget(self.x_pos_spin)
        precision_layout.addLayout(x_pos_layout)
        
        # Y pozíció
        y_pos_layout = QHBoxLayout()
        y_pos_layout.addWidget(QLabel("Y:"))
        self.y_pos_spin = QDoubleSpinBox()
        self.y_pos_spin.setRange(0, self.machine.max_y)
        self.y_pos_spin.setSuffix(" mm")
        y_pos_layout.addWidget(self.y_pos_spin)
        precision_layout.addLayout(y_pos_layout)
        
        # Gomb a pozícionáláshoz
        self.go_to_btn = QPushButton("Mozgatás")
        self.go_to_btn.clicked.connect(self.go_to_position)
        precision_layout.addWidget(self.go_to_btn)
        
        precision_group.setLayout(precision_layout)
        layout.addWidget(precision_group)
        
        self.setLayout(layout)
    
    def move_relative(self, dx, dy):
        """Relatív mozgatás"""
        cmd = f"G91\nG0 X{dx} Y{dy}\nG90"
        self.serial.send_command(cmd)
    
    def pen_up(self):
        self.serial.send_command("M3 S250")
    
    def pen_down(self):
        self.serial.send_command("M3 S0")
    
    def go_to_position(self):
        """Abszolút pozícionálás"""
        x = self.x_pos_spin.value()
        y = self.y_pos_spin.value()
        cmd = f"G90\nG0 X{x} Y{y}"
        self.serial.send_command(cmd)
