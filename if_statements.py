#working with if and elif statements

#1

sapa_user = float(input("how much is in your account: "))
if sapa_user < 1000:
    print (float(sapa_user + 1000))
else:
    print ("you are rich")

#2

drinker = int(input("enter your drinking age: "))
if drinker < 18:
    print ("you can't drink alcohol")
if drinker > 18:
    print ("cheers drunkard")

#3

list_lenght = int(input("enter list lenght: "))
if list_lenght < 6:
    print ("is less than 6")
if list_lenght == 6:
    print ("is equal to 6")
if list_lenght > 6:
    print ("now we talking")


