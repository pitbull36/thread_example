import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

import time

# set the UI file I need to use
Ui_MainWindow, QtBaseClass = uic.loadUiType("thread.ui")

class MyApp(QMainWindow):

    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # connect the two buttons to their functions
        self.ui.b_waitdisplay.clicked.connect(self.wait_and_display)
        self.ui.b_numbers.clicked.connect(self.increasing_numbers)

        self.counter = 0 # this will be my counter; its value will be the displayed number

    def wait_and_display(self):
        self.ui.b_waitdisplay.setEnabled(False) # disable button

        self.ui.l_waitdisplay.setText("waiting...")
        time.sleep(5) # wait five seconds
        self.ui.l_waitdisplay.setText("FINISHED WAITING!")

        self.ui.b_waitdisplay.setEnabled(True) # re-enable button

    def increasing_numbers(self):
        self.ui.l_numbers.setText(str(self.counter)) # display the current counter value
        self.counter+=1 # increase the counter

   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MyApp()
    window.show()
    sys.exit(app.exec_())