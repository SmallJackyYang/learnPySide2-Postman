# Pyside2-Postman
最近有时间，又回到了Python的学习中，之前看过QT界面的相关资料，自己学习也想尝试一下

具体参照的工具是POSTMAN，用过的朋友可能比较熟悉（原谅我做的功能非常简陋）

纯粹当成一个入门的学习吧，要使用到项目中还需要更多的深入学习

简单说一下里面的一些细节吧

## import相关
```python
from PySide2.QtWidgets import QApplication, QTableWidgetItem, QAbstractItemView
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon
from threading import Thread
import requests
import json
```
引入PySide2 QtWidgets界面需要相关东西，这里其实少了很多引入，因为直接使用了QUiLoader，在QT designer里已经设计好界面的排版，文件里也一并上传，可直接使用designer打开查看

QIcon用于添加主窗口图标，使用的是png格式图标

多线程Thread 与requests 还有 json库就不额外多说了

## 其它代码
代码里注释都已经写的比较详细，其实功能挺简单的，会python的朋友都能轻松掌握

## 关于打包
打包使用 pyinstaller，cmd到当前目录 使用pyinstaller httprequest.py -F --noconsole --hidden-import PySide2.QtXml --icon="logo.ico" 

打包这里有几条注意事项

1.-F ： 打包完成后只有一个单独的EXE文件，个人比较喜欢这种方式

2.--hidden-import PySide2.QtXml : 因为这个 QtXml库是动态导入，PyInstaller没法分析出来，需要我们告诉它

3.--icon : 应用程序图标  ,这个与下面python代码中png图标不是同一个，下面代表的是主窗口图标
``` python
    # 加载 icon
    app.setWindowIcon(QIcon('logo.png'))
```

4.打包完成后，需要将.ui 文件与png文件 放到同一个目录下，因为程序动态打开的资源文件，比如 图片、excel、ui这些，它是不会帮你打包的

#### 觉得对你有帮助的话，star下哦。
