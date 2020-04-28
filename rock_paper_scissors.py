import random
import time


choice = ['rock' , 'paper' , 'scissors' ]

player = ''
game = False
rounds = 0
max_rounds = 3
player_score = 0
comp_score = 0

print('Welcome to rock,paper and scissors game!')
time.sleep(1)
while not(game) and rounds < max_rounds :
    comp = random.choice(choice)
    player = input('Type rock, paper or scissors:')
    if player == comp :
      print('This is the computers choice: ' + str(comp))
      print ('Thats a draw')
      rounds+=1
    elif player == 'rock' and comp == 'paper':
      print('This is the computers choice: ' + str(comp))
      print('You lost this round !')
      rounds+=1
      comp_score +=1
    elif player == 'rock' and comp == 'scissors':
      print('This is the computers choice: ' + str(comp))
      print('You won this round !')
      rounds+=1
      player_score +=1
    elif player == 'paper' and comp == 'rock':
      print('This is the computers choice: ' + str(comp))
      print('You won this round')
      player_score +=1
      rounds+=1
    elif player == 'paper' and comp == 'scissors':
      print('This is the computers choice: ' + str(comp))
      print('You lost this round!')
      comp_score +=1
      rounds+=1
    elif player == 'scissors' and comp == 'rock':
      print('This is the computers choice: ' + str(comp))
      print('You lost this round!')
      comp_score +=1
      rounds+=1
    elif player == 'scissors' and comp == 'paper':
      print('This is the computers choice: ' + str(comp))
      print('You won this round!')
      player_score +=1
      rounds+=1
time.sleep(1)
print('This was the last round ')
time.sleep(1)
if player_score > comp_score:
    print('You are the winner!')
elif comp_score> player_score:
    print('The computer is the winner!')
else:
    print('The game is a draw')