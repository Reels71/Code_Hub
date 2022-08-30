# Write a calculator app that can only be ended when a user types end in the command line.
# Now this calculator should be able to take in as much values that the user decided to perform calculations on.
import math
print ('OPERATORs: + = addition, - = subtraction, * = multiplication, / = division, ** = exponent,\n // = floored quotient/interger division, % = modulus/remainder, math.sqrt = square root')

Num1 = float(input())
Operator = input()
Num2 = float(input())


def calculator():
  for x in range (0,1):
    if Operator == 'END':
        break

    if Operator == '+':
        print (Num1 + Num2)
    
    elif Operator == '-':
        print (Num1 - Num2)

    elif Operator == '*':
        print (Num1 * Num2)
    
    elif Operator == '/':
        print (Num1 / Num2)
    
    elif Operator == '**':
        print (Num1 ** Num2)

    elif Operator == '//':
        print (Num1 // Num2)

    elif Operator == '%':
        print (Num1 % Num2)

    elif Operator == 'math.sqrt':
        print (math.sqrt(Num1))

    else:
        print ('invalid..... try again')

calculator()
    