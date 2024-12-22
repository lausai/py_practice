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
        self.ui.pushButton1.clicked.connect(self.button1_clicked)
        self.ui.pushButton2.clicked.connect(self.button2_clicked)


    def button1_clicked(self):
        ret = QMessageBox.information(
            self, 'Msg Box',
            'Hello tab1',
            QMessageBox.Ok, QMessageBox.Cancel)
        print('press: ' + str(ret))


    def button2_clicked(self):
        ret = QMessageBox.information(
            self, 'Msg Box',
            'Hello tab2',
            QMessageBox.Ok, QMessageBox.Cancel)
        print('press: ' + str(ret))



# 创建应用程序对象
app = QApplication([])

# 创建并显示主窗口
window = MainWindow()
window.show()

# 运行事件循环
app.exec()

