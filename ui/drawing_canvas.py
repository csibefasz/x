from PyQt5.QtWidgets import QGraphicsView

class DrawingCanvas(QGraphicsView):
    def __init__(self, machine, serial_connection):  # Frissített konstruktor
        super().__init__()
        self.machine = machine
        self.serial = serial_connection
        self.init_ui()

    def init_ui(self):
        self.setSceneRect(0, 0, self.machine.max_x, self.machine.max_y)
        
        # Alap beállítások
        self.setRenderHint(QPainter.Antialiasing)  # Most már működik
        self.setBackgroundBrush(Qt.white)
        
        # Rajzolási változók
        self.drawing = False
        self.last_point = QPointF()
        
        # Eseménykezelők
        self.setMouseTracking(True)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = self.mapToScene(event.pos())
            self.send_pen_position(self.last_point, pen_down=True)
    
    def mouseMoveEvent(self, event):
        if self.drawing:
            current_point = self.mapToScene(event.pos())
        if (current_point - self.last_point).manhattanLength() > 5:  # Érzékenység csökkentése
            self.draw_line(self.last_point, current_point)
            self.last_point = current_point
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
            self.send_pen_position(self.last_point, pen_down=False)
    
    def draw_line(self, start, end):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        self.scene.addLine(start.x(), start.y(), end.x(), end.y(), pen)
    
    def send_pen_position(self, point, pen_down=None):
        """Pozíció küldése a robothoz"""
        x = point.x()
        y = self.machine.max_y - point.y()  # Y tengely megfordítása
        
        if pen_down is not None:
            if pen_down:
                self.serial.send_command("M3 S0")  # Toll le
            else:
                self.serial.send_command("M3 S250")  # Toll fel
        
        cmd = f"G0 X{x:.2f} Y{y:.2f}"
        self.serial.send_command(cmd)
