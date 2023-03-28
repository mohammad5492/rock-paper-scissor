import random

option = ['siserc','rock','paper']
computer=random.choice(option)
player = input('enter rock or scissor or paper ')

while player not in option:
    player = input('enter rock or  scissor or paper :')
print(f'computer chose  is {computer}')

if player == computer:
    print('it is a tie')
elif player == 'rock' and computer == 'scissor':
    print('you win')
elif player == 'paper' and computer == 'rock':
    print('you win')
elif player == 'scissor' and computer == 'paper':
    print('you win')
else:
    print('you lose')