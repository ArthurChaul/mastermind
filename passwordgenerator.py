import random

print()
print("                        M A S T E R    M I N D                          ")
print("                            ---------------                             ")
print()
print("The rules to this Master Mind game is simple. You have to guess the 4 COLORS that I am thinking correctly.")
print()
print("                             R U L E S !          ")
print("                               ------             ")
print()
print(" 1. YOU only need to guess 4 colors. ")
print()
print(" 2. Please key in the correct keyword for each color.")
print()
print(" 3. List of colors: Red , Blue , Green , Yellow, Purple, Black.")
print()
print()

colors = ['Blue', 'Yellow', 'Green', 'Red', 'Purple', 'Black']

ans1 = random.choice(colors)
ans2 = random.choice(colors)
ans3 = random.choice(colors)
ans4 = random.choice(colors)
pass_guess1 = None
pass_guess2 = None
pass_guess3 = None
pass_guess4 = None


def pass_checker():
    global pass_guess1
    global pass_guess2
    global pass_guess3
    global pass_guess4
    pass_guess1 = input('First hole: ').capitalize()
    pass_guess2 = input('Second hole: ').capitalize()
    pass_guess3 = input('Third hole: ').capitalize()
    pass_guess4 = input('Fourth hole: ').capitalize()

    while True:
        if pass_guess1 == ans1:
            print(f'\n{pass_guess1} is in the correct place!')
            break
        elif pass_guess1 == ans2 or pass_guess1 == ans3 or pass_guess1 == ans4:
            print(f'\n{pass_guess1} is in the sequence but is not in the correct place.')
            break
        elif pass_guess1 != ans2 or pass_guess1 != ans3 or pass_guess1 != ans4:
            print(f'\n{pass_guess1} is not in the sequence.')
            break
        break
    while True:
        if pass_guess2 == ans2:
            print(f'\n{pass_guess2} is in the correct place!')
            break
        elif pass_guess2 == ans1 or pass_guess2 == ans3 or pass_guess2 == ans4:
            print(f'\n{pass_guess2} is in the sequence but is not in the correct place.')
            break
        elif pass_guess2 != ans1 or pass_guess2 != ans3 or pass_guess2 != ans4:
            print(f'\n{pass_guess2} is not in the sequence.')
            break
        break
    while True:
        if pass_guess3 == ans3:
            print(f'\n{pass_guess3} is in the correct place!')
            break
        elif pass_guess3 == ans2 or pass_guess3 == ans1 or pass_guess3 == ans4:
            print(f'\n{pass_guess3} is in the sequence but is not in the correct place.')
            break
        elif pass_guess3 != ans2 or pass_guess3 != ans1 or pass_guess3 != ans4:
            print(f'\n{pass_guess3} is not in the sequence.')
            break
        break
    while True:
        if pass_guess4 == ans4:
            print(f'\n{pass_guess4} is in the correct place!\n')
            break
        elif pass_guess4 == ans2 or pass_guess4 == ans3 or pass_guess4 == ans1:
            print(f'\n{pass_guess4} is in the sequence but is not in the correct place.\n')
            break
        elif pass_guess4 != ans2 or pass_guess4 != ans3 or pass_guess4 != ans1:
            print(f'\n{pass_guess4} is not in the sequence.\n')
            break
        break


attempts = 1

while pass_guess1 != ans1 or pass_guess2 != ans2 or pass_guess3 != ans3 or pass_guess4 != ans4:
    print(f'Attempt #{attempts}!\n')
    pass_checker()
    attempts += 1

print(f'Congratulations, it took you {attempts} attempts to get the correct sequence!\n')
print("                            ---------------                             ")
print('             T H A N K    Y O U    F O R    P L A Y I N G               \n')
print("                        M A S T E R    M I N D                          ")
print("                            ---------------                             ")
print('                       B Y    A R T H U R    S A')
print("                            ---------------                             ")
