 #Lerning to work with functions.

#1

from calendar import c


def fahrenheit():
    celcius_value = float(input('celcius value: '))
    answer_in_fahrenheit = ((celcius_value - 32) / 1.8)
    print (f'fahrenheit value = ', answer_in_fahrenheit)

fahrenheit()


#2

def fight():
    user = input().lower()
    if user == 'war':
         for fight in range (0 , 4):
            print('russia vs nigeria')

fight()


#3

market_items = []

def mkt():
    while True:
        for user in range (0, 7):
            user = input('market_items = ').lower()
            if user == 'stop':
             break
            market_items.append(user)
        print(market_items)
        break
              
mkt()






