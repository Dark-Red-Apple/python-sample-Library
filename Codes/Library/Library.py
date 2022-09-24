#Author:Alma, 2019

#****************check
#I copied function below from the internet
#Because of the error: qtcore.dll import when using pyinstaller to produce exe file
#I tried to use --add-data --paths --hidden-import options during pyinstaller command, but I was not sucessful
#Apparently, there is a problem with dynamic path of the program and modules imported

import os
import sys
import logging

def _append_run_path():
    if getattr(sys, 'frozen', False):
        pathlist = []

        # If the application is run as a bundle, the pyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.
        pathlist.append(sys._MEIPASS)

        # the application exe path
        _main_app_path = os.path.dirname(sys.executable)
        pathlist.append(_main_app_path)

        # append to system path enviroment
        os.environ["PATH"] += os.pathsep + os.pathsep.join(pathlist)

    logging.error("current PATH: %s", os.environ['PATH'])
    
_append_run_path()
##################

from PyQt5 import QtCore, QtGui, QtWidgets
#Alma
import os
from books import books
from customers import customers
from checkout import checkout
from configue import create_database
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtGui import QIcon, QPixmap
create_database()
#check the database
if(os.path.isfile('./library.sqlite')):
    if(not books.list_books('Select COUNT(*) from books')[0][0]):
        books.build_sample_books('./media/default_books.json')
    if(not customers.list_customers('Select COUNT(*) from customers')[0][0]):
        customers.register(['alma','zia','9-4-1990','female'])
