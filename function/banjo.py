#Mrs banjo account balance in GTB is 100000, the bank decided to be
#removing 2000 from her account every day this action should 
#continue while her balance is > 5000.
#Write a python function code that will show the trans

def banjo():
    balance=100000
    while balance > 5000:
        balance=balance-2000
        print(balance)
banjo()        