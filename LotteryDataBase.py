from shutil import which
import sys, os

class DataBase:
    def __init__(self, which, options):
        while True:     # Looping
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

            # Choosing what we want to do with our data base

            whatop = {
                '1': 'Show me common and uncommon numbers',
                '2': 'Delete some draws from data base',
                '3': 'Add some draws to data base',
                '0': 'Exit / Start over'
            }

            print("What you want to do with data base?")
            for key in whatop:
                print(key, ":", whatop[key])
            what = input()

            while what not in whatop:
                print("Wrong choice. Try again.")
                what = input()

            # Redirection to the appropriate function

            if what == '1':
                self.commonAndUncommon()
            elif what == '2':
                self.deleting()
            elif what == '3':
                if self.which == "3" or self.which == "7":
                    self.lotteries[self.which][1] = 10
                self.adding()
            elif what == '0':
                return

            loop = input("\nType 'exit' to quit data base\nType anything to start over\n")
            if loop == 'exit':
                break

    def commonAndUncommon(self):

        # Reeding our txt file
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

        # Counting most common and uncommon numbers

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

        drawsToDelete = []
        print("How many draws you want to delete?")
        howManyToDelete = self.inputing()
        print("Which draws you want to delete?\nPlease give them one at a time")
        for _ in range(howManyToDelete):
            drawsToDelete.append(self.inputing())

        # Reeding and saving our txt file without lines we choose

        file = open(os.path.join(sys.path[0], self.options[self.which] + "_draws.txt"), "r+")
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        for number, line in enumerate(lines):
            if number + 1 not in drawsToDelete:
                file.write(line)
        file.close

        print("Draws successfull deleted")

    def adding (self):

        print("How many draws you want to add?")
        howManyDrawsToAdd = self.inputing()

        while howManyDrawsToAdd != 0:   # Looping

            # Getting numbers from the user which we wont to add to txt file

            myNumbers = []
            myNumbers2 = []
            print("\nOkay. Give me your", self.lotteries[self.which][1],
                "numbers from 1 to", self.lotteries[self.which][0],
                "\nPlease give them one at a time")
            for _ in range(self.lotteries[self.which][1]):
                myNumbers.append(self.inputing())
                while myNumbers[_] not in range(1, self.lotteries[self.which][0] + 1) or myNumbers.count(myNumbers[_]) > 1:
                    print("You give me wrong number. Try again: ")
                    myNumbers.pop()
                    myNumbers.append(self.inputing())

            if len(self.lotteries[self.which]) > 2:
                print("\nNow give me", self.lotteries[self.which][3],
                    "number/s from 1 to", self.lotteries[self.which][2])
                for _ in range(self.lotteries[self.which][3]):
                    myNumbers2.append(self.inputing())
                    while myNumbers2[_] not in range(1, self.lotteries[self.which][2] + 1) or myNumbers2.count(myNumbers2[_]) > 1:
                        print("You give me wrong number. Try again: ")
                        myNumbers2.pop()
                        myNumbers2.append(self.inputing())

            # Adding this numbers to txt file

            if len(self.lotteries[self.which]) > 2:
                file = open(os.path.join(sys.path[0], self.options[self.which] + "_draws.txt"), "a")
                file.write(str(sorted(myNumbers)) + " " + str(sorted(myNumbers2)) + "\n")
                file.close

            else:
                file = open(os.path.join(sys.path[0], self.options[self.which] + "_draws.txt"), "a")
                file.write(str(sorted(myNumbers)) + "\n")
                file.close

            if self.which == "3" or self.which == "7":
                self.lotteries[self.which][1] = 20

            howManyDrawsToAdd -= 1

    def inputing (self):

        while True:
            try:
                Input = int(input())
                break
            except ValueError:
                print("Wrong value. Try again. ")
                pass

        return Input