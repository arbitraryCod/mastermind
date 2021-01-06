import random
import saver
FILENAME="scoreboard"
EASY="easy"
HARD="hard"
NORMAL="normal"
class board():
    def __init__(self, numberOfInts,difficulty):
        self.guesses=0
        self.numbers=[]
        self.difficulty=difficulty
        self.numberOfInts=numberOfInts
        self.running=True
        try:
            self.scoreBoard=saver.load(FILENAME)
            print(self.getHighScore())
        except:
            self.scoreBoard=[]
        for i in range(numberOfInts):
            self.numbers.append(random.randint(0,9))
        print(self.numbers)
    def go(self):
        guess=input("number:")
        correctPos=[]
        correct=0
        if len(guess)==self.numberOfInts:
            self.guesses+=1
##            guessAsInts=[]
            for i in range (self.numberOfInts):
 ##               guessAsInts.append(int(guess[i]))
                if int(guess[i])==self.numbers[i]:
                    correct+=1
                    correctPos.append("correct")
                else:
                    correctPos.append("incorect")
        if correct==self.numberOfInts:
            self.win()
        else:
            if self.difficulty==EASY:
                self.display(correctPos)
            else:
                self.display(correct)
    def win(self):
        self.display("correct it took you %s goes"%self.guesses)
        self.scoreBoard.append([input("name:"),self.difficulty,self.guesses])
        self.running=False
        for i in self.scoreBoard:
            print(i)
        saver.save(FILENAME,self.scoreBoard)
    def display(self, string):
        print(string)
    def getHighScore(self):
        tempBoard=[]
        for i in self.scoreBoard:
            if i[1]==self.difficulty:
                tempBoard.append(i)
        tempHigh=[0,0]
        for i in range(len(tempBoard)):
            if tempBoard[i][2]<tempHigh[1]:
                tempHigh=[i,tempBoard[i][2]]
        return tempBoard[tempHigh[0]]
def main():
    z=""
    while not (z in [NORMAL,HARD,EASY]):
        z=input("difficulty (easy/normal/hard):").lower()
    if z==HARD:
        myBoard=board(5,z)
    if z==NORMAL:
        myBoard=board(4,z)
    if z==EASY:
        myBoard=board(4,z)
    while myBoard.running:
        myBoard.go()
main()