#High resolution screens
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(692, 406)
        #Alma
        MainWindow.setWindowIcon(QtGui.QIcon('media/icon.png'))        

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.mainTabs.setGeometry(QtCore.QRect(20, 10, 651, 371))
        self.mainTabs.setObjectName("mainTabs")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.label_9 = QtWidgets.QLabel(self.Home)
        self.label_9.setGeometry(QtCore.QRect(30, 50, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(36)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setAutoFillBackground(True)
        self.label_9.setObjectName("label_9")
        self.mainTabs.addTab(self.Home, "")
        self.addBooksTab = QtWidgets.QWidget()
        self.addBooksTab.setObjectName("addBooksTab")
        self.label_3 = QtWidgets.QLabel(self.addBooksTab)
        self.label_3.setGeometry(QtCore.QRect(30, 40, 39, 11))
        self.label_3.setObjectName("label_3")
        self.bookNameText = QtWidgets.QLineEdit(self.addBooksTab)
        self.bookNameText.setGeometry(QtCore.QRect(160, 30, 301, 31))
        self.bookNameText.setObjectName("bookNameText")
        self.label_4 = QtWidgets.QLabel(self.addBooksTab)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 39, 11))
        self.label_4.setObjectName("label_4")
        self.bookAuthorText = QtWidgets.QLineEdit(self.addBooksTab)
        self.bookAuthorText.setGeometry(QtCore.QRect(160, 80, 301, 31))
        self.bookAuthorText.setObjectName("bookAuthorText")
        self.label_5 = QtWidgets.QLabel(self.addBooksTab)
        self.label_5.setGeometry(QtCore.QRect(30, 130, 91, 16))
        self.label_5.setObjectName("label_5")
        self.bookDateText = QtWidgets.QLineEdit(self.addBooksTab)
        self.bookDateText.setGeometry(QtCore.QRect(160, 130, 301, 31))
        self.bookDateText.setObjectName("bookDateText")
        self.label_6 = QtWidgets.QLabel(self.addBooksTab)
        self.label_6.setGeometry(QtCore.QRect(30, 190, 39, 11))
        self.label_6.setObjectName("label_6")
        self.bookSummaryText = QtWidgets.QLineEdit(self.addBooksTab)
        self.bookSummaryText.setGeometry(QtCore.QRect(160, 180, 301, 91))
        self.bookSummaryText.setObjectName("bookSummaryText")
        self.bookAvailableCheck = QtWidgets.QCheckBox(self.addBooksTab)
        self.bookAvailableCheck.setGeometry(QtCore.QRect(160, 290, 59, 15))
        self.bookAvailableCheck.setObjectName("bookAvailableCheck")
        self.label_13 = QtWidgets.QLabel(self.addBooksTab)
        self.label_13.setGeometry(QtCore.QRect(30, 290, 71, 16))
        self.label_13.setObjectName("label_13")
        self.addBookClearButton = QtWidgets.QPushButton(self.addBooksTab)
        self.addBookClearButton.setGeometry(QtCore.QRect(400, 300, 62, 19))
        self.addBookClearButton.setObjectName("addBookClearButton")
        self.addBooktButton = QtWidgets.QPushButton(self.addBooksTab)
        self.addBooktButton.setGeometry(QtCore.QRect(320, 300, 62, 19))
        self.addBooktButton.setObjectName("addBooktButton")
        self.mainTabs.addTab(self.addBooksTab, "")
        self.CheckoutBooksTab = QtWidgets.QWidget()
        self.CheckoutBooksTab.setObjectName("CheckoutBooksTab")
        self.bookList = QtWidgets.QListView(self.CheckoutBooksTab)
        self.bookList.setGeometry(QtCore.QRect(160, 170, 451, 81))
        self.bookList.setAccessibleName("")
        self.bookList.setObjectName("bookList")
        self.label = QtWidgets.QLabel(self.CheckoutBooksTab)
        self.label.setGeometry(QtCore.QRect(40, 30, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.CheckoutBooksTab)
        self.label_2.setGeometry(QtCore.QRect(40, 170, 161, 21))
        self.label_2.setObjectName("label_2")
        self.searchBookText = QtWidgets.QLineEdit(self.CheckoutBooksTab)
        self.searchBookText.setGeometry(QtCore.QRect(160, 30, 301, 31))
        self.searchBookText.setAccessibleName("")
        self.searchBookText.setObjectName("searchBookText")
        self.label_12 = QtWidgets.QLabel(self.CheckoutBooksTab)
        self.label_12.setGeometry(QtCore.QRect(40, 80, 161, 21))
        self.label_12.setObjectName("label_12")
        self.custemerIdText = QtWidgets.QLineEdit(self.CheckoutBooksTab)
        self.custemerIdText.setGeometry(QtCore.QRect(160, 80, 301, 31))
        self.custemerIdText.setAccessibleName("")
        self.custemerIdText.setObjectName("custemerIdText")
        self.checkoutClearButton = QtWidgets.QPushButton(self.CheckoutBooksTab)
        self.checkoutClearButton.setGeometry(QtCore.QRect(540, 280, 62, 19))
        self.checkoutClearButton.setObjectName("checkoutClearButton")
        self.checkoutButton = QtWidgets.QPushButton(self.CheckoutBooksTab)
        self.checkoutButton.setGeometry(QtCore.QRect(470, 280, 62, 19))
        self.checkoutButton.setObjectName("checkoutButton")
        self.refreshBooksButton = QtWidgets.QPushButton(self.CheckoutBooksTab)
        self.refreshBooksButton.setGeometry(QtCore.QRect(570, 140, 41, 19))
        self.refreshBooksButton.setObjectName("refreshBooksButton")
        self.label_10 = QtWidgets.QLabel(self.CheckoutBooksTab)
        self.label_10.setGeometry(QtCore.QRect(310, 120, 151, 20))
        self.label_10.setObjectName("label_10")
        self.mainTabs.addTab(self.CheckoutBooksTab, "")
        self.registerCustomerTab = QtWidgets.QWidget()
        self.registerCustomerTab.setObjectName("registerCustomerTab")
        self.label_7 = QtWidgets.QLabel(self.registerCustomerTab)
        self.label_7.setGeometry(QtCore.QRect(40, 100, 39, 11))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.registerCustomerTab)
        self.label_8.setGeometry(QtCore.QRect(40, 50, 39, 11))
        self.label_8.setObjectName("label_8")
        self.customerNameText = QtWidgets.QLineEdit(self.registerCustomerTab)
        self.customerNameText.setGeometry(QtCore.QRect(170, 40, 301, 31))
        self.customerNameText.setAccessibleName("")
        self.customerNameText.setObjectName("customerNameText")
        self.customerFamilyText = QtWidgets.QLineEdit(self.registerCustomerTab)
        self.customerFamilyText.setGeometry(QtCore.QRect(170, 90, 301, 31))
        self.customerFamilyText.setObjectName("customerFamilyText")
        self.label_14 = QtWidgets.QLabel(self.registerCustomerTab)
        self.label_14.setGeometry(QtCore.QRect(40, 150, 39, 11))
        self.label_14.setObjectName("label_14")
        self.customerBirthdayText = QtWidgets.QLineEdit(self.registerCustomerTab)
        self.customerBirthdayText.setGeometry(QtCore.QRect(170, 140, 301, 31))
        self.customerBirthdayText.setObjectName("customerBirthdayText")
        self.label_15 = QtWidgets.QLabel(self.registerCustomerTab)
        self.label_15.setGeometry(QtCore.QRect(40, 200, 39, 11))
        self.label_15.setObjectName("label_15")
        self.customerFemaleRadio = QtWidgets.QRadioButton(self.registerCustomerTab)
        self.customerFemaleRadio.setGeometry(QtCore.QRect(170, 200, 69, 15))
        self.customerFemaleRadio.setObjectName("customerFemaleRadio")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.customerFemaleRadio)
        self.customerMaleRadio = QtWidgets.QRadioButton(self.registerCustomerTab)
        self.customerMaleRadio.setGeometry(QtCore.QRect(250, 200, 69, 15))
        self.customerMaleRadio.setObjectName("customerMaleRadio")
        self.buttonGroup.addButton(self.customerMaleRadio)
        self.registerClearButton = QtWidgets.QPushButton(self.registerCustomerTab)
        self.registerClearButton.setGeometry(QtCore.QRect(410, 260, 62, 19))
        self.registerClearButton.setObjectName("registerClearButton")
        self.registerButton = QtWidgets.QPushButton(self.registerCustomerTab)
        self.registerButton.setGeometry(QtCore.QRect(330, 260, 62, 19))
        self.registerButton.setObjectName("registerButton")
        self.mainTabs.addTab(self.registerCustomerTab, "")
        self.customersListTab = QtWidgets.QWidget()
        self.customersListTab.setObjectName("customersListTab")
        self.label_31 = QtWidgets.QLabel(self.customersListTab)
        self.label_31.setGeometry(QtCore.QRect(60, 20, 131, 16))
        self.label_31.setObjectName("label_31")
        self.customersList = QtWidgets.QListView(self.customersListTab)
        self.customersList.setGeometry(QtCore.QRect(60, 50, 511, 231))
        self.customersList.setObjectName("customersList")
        self.refreshCustomersButton = QtWidgets.QPushButton(self.customersListTab)
        self.refreshCustomersButton.setGeometry(QtCore.QRect(530, 20, 41, 19))
        self.refreshCustomersButton.setObjectName("refreshCustomersButton")
        self.mainTabs.addTab(self.customersListTab, "")
        self.checkoutHistoryTab = QtWidgets.QWidget()
        self.checkoutHistoryTab.setObjectName("checkoutHistoryTab")
        self.checkoutHistoryText = QtWidgets.QListView(self.checkoutHistoryTab)
        self.checkoutHistoryText.setGeometry(QtCore.QRect(60, 50, 511, 231))
        self.checkoutHistoryText.setObjectName("checkoutHistoryText")
        self.label_11 = QtWidgets.QLabel(self.checkoutHistoryTab)
        self.label_11.setGeometry(QtCore.QRect(60, 20, 131, 16))
        self.label_11.setObjectName("label_11")
        self.refreshcheckoutsButton = QtWidgets.QPushButton(self.checkoutHistoryTab)
        self.refreshcheckoutsButton.setGeometry(QtCore.QRect(530, 20, 41, 19))
        self.refreshcheckoutsButton.setObjectName("refreshcheckoutsButton")
        self.mainTabs.addTab(self.checkoutHistoryTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionyg = QtWidgets.QAction(MainWindow)
        self.actionyg.setObjectName("actionyg")
        self.actionList_books = QtWidgets.QAction(MainWindow)
        self.actionList_books.setObjectName("actionList_books")
        self.actionCheckout_Books = QtWidgets.QAction(MainWindow)
        self.actionCheckout_Books.setCheckable(False)
        self.actionCheckout_Books.setObjectName("actionCheckout_Books")
        self.actionUpdate_Customer_Info = QtWidgets.QAction(MainWindow)
        self.actionUpdate_Customer_Info.setObjectName("actionUpdate_Customer_Info")

        self.retranslateUi(MainWindow)
        self.mainTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    #Alma start
        
        self.bookList.clicked[QtCore.QModelIndex].connect(self.on_click_select_book)        
        self.checkoutButton.clicked.connect(self.on_click_checkout)        
        self.checkoutClearButton.clicked.connect(self.checkout_clear)        
        self.searchBookText.textChanged.connect(self.search_item)        
        self.addBooktButton.clicked.connect(self.on_click_addbook)
        self.addBookClearButton.clicked.connect(self.add_book_clear)
        self.refreshBooksButton.clicked.connect(lambda: self.list_of_books('Select book_no, name, author from books'))        
        self.registerButton.clicked.connect(self.register_customer)        
        self.registerClearButton.clicked.connect(self.customer_register_clear)
        self.list_checkouts('Select * from checkout')
        self.list_customers('Select * from customers')
        #****************check
        #This should be after list_checkouts above or will not work correctly on bookList.clecked!
        #Why? Perhaps signals? Or more than one listview?
        self.list_of_books('Select book_no, name, author from books')
        self.refreshCustomersButton.clicked.connect(lambda: self.list_customers('Select * from customers'))
        self.refreshcheckoutsButton.clicked.connect(lambda: self.list_checkouts('Select * from checkout'))
        
        #Home picture
        self.welcomeL = QtWidgets.QLabel(self.Home)
        pixmap = QPixmap('media/(1).jpg')
        self.welcomeL.setPixmap(pixmap)
        #self.resize(pixmap.width(),pixmap.height())
        
    def search_item(self):
        if(not self.searchBookText.text()):
            self.list_of_books('Select book_no, name, author from books')
        else:
            book_name = self.searchBookText.text()
            self.list_of_books("Select book_no, name, author from books where name like '%{}%'".format(book_name))

    def list_of_books(self, query):
        books_list = books.list_books(query)
        #we have to use model to add items to list view(Changing the functionality)
        self.entry = QtGui.QStandardItemModel()
        self.bookList.setModel(self.entry)

        # When receiving the signal, call QtGui.QStandardItemModel.itemFromIndex() 
        # on the given model index to get a pointer to the item
        for book in books_list:
            item = ', '.join(str(info) for info in book)
            it = QtGui.QStandardItem(item)
            self.entry.appendRow(it)
        self.itemOld = QtGui.QStandardItem("text")
        
    def list_checkouts(self, query):
        checks = checkout.list_checkout(query)
        self.entry = QtGui.QStandardItemModel()
        self.checkoutHistoryText.setModel(self.entry)     

        for check in checks:
            item = ', '.join(str(info) for info in check)
            it = QtGui.QStandardItem(item)
            self.entry.appendRow(it)
        self.itemOld = QtGui.QStandardItem("text")
        
    def list_customers(self, query):
        custs = customers.list_customers(query)
        self.entry = QtGui.QStandardItemModel()
        self.customersList.setModel(self.entry)     

        for customer in custs:
            item = ', '.join(str(info) for info in customer)
            it = QtGui.QStandardItem(item)
            self.entry.appendRow(it)
        self.itemOld = QtGui.QStandardItem("text")
        
    def on_click_checkout(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Alert")
        if(self.custemerIdText.text().isdigit() and self.book_num):
            res = customers.checkout_books(int(self.custemerIdText.text()),[self.book_num])
            msg.setText(res)
            self.checkout_clear()
        else:
            msg.setText('Entries are not correct!')
        x = msg.exec_()
            
    def checkout_clear(self):
        self.custemerIdText.clear()
        self.searchBookText.clear()
        
    def on_click_select_book(self, index):
        self.book_num = None
        item = self.entry.itemFromIndex(index)
        if item:
            item.setForeground(QBrush(QColor(255, 0, 0)))
            self.itemOld.setForeground(QBrush(QColor(0, 0, 0)))
            self.itemOld = item
            self.book_num = item.text().split(',')[0]
            
    def register_customer(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Alert")
        if(self.customerNameText.text() and self.customerFamilyText.text()
           and self.customerBirthdayText.text() and (self.customerFemaleRadio.isChecked() or self.customerMaleRadio.isChecked()) ):
            customer_info = []
            customer_info.append(self.customerNameText.text())
            customer_info.append(self.customerFamilyText.text())
            customer_info.append(self.customerBirthdayText.text())
            if self.customerFemaleRadio.isChecked(): customer_info.append('female')
            else : customer_info.append('male')
            res = customers.register(customer_info)
            msg.setText(res)
            self.customer_register_clear()
        else:
            msg.setText('Entries are not correct!')            
        x = msg.exec_()
            
    def on_click_addbook(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Alert")
        if(self.bookNameText.text() and self.bookAuthorText.text() and self.bookDateText.text() and self.bookSummaryText.text()):
            book_info = {}
            book_info['author'], book_info['title'] = self.bookAuthorText.text(), self.bookNameText.text()
            book_info['description'], book_info['year'] = self.bookSummaryText.text(), self.bookDateText.text()
            book_info['available'] = 'Yes' if self.bookAvailableCheck.isChecked() else 'No'
            res = books.add_book(book_info)
            msg.setText(res)
            self.add_book_clear()
        else:
            msg.setText('Entries are not correct!')            
        x = msg.exec_()
            
    def add_book_clear(self):
        self.bookAuthorText.clear()
        self.bookNameText.clear()
        self.bookSummaryText.clear()
        self.bookDateText.clear()
        self.bookAvailableCheck.setChecked(False)
        
    def customer_register_clear(self):
        self.customerNameText.clear()
        self.customerFamilyText.clear()
        self.customerBirthdayText.clear()
        self.customerFemaleRadio.setChecked(False)
        self.customerMaleRadio.setChecked(False)
        
    #Alma end


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Library"))
        self.label_9.setText(_translate("MainWindow", "WELCOME TO THIS LIBRARY"))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.Home), _translate("MainWindow", "Home"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Author"))
        self.label_5.setText(_translate("MainWindow", "Date of publication"))
        self.label_6.setText(_translate("MainWindow", "summary"))
        self.bookAvailableCheck.setText(_translate("MainWindow", "Yes"))
        self.label_13.setText(_translate("MainWindow", "Is available"))
        self.addBookClearButton.setText(_translate("MainWindow", "clear"))
        self.addBooktButton.setText(_translate("MainWindow", "Ok"))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.addBooksTab), _translate("MainWindow", "Add book"))
        self.label.setText(_translate("MainWindow", "Search by name"))
        self.label_2.setText(_translate("MainWindow", "Please Select Books"))
        self.label_12.setText(_translate("MainWindow", "Enter customer id"))
        self.checkoutClearButton.setText(_translate("MainWindow", "clear"))
        self.checkoutButton.setText(_translate("MainWindow", "Ok"))
        self.refreshBooksButton.setText(_translate("MainWindow", "Refresh"))
        self.label_10.setText(_translate("MainWindow", "There is a default student with id = 1"))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.CheckoutBooksTab), _translate("MainWindow", "Checkout Books"))
        self.label_7.setText(_translate("MainWindow", "Family"))
        self.label_8.setText(_translate("MainWindow", "Name"))
        self.label_14.setText(_translate("MainWindow", "Birthday"))
        self.label_15.setText(_translate("MainWindow", "Gender"))
        self.customerFemaleRadio.setText(_translate("MainWindow", "Female"))
        self.customerMaleRadio.setText(_translate("MainWindow", "Male"))
        self.registerClearButton.setText(_translate("MainWindow", "clear"))
        self.registerButton.setText(_translate("MainWindow", "Ok"))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.registerCustomerTab), _translate("MainWindow", "Register customer"))
        self.label_31.setText(_translate("MainWindow", "Customers List"))
        self.refreshCustomersButton.setText(_translate("MainWindow", "Refresh"))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.customersListTab), _translate("MainWindow", "Customers List"))
        self.label_11.setText(_translate("MainWindow", "Checkout History"))
        self.refreshcheckoutsButton.setText(_translate("MainWindow", "Refresh"))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.checkoutHistoryTab), _translate("MainWindow", "Checkout History"))
        self.actionyg.setText(_translate("MainWindow", "Register new book"))
        self.actionList_books.setText(_translate("MainWindow", "List books"))
        self.actionCheckout_Books.setText(_translate("MainWindow", "Checkout Books"))
        self.actionUpdate_Customer_Info.setText(_translate("MainWindow", "Update Customer Info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
