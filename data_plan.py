#Building a mini data plan


from ast import Return
from re import I
from tkinter.messagebox import RETRY



Subscriber = input('which data bundle can you afford; monthly(1) or weekly(2) or daily(3)??  ')


monthly_data_plan = {'M1':'N1000/1.5GB', 'M2':'N1200/2GB', 'M3':'N1500/3GB', 'M4':'N2000/4.5GB', 'M5':'N2500/6GB'}
                        
weekly_data_plan =  {'W1':'N500/750MB/14days', 'W2':'N500/1GB/7days', 'W3':'N1500/6GB/7days', 'W4':'N300/350MB/7days', 'W5':'N100/7All Social/5days'}
                       
daily_data_plan = {'D1':'N50/40MB/Daily', 'D2':'N100/100MB/Daily', 'D3':'N200/200MB/3days', 'D4':'N300/1GB/Daily', 'D5':'N500/2GB/Daily'}

def data():
    for x in range (1):
        if Subscriber == ('1'):
            print (monthly_data_plan)
            print ('select your preferred bundle; M1 - M5 ')
        
        elif Subscriber == ('2'):
            Subscriber == weekly_data_plan
            print (weekly_data_plan)
            print ('select your preferred bundle; W1 - W5 ')
        
        elif Subscriber == ('3'):
            Subscriber == daily_data_plan
            print (daily_data_plan)
            print ('select your preferred bundle; D1 - D5 ')
            
        else:
            print('invalid')
            
            break


data()

x = input('').capitalize()
def bundle():
    i = 1
    try:
        while i <= 5:
            if x == ('M' + str(i)):
                print(f'from monthly data plans, you have selected ' + monthly_data_plan.get(str(x)))
                print('Enter 1 to bundle or 2 to cancel or enter 3 to return to main menu ')
                user = int(input())
                if user == 1:
                    print('you have bundled successfully!!!')
                elif user == 3:
                 print('retry')
                else:
                 break

            elif x == ('W' + str(i)):
                print(f'from weekly data plans, you have selected ' + weekly_data_plan.get(str(x)))
                print('Enter 1 to bundle or 2 to cancel or enter 3 to return to main menu ')
                user = int(input())
                if user == 1:
                    print('you have bundled successfully!!!')
                elif user == 3:
                 print('retry')
                else:
                 break

            elif x == ('D' + str(i)):
                print(f'from daily data plans, you have selected ' + daily_data_plan.get(str(x)))
                print('Enter 1 to bundle or 2 to cancel or enter 3 to return to main menu ')
                user = int(input())
                if user == 1:
                    print('you have bundled successfully!!!')
                elif user == 3:
                 print('retry')
                else:
                 break
            i = i + 1

    except:

        print('invalid')

bundle()
            