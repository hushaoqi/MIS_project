import sys

from PyQt5.QtWidgets import QApplication

from ctrl.sys_control import Systemdatasetting

if __name__ == '__main__':
    app = QApplication(sys.argv)
    on = Systemdatasetting()
    on.setupUi(on)
    on.show()

    sys.exit(app.exec_())
