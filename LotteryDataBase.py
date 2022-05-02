from shutil import which
import sys, os

class DataBase:
    def __init__(self, which, options):
        while True:
            self.which = which
            self.options = options
            self.lotteries = {
                '1': [49, 6],  # Lotto
                '2': [42, 5],  # MiniLotto
                '3': [80, 20],  # MultiMulti
                '4': [35, 5, 4, 1],  # ExtraSalary
                '5': [50, 5, 10, 2],  # Eurojackpot
                '6': [32, 6], # Fast 600
                '7': [70, 20] # Keno
            }
            whatop = {
                '1': 'Show me common and uncommon numbers',
                '2': 'Delete some draws from data base'
            }

            print("What you want to do with data base?")
            for key in whatop:
                print(key, ":", whatop[key])
            what = input()

            while what not in whatop:
                print("Wrong choice. Try again.")
                what = input()

            if what == '1':
                self.commonAndUncommon()
            elif what == '2':
                self.deleting()

            loop = input("\nType 'exit' to quit data base\nType anything to start over\n")
            if loop == 'exit':
                break

    def commonAndUncommon(self):

        howManyDraws = 0
        tab = []
        for _ in range(self.lotteries[self.which][0]):
            tab.append(0)

        file = open(os.path.join(sys.path[0], self.options[self.which] + "_draws.txt"), "r")

        for line in open(os.path.join(sys.path[0], self.options[self.which] + "_draws.txt"), "r"):
            howManyDraws += 1
            line = line.replace('[', '').replace(']', '').replace(',', '')
            line = [int(i) for i in line.split(' ')]

            for value in line:
                tab[value-1] += 1
                
        file.close

        temp=tab

        print("How many common and uncommon numbers you want to see?")
        howManyNumbers = self.inputing()

        print("The most common numbers in", howManyDraws, "draws are: ")
        for _ in range(howManyNumbers):
            print(tab.index(max(tab)) + _ + 1, "which appeared", max(tab), "times")
            tab.pop(tab.index(max(tab)))

        tab = temp

        print("\nThe most uncommon numbers in", howManyDraws, "draws are: ")
        for _ in range(howManyNumbers):
            print(tab.index(min(tab)) + _ + 1, "which appeared", min(tab), "times")
            tab.pop(tab.index(min(tab)))

    def deleting (self):

        print("How many draws you want to delete?")
        drawsToDelete = self.inputing()

        file = open(os.path.join(sys.path[0], self.options[self.which] + "_draws.txt"), "r+")
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        file.writelines(lines[drawsToDelete:])
        file.close

        print("Draws successfull deleted")

    def inputing (self):

        while True:
            try:
                Input = int(input())
                break
            except ValueError:
                print("Wrong value. Try again. ")
                pass

        return Input