print("WELCOME TO KBC")
print()
print('''RULE OF GAME
1.you will be asked 5 question from general knowledge.
2. you have to select your answer from the 4 option provided.
3. for every correct answer you will be awarded with 1000 Rs.
4. in case of wrong answer, you will be penalized by 500 RS.''')
print()
print("NOW START YOUR QUIZ")
print()
print("YOUR QUESTION ARE HERE and YOUR TIME START NOW")
print()
reward = 0
corct_qstn = 0
incorct_qstn = 0
#questions
print("QUESTION 1 . WHO IS THE FIRST PRIME MINISTER OF INDIA?")
print('options:')
print('''1. pt.neharu
2. Narendra modi
3. Indira gandhi
4. Draupadi murmu''')
choose_opt = int(input("choose your answer:"))
if choose_opt == 1:
    reward = reward + 1000
    corct_qstn = corct_qstn + 1
    print("you earn reward of '1000Rs'.")
else:
    reward = reward - 500
    incorct_qstn = incorct_qstn  + 1
    print("you have charge penaliti of '500RS'.")
print()
print("QUESTION.2 WHO IS THE HEAD OF 'ISRO'?")
print('optins:')
print('''1. S.somanath
2. Naredra modi
3. A.p.j kalam
4. Ram nath kovind''')
choose_opt = int(input("choose your answer:"))
if choose_opt == 1:
    reward = reward + 1000
    corct_qstn = corct_qstn + 1
    print("you earned '1000RS'.")
else:
    reward = reward - 500
    incorct_qstn = incorct_qstn + 1
    print("you charged penality of '500Rs'.")
print()
print("QUESTION.3 WHAT IS THE ADDION OF  10 AND 20 ?")
print("options:")
print('''1. 10
2. 40
3. 50
4. 30''')
choose_option = int(input('choose your answer:'))
if choose_option == 4:
    reward = reward + 1000
    corct_qstn = corct_qstn + 1
    print("you earned reward of '1000RS'.")
else:
    reward = reward - 500
    incorct_qstn = incorct_qstn + 1
    print("you have charged penaliti of '500RS'.")
print()
print("QUESTION 4. WHAT IS THE SCIENCETIFIC FORMULA OF 'WATER'? ")
print('options:')
print('''1. co3
2. H2o
3. cu
4. al''')
choose_option = int(input('choose your answer:'))
if choose_option == 2:
    reward = reward + 1000
    corct_qstn = corct_qstn + 1
    print("you earned reward of '1000Rs'.")
else:
    reward = reward - 500
    incorct_qstn = incorct_qstn + 1
    print("you have charged penaliti of '500Rs'.")
print()
print("QUESTION.5 WHAT IS THE CAPITAL OF 'UTTAR PRADESH'?")
print('options:')
print('''1. punjab
2. Bhopal
3. Lucknow
4. New delhi''')
choose_option = int(input("enter your answer:"))
if choose_option == 3:
    reward = reward + 1000
    corct_qstn = corct_qstn + 1
    print("you earned reward of '1000'RS.")
else:
    reward = reward - 500
    incorct_qstn = incorct_qstn + 1
    print("you have charged the penality of '500'rs.")

print("your total ammount:",reward)
print(f"you are given {corct_qstn} answer is correct.")
print(f'you are given {incorct_qstn} answer is wrong.')
print("you played well")

