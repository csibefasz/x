import serial
import serial.tools.list_ports
from PyQt5.QtCore import QObject, pyqtSignal

class SerialConnection(QObject):
    connection_changed = pyqtSignal(bool)
    data_received = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.serial = None
        self.connected = False

    def connect(self, port, baudrate=115200):
        try:
            self.serial = serial.Serial(port, baudrate, timeout=1)
            self.connected = True
            self.connection_changed.emit(True)
            return True
        except Exception as e:
            print(f"Hiba: {e}")
            return False

    def send_command(self, command):
        if self.connected:
            self.serial.write(f"{command}\n".encode())

    def read_response(self):
        return self.serial.readline().decode().strip() if self.connected else ""
