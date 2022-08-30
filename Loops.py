#Learning loops in python

a = 'ifiok'
i = 0

while i < len(a):
    print (a[i])
    i = i + 1



Market_items =[]
while True:
    
    user = input('market items: ').lower()
    if user == 'stop':
        break
    Market_items.append(user)
print (Market_items)

a = 'ifiok'

for x in a:
    print (x)


market_items =[]

for items in range(1, 7):
    user = input('market items: ')

    if user == 'stop':
        break
    market_items.append(user)
print(market_items)
    




list_A = ['amaka', 'koffi', 'merci']
list_B = ['nigeria', 'ghana', 'france']

for x in list_A:
    for y in list_B:
        print (x, y)
        