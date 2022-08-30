#generate a random number
#we ask the person what number is on our mind (between 1 - 10)
#we compare what they enter to what we have generated
#if it is correct, say "you win"
#if it is not correct, say "try again"

from random import randint


guess = randint (1, 10)


def game():
 

 for guessT in range (0, 3):
     print('guess')
     Player = int(input('what number is on my mind: '))
     
     if Player > guess:
               print("it's greater than the expected number")
     elif Player < guess:
          print("it's less than the expected number")
     else:
          break
         
     if Player == guess:
           print ('you win')
     else: 
         print('try again')
         
          

game()


            
     
            
           
          
           




