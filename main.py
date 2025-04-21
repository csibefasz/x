import sys
from PyQt5.QtWidgets import QApplication
from core.machine import Machine
from core.state_manager import StateManager
from ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    machine = Machine()
    state = StateManager()
    window = MainWindow(machine, state)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
