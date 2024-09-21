print()
import random

house=['speads','club','heart','diamond']
card=['ace',2,3,4,5,6,7,8,9,10,'j','q','k']
deck=[]
for h in house:
    for c in card:
        deck.append((h,c))

random.shuffle(deck)
print(deck)
game=[]
for i in range(1,5):
    l=[]
    user=input('enter name:')
    for g in deck[i::4]:
        l.append(g)
    l.insert(0,user)
    game.append(l)
for t in game:
  print(t)
  print(len(t))