import time

def translator (phrase):
  translation = ''
  for letter in phrase:
     if letter in 'AOPaop':
      translation = translation + 'g'
     else :
       translation = translation + letter
       
  return translation   
       
time.sleep(1)
print (translator(input('Enter your word :')))