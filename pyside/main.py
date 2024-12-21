from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from main_window import Ui_MainWindow  # 导入生成的界面类

# 创建主窗口类
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # 创建界面类的实例
        self.ui.setupUi(self)      # 将界面设置到当前窗口上

        self.setup_control()


    def setup_control(self):
        self.ui.pushButton.clicked.connect(self.button_clicked)


    def button_clicked(self):
        ret = QMessageBox.information(
            self, 'Msg Box',
            'This is inline message box, with return',
            QMessageBox.Ok, QMessageBox.Cancel)
        print('press: ' + str(ret))



# 创建应用程序对象
app = QApplication([])

# 创建并显示主窗口
window = MainWindow()
window.show()

# 运行事件循环
app.exec()

