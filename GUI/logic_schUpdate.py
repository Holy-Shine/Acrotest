from ui_schUpdateWin import Ui_SchUpdate

from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon

class logicSchUpdate(Ui_SchUpdate, QDialog):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        
        self.btn_search.setIcon(QIcon('resource/search.png'))