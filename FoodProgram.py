import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1': ['2/15/2023', 'The Lone Patty', 17, 569],
        'trans2': ['2/15/2023', 'The Octobreakfast', 18, 569],
        'trans3': ['2/15/2023', 'The Octoveg', 16, 570],
        'trans4': ['2/15/2023', 'The Octoburger', 20, 570],
        }

order_total = 0
member_discount = 0

# customer = fc.Customer(570, "Danni Sellyar", "97 Mitchell Way Hewitt Texas 76712",
#                       "dsellyarft@gmpg.org", "254-555-9362", "False")
customer = fc.Customer(569, "Aubree Himsworth", "1172 Moulton Hill Waco Texas 76710",
                       "ahimsworthfs@list-manage.com", "254-555-2273", "True")

print('Customer Name: ' + customer.get_customerName())
print('Phone: ' + customer.get_customerPhone())

for tx in dict:
    customer_tx = fc.Transaction(
        dict[tx][0], dict[tx][1], dict[tx][2], dict[tx][3])
    if (customer_tx.get_txCustomerID() == customer.get_customerID()):
        order_total += customer_tx.get_txCost()
        print('Order Item: ' + customer_tx.get_txItemName() + '  '
              'Price: $' + format(customer_tx.get_txCost(), ',.2f'))
        if (customer.get_customerMemberStatus() == True):
            member_discount += (0.2 * customer_tx.get_txCost())


print('Total Cost: $' + format(order_total, ',.2f'))

if (customer.get_customerMemberStatus() == True):
    print('Member Discount: $' + format(member_discount, ',.2f'))
    print('Total Cost after discount: $' +
          format((order_total-member_discount), ',.2f'))
