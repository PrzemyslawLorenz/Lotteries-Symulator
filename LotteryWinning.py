class Winning:
    def __init__(self, which, generatedNumbers1, generatedNumbers2, myNumbers, myNumbers2, hitsOnFirst=0, hitsOnSecond=0):
        self.which = which
        self.generatedNumbers1 = generatedNumbers1
        self.generatedNumbers2 = generatedNumbers2
        self.myNumbers = myNumbers
        self.myNumbers2 = myNumbers2
        self.hitsOnFirst = str(hitsOnFirst)
        self.hitsOnSecond = str(hitsOnSecond)

        whichToCheck = {
            '1': self.lotto,
            '2': self.minilotto,
            '3': self.multimulti,
            '4': self.extrasalary,
            '5': self.eurojackpot,
            '6': self.fast600
        }

        # Redirection to the appropriate function to set the right values of winTable

        whichToCheck[self.which]()

        # Checking the degree of winning and printing already existing generated numbers and yours

        if self.hitsOnFirst + self.hitsOnSecond in self.winTable:
            print("\nCongratulations! I's a",
                  self.winTable[self.hitsOnFirst + self.hitsOnSecond])

            if self.generatedNumbers2 is not None:
                print("\nYour numbers: ", self.myNumbers, self.myNumbers2)
                print("\nGenerated numbers: ", self.generatedNumbers1, self.generatedNumbers2)
            else:
                print("\nYour numbers: ", self.myNumbers)
                print("\nGenerated numbers: ", self.generatedNumbers1)

        else:
            print("\nSorry you have",
                int(self.hitsOnFirst) + int(self.hitsOnSecond),
                "hits. There is no prize for you")

            if self.generatedNumbers2 is not None:
                print("\nYour numbers: ", self.myNumbers, self.myNumbers2)
                print("\nGenerated numbers: ", self.generatedNumbers1, self.generatedNumbers2)
            else:
                print("\nYour numbers: ", self.myNumbers)
                print("\nGenerated numbers: ", self.generatedNumbers1)

    # Declaration of the degree of winnings for individual lotteries

    def lotto(self):
        self.winTable = {
            '60': "1st degree win",
            '50': "2nd degree win",
            '40': "3rd degree win",
            '30': "4th degree win"
        }

    def minilotto(self):
        self.winTable = {
            '50': "1st degree win",
            '40': "2nd degree win",
            '30': "3rd degree win"
        }

    def multimulti(self):
        self.winTable = {
            '100': "1st degree win",
            '90': "2nd degree win",
            '80': "3rd degree win",
            '70': "4th degree win",
            '60': "5th degree win",
            '50': "6th degree win",
            '40': "7th degree win"
        }

    def extrasalary(self):
        self.winTable = {
            '51': "1st degree win",
            '50': "2nd degree win",
            '41': "3rd degree win",
            '40': "4th degree win",
            '31': "5th degree win",
            '30': "6th degree win",
            '21': "7th degree win",
            '20': "8th degree win"
        }

    def eurojackpot(self):
        self.winTable = {
            '52': "1st degree win",
            '51': "2nd degree win",
            '50': "3rd degree win",
            '42': "4th degree win",
            '41': "5th degree win",
            '40': "6th degree win",
            '32': "7th degree win",
            '31': "8th degree win",
            '30': "9th degree win",
            '12': "10th degree win",
            '21': "11th degree win"
        }

    def fast600(self):
        self.winTable = {
            '60': "1st degree win",
            '50': "2nd degree win",
            '40': "3rd degree win",
            '30': "4th degree win",
            '20': "5th degree win"
        }
