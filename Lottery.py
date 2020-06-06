from LotteryGenerator import Generator


class Menu:
    def __init__(self):

        # Choosing which lottery we want to play from available options

        options = {
            '1': 'Lotto',
            '2': 'MiniLotto',
            '3': 'MultiMulti',
            '4': 'ExtraSalary',
            '5': 'Eurojackpot',
            '0': 'Exit / Start over'
        }
        print("Which lottery you want to play? Choose number from below:")
        for key in options:
            print(key, ":", options[key])
        which = input()

        while which not in options:
            print("Wrong choice. Try again.")
            which = input()

        if which == '0':
            return

        # Choosing what we want to do with selected lottery from available options

        options = {
            '1': 'Just show me some examples of this lottery',
            '2': 'I\'m gonna try my luck. LET\'S PLAY !',
            '3': 'Show me website',
            '0': 'Exit / Start over'
        }
        print("\nWhat you want to do?")
        for key in options:
            print(key, ":", options[key])
        what = input()

        while what not in options:
            print("Wrong choice. Try again.")
            what = input()

        if which == '0':
            return

        # Redirection to the appropriate function

        Generator(which, what)

# Looped whole program

while True:
    Menu()
    loop = input("Type 'exit' to end program\nType anything to start over\n")
    if loop == 'exit':
        break
