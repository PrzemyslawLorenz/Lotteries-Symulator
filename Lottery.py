from LotteryGenerator import Generator
from LotteryDataBase import DataBase

class Menu:
    def __init__(self):

        # Choosing what we want to do from available options

        options = {
            '1': 'Just show me some examples of lottery',
            '2': 'I\'m gonna try my luck. LET\'S PLAY !',
            '3': 'Go to data base',
            '4': 'Show me website',
            '0': 'Exit / Start over'
        }
        print("\nWhat you want to do?")
        for key in options:
            print(key, ":", options[key])
        what = input()

        while what not in options:
            print("Wrong choice. Try again.")
            what = input()

        if what == '0':
            return

        # Choosing which lottery we want to use

        options = {
            '1': 'Lotto',
            '2': 'MiniLotto',
            '3': 'MultiMulti',
            '4': 'ExtraSalary',
            '5': 'Eurojackpot',
            '6': 'Fast600',
            '7': 'Keno',
            '0': 'Exit / Start over'
        }
        print("Which lottery you want? Choose number from below:")
        for key in options:
            print(key, ":", options[key])
        which = input()

        while which not in options:
            print("Wrong choice. Try again.")
            which = input()

        # Redirection to the appropriate function or class

        if which == '0':
            return
        elif what == '3':
            DataBase(which, options)
        else:
            Generator(which, what, options)

# Looped whole program

while True:
    Menu()
    loop = input("\nType 'exit' to end program\nType anything to start over\n")
    if loop == 'exit':
        break