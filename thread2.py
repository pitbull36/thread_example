import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot

import time

# set the UI file I need to use
Ui_MainWindow, QtBaseClass = uic.loadUiType("thread.ui")


# THREAD
class Worker(QObject):
    # here initialise variables for output
    message = pyqtSignal(str)
    finished = pyqtSignal()

    def heavy_function(self):
        self.message.emit("waiting...")
        time.sleep(5)
        self.message.emit("FINISHED WAITING!")
        self.finished.emit()


class MyApp(QMainWindow):

    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # connect the two buttons to their functions
        self.ui.b_waitdisplay.clicked.connect(self.start_thread)
        self.ui.b_numbers.clicked.connect(self.increasing_numbers)

        self.counter = 0

        
    def start_thread(self):

        self.ui.b_waitdisplay.setEnabled(False)

        self.thread = QThread() # create a QThread object
        self.worker = Worker() # create a worker object
        self.worker.moveToThread(self.thread) # move worker to the thread

        self.thread.start() # start the thread

        # connect signals and slots
        self.thread.started.connect(self.worker.heavy_function)
        self.thread.finished.connect(lambda: self.ui.b_waitdisplay.setEnabled(True))
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.message.connect(self.wait_and_display)

    
    def wait_and_display(self, message_from_thread):
        # time.sleep(5) # wait five seconds
        # self.ui.l_waitdisplay.setText("FINISHED WAITING!")
        self.ui.l_waitdisplay.setText(message_from_thread)

    def increasing_numbers(self):
        self.ui.l_numbers.setText(str(self.counter))
        self.counter+=1
 

   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MyApp()
    window.show()
    sys.exit(app.exec_())