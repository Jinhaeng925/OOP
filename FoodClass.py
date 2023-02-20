class Customer:
    def __init__(self, customerid, name, address, email, phone, member_status):
        self.__customerid = customerid
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        if (member_status == 'True'):
            self.__member_status = True
        else:
            self.__member_status = False

    # Accessor method to get Customer ID
    def get_customerID(self):
        return self.__customerid

    # Accessor method to get Customer Name
    def get_customerName(self):
        return self.__name

    # Accessor method to get Customer Address
    def get_customerAddress(self):
        return self.__address

    # Accessor method to get Customer Email
    def get_customerEmail(self):
        return self.__email

    # Accessor method to get Customer Phone Number
    def get_customerPhone(self):
        return self.__phone

    # Accessor method to get Customer Membership Status
    def get_customerMemberStatus(self):
        return self.__member_status


class Transaction:
    def __init__(self, date, itemName, cost, customerid):
        self.__txDate = date
        self.__txItemName = itemName
        self.__txCost = cost
        self.__txCustomerID = customerid

    # Accessor method to get Transaction Date
    def get_txDate(self):
        return self.__txDate

    # Accessor method to get Transaction Item Name
    def get_txItemName(self):
        return self.__txItemName

    # Accessor method to get Transaction Cost
    def get_txCost(self):
        return self.__txCost

    # Accessor method to get Transaction Customer ID
    def get_txCustomerID(self):
        return self.__txCustomerID
