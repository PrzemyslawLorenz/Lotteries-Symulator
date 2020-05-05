from LotteryGenerator import Generator


class Menu:
    def __init__(self):
        options = {
            '1': 'Lotto',
            '2': 'MiniLotto',
            '3': 'MultiMulti',
            '4': 'ExtraSalary',
            '5': 'Eurojackpot',
            '0': 'Exit'
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

        options = {
            '1': 'Just show me some examples of this lottery',
            '2': 'I\'m gonna try my luck. LET\'S PLAY !',
            '3': 'Show me website'
        }
        print("\nWhat you want to do?")
        for key in options:
            print(key, ":", options[key])
        what = input()

        while what not in options:
            print("Wrong choice. Try again.")
            what = input()

        Generator(which, what)


Menu()
print("\nThank you for using this program")
exit = input("Press ENTER to exit")