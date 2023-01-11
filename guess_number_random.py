import random
num=random.randint(0,50)
print('Number to be guessed is between 0 to 50 \nwill get 5 chances')
for i in range(1,6):
  n=int(input('Enter your guess:'))
  if n==num:
    print('Correct guess! \nCongratulations')
    break
  elif n>50:
    print('Range is 0-50! \nChoose correctly!')
  else:
    print('Wrong Guess! \nTry Again \nYou have ',5-i,' chances left.')
if n!=num:
  print('Correct Guess was:',num)
