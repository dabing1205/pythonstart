#!/usr/bin/env python
# -*- coding: utf-8

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf-8"))

class StockDialog(QDialog):
    def __init__(self, parent=None):
        super(StockDialog, self).__init__(parent)
        self.setWindowTitle(self.tr("综合布局实例"))
        
        mainSplitter = QSplitter(Qt.Horizontal)
        mainSplitter.setOpaqueResize(True)
        
        listWidget = QListWidget(mainSplitter)
        listWidget.insertItem(0, self.tr("个人基本资料"))
        listWidget.insertItem(1, self.tr("联系方式"))
        listWidget.insertItem(2, self.tr("详细信息"))
        
        
        stack = QStackedWidget()
        stack.setFrameStyle(QFrame.Panel|QFrame.Raised)
        
        baseInfo = BaseInfo()
        contact = Contact()
        detail = Detail()
        stack.addWidget(baseInfo)
        stack.addWidget(contact)
        stack.addWidget(detail)
        
        amendPushButton = QPushButton(self.tr("修改"))
        closePushButton = QPushButton(self.tr("关闭"))
        
        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(amendPushButton)
        buttonLayout.addWidget(closePushButton)
        
        frame = QFrame(mainSplitter)
        mainLayout = QVBoxLayout(frame)
        mainLayout.setMargin(10)
        mainLayout.setSpacing(6)
        mainLayout.addWidget(stack)
        mainLayout.addLayout(buttonLayout)
        
        self.connect(listWidget, SIGNAL("currentRowChanged(int)"), stack, SLOT("setCurrentIndex(int)"))
        self.connect(closePushButton, SIGNAL("clicked()"), self, SLOT("close()"))
        
        layout = QHBoxLayout(self)
        layout.addWidget(mainSplitter)
        self.setLayout(layout)
        
class BaseInfo(QWidget):
    def __init__(self, parent=None):
        super(BaseInfo, self).__init__(parent)
        
        label1 = QLabel(self.tr("用户名: "))
        label2 = QLabel(self.tr("姓名: "))
        label3 = QLabel(self.tr("性别: "))
        label4 = QLabel(self.tr("部门: "))
        label5 = QLabel(self.tr("年龄: "))
        otherlabel = QLabel(self.tr("备注"))
        otherlabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        nameLineEdit = QLineEdit()
        userLineEdit = QLineEdit()
        sexComboBox = QComboBox()
        sexComboBox.insertItem(0, self.tr("男"))
        sexComboBox.insertItem(1, self.tr("女"))
        departmentTextEdit = QTextEdit()
        ageLineEdit = QLineEdit()
        
        labelCol = 0
        contentCol = 1
        
        leftLayout = QGridLayout()
        leftLayout.addWidget(label1, 0, labelCol)
        leftLayout.addWidget(userLineEdit, 0, contentCol)
        leftLayout.addWidget(label2, 1, labelCol)
        leftLayout.addWidget(nameLineEdit, 1, contentCol)
        leftLayout.addWidget(label3, 2, labelCol)
        leftLayout.addWidget(sexComboBox, 2, contentCol)
        leftLayout.addWidget(label4, 3, labelCol)
        leftLayout.addWidget(departmentTextEdit, 3, contentCol)
        leftLayout.addWidget(label5, 4, labelCol)
        leftLayout.addWidget(ageLineEdit,4, contentCol)
        leftLayout.addWidget(otherlabel, 5, labelCol, 1, 2)
        leftLayout.setColumnStretch(0, 1)
        leftLayout.setColumnStretch(1, 3)
        
        label6 = QLabel(self.tr("头像"))
        iconLabel = QLabel()
        icon = QPixmap("3.bmp")
        iconLabel.setPixmap(icon)
        iconLabel.resize(icon.width(), icon.height())
        iconPushButton = QPushButton(self.tr("改变"))
        hLayout = QHBoxLayout()
        hLayout.setSpacing(20)
        hLayout.addWidget(label6)
        hLayout.addWidget(iconLabel)
        hLayout.addWidget(iconPushButton)
        
        label7 = QLabel(self.tr("个人说明"))
        descTextEdit = QTextEdit()
        
        rightLayout = QVBoxLayout()
        rightLayout.setMargin(10)
        rightLayout.addLayout(hLayout)
        rightLayout.addWidget(label7)
        rightLayout.addWidget(descTextEdit)
        
        mainLayout = QGridLayout(self)
        mainLayout.setMargin(15)
        mainLayout.setSpacing(10)
        mainLayout.addLayout(leftLayout, 0, 0)
        mainLayout.addLayout(rightLayout, 0, 1)
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        
class Contact(QWidget):
    def __init__(self, parent=None):
        super(Contact, self).__init__(parent)
        label1 = QLabel(self.tr("电子邮件: "))
        label2 = QLabel(self.tr("联系地址: "))
        label3 = QLabel(self.tr("邮政编码: "))
        label4 = QLabel(self.tr("移动电话: "))
        label5 = QLabel(self.tr("办公电话: "))
        
        mailLineEdit = QLineEdit()
        addressLineEdit = QLineEdit()
        codeLineEdit = QLineEdit()
        mpLineEdit = QLineEdit()
        phoneLineEdit = QLineEdit()
        receiveCheckBox = QCheckBox(self.tr("接受留言"))
        
        layout = QGridLayout(self)
        layout.addWidget(label1, 0, 0)
        layout.addWidget(mailLineEdit, 0, 1)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(addressLineEdit, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(codeLineEdit, 2, 1)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(mpLineEdit, 3, 1)
        layout.addWidget(receiveCheckBox, 3, 2)
        layout.addWidget(label5, 4, 0)
        layout.addWidget(phoneLineEdit, 4, 1)

class Detail(QWidget):
    def __init__(self, parent=None):
        super(Detail, self).__init__(parent)
        label1 = QLabel(self.tr("地区"))
        label2 = QLabel(self.tr("州"))
        label3 = QLabel(self.tr("城市"))
        label4 = QLabel(self.tr("个人说明"))
        
        countryComboBox = QComboBox()
        countryComboBox.addItem(self.tr("中国"))
        countryComboBox.addItem(self.tr("香港"))
        countryComboBox.addItem(self.tr("台北"))
        countryComboBox.addItem(self.tr("澳门"))
        
        provinceComboBox = QComboBox()
        provinceComboBox.addItem(self.tr("安徽"))
        provinceComboBox.addItem(self.tr("广西"))
        
        cityLineEdit = QLineEdit()
        remarkTextEdit = QTextEdit()
        
        layout = QGridLayout(self)
        layout.addWidget(label1, 0, 0)
        layout.addWidget(countryComboBox, 0, 1)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(provinceComboBox, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(cityLineEdit, 2, 1)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(remarkTextEdit, 3, 1)         
        
        


if __name__=='__main__':
    
    app = QApplication(sys.argv)
    form = StockDialog()
    form.show()
    app.exec_()