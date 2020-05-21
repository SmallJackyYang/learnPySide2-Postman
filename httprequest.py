from PySide2.QtWidgets import QApplication, QTableWidgetItem, QAbstractItemView
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon
from threading import Thread
import requests
import json


class Stats:
    def __init__(self):
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.window.button , self.window.textEdit
        self.window = QUiLoader().load('httptest.ui')
        # 设定第1列的宽度为 110像素
        self.window.tableWidget.setColumnWidth(0, 110)
        # 设定第2列的宽度为 170像素
        self.window.tableWidget.setColumnWidth(1, 170)
        # 让 表格控件宽度随着父窗口的缩放自动缩放
        self.window.tableWidget.horizontalHeader().setStretchLastSection(True)
        # 将发送按钮点击事件绑定到函数handsendrequest之上
        self.window.requestbutton.clicked.connect(self.handsendrequest)
        # 将清除按钮点击事件绑定到函数textBrowser之上
        self.window.clearbutton.clicked.connect(self.textbrowser)
        # 将添加消息头按钮点击事件绑定到函数showdialog之上
        self.window.addbutton.clicked.connect(self.showdialog)
        self.window.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 调用自定义函数一定要加上lambda！是个坑
        self.window.delete_2.clicked.connect(lambda: self.deleteheader())
        # 创建一个dialog对象，用于添加消息头使用，暂时不需要显示
        self.dialog = QUiLoader().load('dialog.ui')
        self.dialog.addheaderbutton.clicked.connect(lambda: self.addheader())

    # 点击按钮之后发送httprequest请求
    def handsendrequest(self):
        headers = {}
        # 获取消息头所有的数据，拼接成dict类型
        for temp_count in range(self.window.tableWidget.rowCount()):
            headers[self.window.tableWidget.item(temp_count, 0).text()] = self.window.tableWidget.item(temp_count, 1).text()
        if self.window.comboBox.currentText() == 'GET':
            data = json.loads(self.window.requestbody.toPlainText())
            # 使用多线程，防止主线程卡死的情况出现
            thread = Thread(target=self.threadgetsend, args=(self.window.urledit.text(), data, headers))
            thread.start()
        else:
            data = self.window.requestbody.toPlainText()
            thread = Thread(target=self.threadpostsend, args=(self.window.urledit.text(), data, headers))
            thread.start()

    # get方式参数名是params
    def threadgetsend(self, url, data, headers):
        res = requests.get(url, params=data, headers=headers)
        # 输出相关打印
        self.window.textBrowser.append('-----------------------发送GET请求----------------------')
        self.window.textBrowser.append('HTTP请求的返回状态：' + str(res.status_code))
        self.window.textBrowser.append('HTTP响应内容的Headers：' + str(res.headers))
        self.window.textBrowser.append('HTTP响应内容的字符串形式：' + str(res.text))
        self.window.textBrowser.append('HTTP响应正文的编码：' + str(res.encoding))

    # Post方式参数名为data
    def threadpostsend(self, url, data, headers):
        res = requests.post(url, data=data, headers=headers)
        self.window.textBrowser.append('-----------------------发送POST请求----------------------')
        self.window.textBrowser.append('HTTP请求的返回状态：' + str(res.status_code))
        self.window.textBrowser.append('HTTP响应内容的Headers：' + str(res.headers))
        self.window.textBrowser.append('HTTP响应内容的字符串形式：' + str(res.text))
        self.window.textBrowser.append('HTTP响应正文的编码：' + str(res.encoding))

    def textbrowser(self):
        # 清除textBrowser内的所有内容
        self.window.textBrowser.clear()

    def showdialog(self):
        # 显示dialog，并初始化两个输入框
        self.dialog.show()
        self.dialog.lineEdit.clear()
        self.dialog.lineEdit_2.clear()

    def addheader(self):
        # 创建新的一行之后  将之前dialog界面输入的两个值插入其中
        self.window.tableWidget.insertRow(0)
        self.window.tableWidget.setItem(0, 0, QTableWidgetItem(self.dialog.lineEdit.text()))
        self.window.tableWidget.setItem(0, 1, QTableWidgetItem(self.dialog.lineEdit_2.text()))
        self.dialog.close()

    def deleteheader(self):
        # 选中之后，执行删除对应行的操作
        if self.window.tableWidget.currentRow() != -1:
            self.window.tableWidget.removeRow(self.window.tableWidget.currentRow())


if __name__ == '__main__':
    # 在创建控件对象之前，先创建对象app
    app = QApplication([])
    # 加载 icon
    app.setWindowIcon(QIcon('logo.png'))
    # 实例化一个Stats类
    stats = Stats()
    # 放在主窗口的控件，要能全部显示在界面上， 必须加上下面这行代码
    stats.window.show()
    # 进入QApplication的事件处理循环，接收用户的输入事件
    app.exec_()