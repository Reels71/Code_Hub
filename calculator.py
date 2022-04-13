#Building a calculator

import math

Operator = input()

if Operator == '+':   #addition
    num = (float(input()) + float(input()))
    print (num)

elif Operator == '-':   #subtraction
    num = (float(input()) - float(input()))
    print (num)

elif Operator == '*':   #multiplication
    num = (float(input()) * float(input()))
    print (num)

elif Operator == '/':    #division
    num = (float(input()) / float(input()))
    print (num)

elif Operator == '**':   #exponent
    num = (float(input()) ** float(input()))
    print (num)

elif Operator == '//':   #floored quotient/interger division
    num = (float(input()) // float(input()))
    print (num)

elif Operator == '%':    #modulus/remainder
    num = (float(input()) % float(input()))
    print (num)

elif Operator == 'math.sqrt':   #square root
    num = (float(input()))
    print (math.sqrt(num))

else:
    print ("invalid")
