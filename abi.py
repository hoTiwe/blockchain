import web3
import json

class OptShop():
    ganache_url = "HTTP://127.0.0.1:7545"
    w3 = web3.Web3(web3.HTTPProvider(ganache_url))

    addres_contract = '0x1b8ddE243fF12c6eb2B55592DBC7b75beD2dC799'

    with open("abi.json", "r") as file:
        abi = json.load(file)

    contract = w3.eth.contract (address = addres_contract, abi = abi)

    def init(self):
        pass

    def accounts(self):
        return self.w3.eth.accounts

    def get_balance(self, address):
        _address = web3.Web3.toChecksumAddress(address)
        return web3.Web3.fromWei(self.w3.eth.getBalance(_address), 'ether')

    def get_deal_num(self):
        return self.contract.functions.get_deal_num().call()

    def admin(self):
        return self.contract.functions.admin().call()

    def get_goods_num(self):
        return self.contract.functions.get_goods_num().call()

    def add_Good(self,idGood, nameFirm, nameGoods, units, amount, valueBuy, valueSell, isSalling):
        tx =self.contract.functions.add_good(idGood, nameFirm, nameGoods, units, amount, valueBuy, valueSell,isSalling).transact({'from': OptShop.admin(self)})
        self.w3.eth.waitForTransactionReceipt(tx)


    def add_Provider(self,id,nameFirm, addressFirm, phoneNumber,address_owner):
        tx = self.contract.functions.add_provider(id,nameFirm,addressFirm,phoneNumber,address_owner).transact({'from':OptShop.admin(self)})
        self.w3.eth.waitForTransactionReceipt(tx)


    def add_Buyer(self, nameFirmBuy, addressFirmBuy, phoneNumberBuy,owner_buyer):
        tx =self.contract.functions.add_buyer(nameFirmBuy, addressFirmBuy, phoneNumberBuy,owner_buyer).transact({'from': owner_buyer})
        self.w3.eth.waitForTransactionReceipt(tx)

    def change_Good(self,idGood, nameGoods, units, amount, valueBuy, valueSell, isSalling):
        tx =self.contract.functions.change_good(idGood, nameGoods, units, amount, valueBuy, valueSell,isSalling).transact({'from': OptShop.admin(self)})
        self.w3.eth.waitForTransactionReceipt(tx)

    def add_deals(self, id, idBuyer, amountSellGoods) :
        tx =self.contract.functions.add_deals(id, idBuyer,amountSellGoods ).transact({'from': OptShop.admin(self)})
        self.w3.eth.waitForTransactionReceipt(tx)

    def buy_good(self,id, removeGood, idBuyer, price):
        tx = self.contract.functions.buy_good(id, removeGood, idBuyer).transact(
            {'from': OptShop.admin(self), 'value': price})
        self.w3.eth.waitForTransactionReceipt(tx)

    def get_good_by_id(self, id):
        return self.contract.functions.get_goods(id).call()

    def get_proov_by_id(self, id):
        return self.contract.functions.get_provider(id).call()


OS = OptShop()
#print(OS.admin())
#acc = OS.accounts()
#balance = OS.get_balance(acc[0])
#print(acc)


#OS.add_Good(10,"123","123","ru",123,5,7, True)
#print(OS.get_proov_by_id(0))
#print(OS.get_goods_num())

#print(acc[0])
#print(balance)