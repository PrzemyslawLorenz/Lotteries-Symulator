import random
import webbrowser
from LotteryWinning import Winning


class Generator:
    def __init__(self, which, what):
        self.which = which
        self.what = what

        # Lottery range and size declaration

        self.lotteries = {
            '1': [49, 6],  # Lotto
            '2': [42, 5],  # MiniLotto
            '3': [80, 20],  # MultiMulti
            '4': [35, 5, 4, 1],  # ExtraSalary
            '5': [50, 5, 10, 2],  # Eurojackpot
            '6': [32, 6] # Fast 600
        }

        # Redirection to the appropriate function

        if self.what == "1":
            howMany = int(input("\nHow many examples do you want?\n"))
            while(howMany):
                print(self.generating())
                howMany -= 1
        elif self.what == "2":
            if self.which == "3":
                self.lotteries[self.which][1] = 10
            self.playing()
        elif self.what == "3":
            self.website()

    def generating(self):

        # Generating random numbers for the selected lottery

        if len(self.lotteries[self.which]) > 2:
            self.generatedNumbers1 = random.sample(
                range(1, self.lotteries[self.which][0] + 1),
                self.lotteries[self.which][1])
            self.generatedNumbers2 = random.sample(
                range(1, self.lotteries[self.which][2] + 1),
                self.lotteries[self.which][3])

            return sorted(self.generatedNumbers1), sorted(self.generatedNumbers2)

        else:
            self.generatedNumbers1 = random.sample(
                range(1, self.lotteries[self.which][0] + 1),
                self.lotteries[self.which][1])

            return sorted(self.generatedNumbers1)

    def playing(self):

        # Getting numbers from the user

        myNumbers = []
        myNumbers2 = []
        print("\nOkay. Give me your", self.lotteries[self.which][1],
              "numbers from 1 to", self.lotteries[self.which][0],
              "\nPlease give them one at a time")
        for _ in range(self.lotteries[self.which][1]):
            myNumbers.append(int(input()))
            while myNumbers[_] not in range(1, self.lotteries[self.which][0] + 1) or myNumbers.count(myNumbers[_]) > 1:
                print("You give me wrong number. Try again: ")
                myNumbers.pop()
                myNumbers.append(int(input()))

        if len(self.lotteries[self.which]) > 2:
            print("\nNow give me", self.lotteries[self.which][3],
                  "number/s from 1 to", self.lotteries[self.which][2])
            for _ in range(self.lotteries[self.which][3]):
                myNumbers2.append(int(input()))
                while myNumbers2[_] not in range(1, self.lotteries[self.which][2] + 1) or myNumbers2.count(myNumbers2[_]) > 1:
                    print("You give me wrong number. Try again: ")
                    myNumbers2.pop()
                    myNumbers2.append(int(input()))

        if self.which == "3":
            self.lotteries[self.which][1] = 20

        self.generating()

        # Comparing and counting hited numbers

        hitsOnFirst = 0
        hitsOnSecond = 0
        for _ in range(self.lotteries[self.which][1]):
            if self.generatedNumbers1[_] in myNumbers:
                hitsOnFirst += 1
        if len(self.lotteries[self.which]) > 2:
            for _ in range(self.lotteries[self.which][3]):
                if self.generatedNumbers2[_] in myNumbers2:
                    hitsOnSecond += 1
                    
        if len(self.lotteries[self.which]) > 2:
            Winning(self.which, self.generatedNumbers1, self.generatedNumbers2, myNumbers, myNumbers2, hitsOnFirst, hitsOnSecond)
        else:
            Winning(self.which, self.generatedNumbers1, None, myNumbers, None, hitsOnFirst, hitsOnSecond)

    def website(self):

        # Lottery websites declaration and redirection to them

        websites = {
            '1': 'lotto',  # Lotto
            '2': 'mini-lotto',  # MiniLotto
            '3': 'multi-multi',  # MultiMulti
            '4': 'ekstra-pensja',  # ExtraSalary
            '5': 'eurojackpot',  # Eurojackpot
            '6': 'szybkie-600' # Fast 600
        }

        webbrowser.open_new_tab("https://www.lotto.pl/" + websites[self.which])