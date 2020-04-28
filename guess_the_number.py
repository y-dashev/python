import random
import time

number = random.randrange(1,11)
guesses = 0
limit = 3
time.sleep(1)
print('Welcome to guess the number game!')
time.sleep(1)
print('Choose a number between 1 and 10')
time.sleep(1)
while guesses < limit:
   guessinput = int(input('Enter your number: '))
   if guessinput == number:
      print('Thats the right number!')
      break
   elif guessinput > number:
      print('Your number is higher')
      guesses +=1
   elif guessinput< number:
      print ('Your number is lower')
      guesses +=1


time.sleep(1)
if guesses == limit:
   print('Sorry you lost')
else:
   print('You won!')