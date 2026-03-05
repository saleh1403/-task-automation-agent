import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QTextEdit, QWidget, QMessageBox
import logging
from datetime import datetime

class TaskManagementApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.init_logging()

    def init_ui(self):
        self.setWindowTitle('Task Management App')
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        self.task_input = QTextEdit()
        self.task_input.setPlaceholderText('Enter your task here...')
        layout.addWidget(self.task_input)

        self.add_task_button = QPushButton('Add Task')
        self.add_task_button.clicked.connect(self.add_task)
        layout.addWidget(self.add_task_button)

        self.task_log = QTextEdit()
        self.task_log.setReadOnly(True)
        layout.addWidget(self.task_log)

        central_widget.setLayout(layout)

    def init_logging(self):
        logging.basicConfig(filename='task_manager.log', level=logging.INFO)
        logging.info(f'[{self.get_current_time()}] Application started')

    def add_task(self):
        task = self.task_input.toPlainText().strip()
        if task:
            self.task_log.append(f'[{self.get_current_time()}] Task Added: {task}')
            logging.info(f'[{self.get_current_time()}] Task Added: {task}')
            self.task_input.clear()
        else:
            QMessageBox.warning(self, 'Input Error', 'Please enter a task!')

    def get_current_time(self):
        return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = TaskManagementApp()
    main_win.show()
    sys.exit(app.exec())