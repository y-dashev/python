import random, time

word = [ 'apple' , 'phone' , 'car' , 'bike' , 'house' ]
randomword = random.choice(word)
print('You must guess the word!!!')
time.sleep(1)
print('This is the first letter of the word: ' + randomword[0])
time.sleep(1)
print ('And the word has ' + str(len(randomword)) + ' letters')
time.sleep(1)
print('You have 5 tries')
time.sleep(1)
guess = ''
tries = 0
triescount = 5
outofguesses = False

while guess != randomword and not(outofguesses) :
 
 if tries < triescount :
   guess = input('Enter your guess :')
   tries +=1
 else:
  outofguesses= True
   
if outofguesses:
 print('Sorry you lost')
else:
  print('You win ')