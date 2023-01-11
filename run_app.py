from PyQt5 import QtWidgets
from run import Ui_Dialog
import sys
from abi import OptShop

class UiWork(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.Api = OptShop()
        self._id = 0X0
        self.ui.tabWidget.setEnabled(0)
        self.ui.btnAddUser.clicked.connect(self.register)
        self.ui.btnEnter.clicked.connect(self.login)
        self.ui.btnAddProv.clicked.connect(self.add_prov)
        self.ui.btnAddGood.clicked.connect(self.add_goods)
        self.ui.btnFindGood.clicked.connect(self.add_good_list)
        self.ui.btnBuyGood.clicked.connect(self.buy_good)
        self.ui.btnChange.clicked.connect(self.change_goods)

    def register(self):
        self._id = self.ui.lineReg4.text()
        name = self.ui.lineReg1.text()
        addr = self.ui.lineReg2.text()
        phone = self.ui.lineReg3.text()
        self.Api.add_Buyer(name, addr, phone,self._id)

    def login(self):
        self._id = self.ui.lineEnterAdr.text()
        self.ui.textBrowser.setText(str(self.Api.get_balance(self._id)))
        if self._id == self.Api.admin():
            self.ui.tabWidget.setEnabled(1)
            self.ui.tab_2.setEnabled(1)
        else:
            self.ui.tabWidget.setEnabled(1)
            self.ui.tab_2.setEnabled(0)



    def find_prov_by_id(self):
        id_proov = self.ui.lineIdProv.text()
        if (id_proov != ""):
            id_proov = int(id_proov)
            temp = self.Api.get_proov_by_id(id_proov)
            print(temp)
            self.ui.outInfoProv.setText("id =" + str(temp[0]) + "\nname firm = " + str(temp[1])
                                        + "\naddress firm = " + str(temp[2]) + "\nphone number = " + str(temp[3]))
        else:
            self.ui.outInfoProv.setText(str("не введено значение"))


    def buy_good(self):
        try:
            id_good = self.ui.lineIdGood_2.text()
            amount_good = self.ui.lineAmountGoodBuy.text()
            if(id_good !="" and amount_good !=""):
                id_good = int(id_good)
                amount_good = int(amount_good)
                temp = self.Api.get_good_by_id(id_good)
                cost = int(temp[6])*amount_good
                self.ui.textBrowser.setText(str(self.Api.get_balance(self._id)))
                self.Api.buy_good(id_good,amount_good,self._id,cost)
                self.ui.outInfoTranz.setText("Success\nYour spend " + str(cost) + str(temp[3]))
            else:
                self.ui.outInfoTranz.setText("Failed")
        except Exception as e:
            print(e)



    def add_prov(self):
        id = self.ui.lineIdGood_4.text()
        addrWallet = self.ui.lineAdrWalltetProv.text()
        name = self.ui.lineNameProv_2.text()
        adr = self.ui.lineAdrProv.text()
        phone = self.ui.linePhoneProv.text()
        if(id!="" and addrWallet !="" and name!="" and adr !="" and phone!=""):
            id = int(id)
            self.Api.add_Provider(id,name,adr,phone,addrWallet)
            self.ui.textInfoAll.setText("You added provider!")
        else:
            self.ui.textInfoAll.setText("Not all field fill in provider")


    def add_goods(self):
        try:
            id = self.ui.lineIdGood_3.text()
            nameProv = self.ui.lineNameProv.text()
            nameGood = self.ui.lineNameGood.text()
            valuta = self.ui.lineValuta.text()
            amount = self.ui.lineAmountGood.text()
            costBuy = self.ui.lineCostBuy.text()
            costSell = self.ui.lineCostSell.text()
            if(id !="" and nameProv!="" and nameGood!="" and valuta!="" and amount!="" and costBuy!="" and costSell!=""):
                id = int(id)
                amount = int(amount)
                costBuy = int(costBuy)
                costSell = int(costSell)
                self.Api.add_Good(id,nameProv,nameGood,valuta, amount, costBuy, costSell,True)
                self.ui.textInfoAll.setText("You added the good!")
            else:
                self.ui.textInfoAll.setText("Not all field fill in goods")
        except Exception as e:
            print(e)

    def change_goods(self):
        try:
            id = self.ui.lineIdGood2.text()
            nameGood = self.ui.lineNameGood2.text()
            valuta = self.ui.lineValutaGood2.text()
            amount = self.ui.lineAmountGood2.text()
            costBuy = self.ui.lineCostBuy2.text()
            costSell = self.ui.lineCostSell2.text()
            if (id != "" and nameGood != "" and valuta != "" and amount != "" and costBuy != "" and costSell != ""):
                id = int(id)
                amount = int(amount)
                costBuy = int(costBuy)
                costSell = int(costSell)
                self.Api.change_Good(id,nameGood,valuta,amount,costBuy,costSell,True)
                self.ui.textInfoAll.setText("You changed filed!")

            else:
                self.ui.textInfoAll.setText("Not all field fill in goods change")
        except Exception as e:
            print(e)

    def add_good_list(self):
        try:
            self.ui.tableWidget.clear()
            arr_size = self.Api.get_goods_num()
            self.ui.tableWidget.setRowCount(arr_size)
            self.ui.tableWidget.setColumnCount(6)
            self.ui.tableWidget.setHorizontalHeaderLabels(["Номер","id товара","Поставщик","Валюта","Количество","Цена"])
            for i in range(arr_size):
                arr = self.Api.get_good_by_id(i)
                for j in range(6):
                    self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(arr[j])))
        except Exception as e:
            print(e)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = UiWork()
    myapp.show()
    sys.exit(app.exec_())