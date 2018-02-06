#!/usr/bin/python3
import random;
import sys

class TerminalColor:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class calculator:
    
    def __init__(self, task="normal"):
        self.task = task
        self.corrects = 0
        self.wrongs = 0
        self.scorearray = [0,0]
        self.wantq=False
        print(self.task)
        self.menu()
    
    def menu(self):
        if (self.task =="addition"):
            self.corrects = self.add()
        else:
            print("esle")
            self.user = input('Enter Username ')
            if self.user == "q":
                self.wantq=True
            while (self.wantq==False):
                print(TerminalColor.YELLOW + "\nYou like to exercise \n(a)ddition/(m)ultiplication/(s)ubtracation/(q)uit ? ",
                      TerminalColor.ENDC)
                self.answer = input();
                if (self.answer == "q"):
                    break;
                elif (self.answer == "a"):
                    self.scorearray = self.add();
                    self.corrects += self.scorearray[0];
                    self.wrongs += self.scorearray[1]
                elif (self.answer == "m"):
                    self.scorearray = self.multi();
                    self.corrects += self.scorearray[0];
                    self.wrongs += self.scorearray[1]
                elif (self.answer == "s"):
                    self.scorearray = self.substract();
                    self.corrects += self.scorearray[0];
                    self.wrongs += self.scorearray[1]

    def add(self):
        print("you are doing addition")
        self.correct = 0;
        self.wrong = 0;
        for self.x in range(1,6):
            self.num1 = random.randint(10, 190);
            self.num2 = random.randint(10, 190);
            print("This is your", self.x, "question.")
            print("How much ", self.num1, " + ",self.num2, "? ");
            self.res = self.num1 + self.num2;
            while (True):
                self.answer = input();
                if (self.answer=="q"):
                    break
                elif (self.answer == str(self.res)):
                    print(TerminalColor.GREEN + "Great!" + TerminalColor.ENDC);
                    self.correct += 1;
                    break
                else:
                    print(TerminalColor.RED + "Wrong!" + TerminalColor.ENDC);
                    self.wrong += 1;
                    break
            if (self.answer=="q"):
                break
        self.writeResult(self.user,self.correct*20,'a')
        print("You answered ", self.correct, " questions correct and ", self.wrong, " questions wrong!");
        return (self.correct, self.wrong)

    def multi(self):
        self.correct = 0;
        self.wrong = 0;
        for self.x in range(1,6):
            self.exitmulti = False
            self.num1 = random.randint(2,14);
            self.num2 = random.randint(2,14);
            print("This is your", self.x, "question.")
            print("How much", self.num1, " * ",self.num2, "? ");
            self.res = self.num1 * self.num2;
            while (self.exitmulti == False):
                self.answer = input();
                if (self.answer == "q"):
                    self.exitmulti = True
                try:#if answer == str(res): auch moeglich
                    self.answer = int(self.answer)
                    if (type(self.answer) == int):
                        break
                except ValueError:
                    if (self.answer != "q"):
                        print("This is no integer!")
            if (self.exitmulti == True):
                break
            if (self.res == self.answer):
                print(TerminalColor.GREEN + "Great!" + TerminalColor.ENDC);
                self.correct += 1;
            else:
                print(TerminalColor.RED + "Wrong!" + TerminalColor.ENDC);
                self.wrong += 1;
        self.writeResult(self.user, self.correct*20,'m')
        print("You answered ", self.correct, " questions correct and ", self.wrong, " questions wrong!")
        return (self.correct, self.wrong)

    def substract(self):
        self.correct = 0;
        self.wrong = 0;
        for self.x in range(1,6):
            self.exitsubs = False
            self.num1 = random.randint(100,290);
            self.num2 = random.randint(40,120);
            print("This is your", self.x, "question.")
            print("How much", self.num1, " - ",self.num2, "? ");
            self.res = self.num1 - self.num2;
            while (self.exitsubs == False):
                self.answer = input();
                if (self.answer == "q"):
                    self.exitsubs = True
                try:#if answer == str(res): auch moeglich
                    self.answer = int(self.answer)
                    if (type(self.answer) == int):
                        break
                except ValueError:
                    if (self.answer != "q"):
                        print("This is no integer!")
            if (self.exitsubs == True):
                break
            if (self.res == self.answer):
                print(TerminalColor.GREEN + "Great!" + TerminalColor.ENDC);
                self.correct += 1;
            else:
                print(TerminalColor.RED + "Wrong!" + TerminalColor.ENDC);
                self.wrong += 1;
        self.writeResult(self.user, self.correct*20,'s')
        print("You answered ", self.correct, " questions correct and ", self.wrong, " questions wrong!")
        return (self.correct, self.wrong)
        
    def writeResult (self, user,perc,task):
        self.out = open('result.txt','a')
        self.out.write(user+"\t"+str(perc)+"\t"+task+"\n")
        self.out.close()


def main():
    if (len(sys.argv)==1):
        mycalc = calculator()
    elif (len(sys.argv)==2):
        mycalc = calculator(sys.argv[1])
    else:
        sys.exit(1)


if (__name__ == "__main__"):
    main();




'''
        self.user = input('Enter Username ')
        if self.user == "q":
            self.wantq=True
        while (self.wantq==False):
            print(TerminalColor.YELLOW + "\nYou like to exercise \n(a)ddition/(m)ultiplication/see your (s)core/(q)uit ? ",
                  TerminalColor.ENDC)
            self.answer = input();
            if (self.answer == "q"):
                break;
            elif (self.answer == "a"):
                self.scorearray = self.add(self);
                self.corrects += self.scorearray[0];
                self.wrongs += self.scorearray[1]
            elif (self.answer == "m"):
                self.scorearray = self.multi(self);
                self.corrects += self.scorearray[0];
                self.wrongs += self.scorearray[1]
            elif (self.answer == "s"):
                print("You answered", self.corrects," correct and", self.wrongs,"wrong!");
            '''
    
