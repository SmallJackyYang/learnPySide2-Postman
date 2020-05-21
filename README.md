# Pyside2-Postman
最近有时间，又回到了Python的学习中，之前看过QT界面的相关资料，自己学习也想尝试一下

具体参照的工具是POSTMAN，用过的朋友可能比较熟悉（原谅我做的功能非常简陋）

纯粹当成一个入门的学习吧，要使用到项目中还需要更多的深入学习

简单说一下里面的一些细节吧

# import相关
```python
from PySide2.QtWidgets import QApplication, QTableWidgetItem, QAbstractItemView
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon
from threading import Thread
import requests
import json
```
