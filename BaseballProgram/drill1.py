'''CURRENT ERRORS: PITCHES THAT ARE BALLS ARE REGISTERING CORRECTLY
                   HUGE ISSUES WITH WHEN THE BALL IS ACTUALLY HIT
                   NAMELY AREAS THAT CONTAIN "atThePlate(strike,ball,BattersName)"
'''                   

import random
import hitPer

#These are the chances each batter has on what base they get on their hit

baseA = ['Single'] * 90 + ['Double'] * 32 + ['Triple'] * 5 + ['Home Run!!!'] * 37
baseB = ['Single'] * 51 + ['Double'] * 16 + ['Triple'] * 0 + ['Home Run!!!'] * 7
baseC = ['Single'] * (153-31-7-8) + ['Double'] * 31 + ['Triple'] * 7 + ['Home Run!!!'] * 8
baseD = ['Single'] * (182-30-3-15) + ['Double'] * 30 + ['Triple'] * 3 + ['Home Run!!!'] * 15
baseE = ['Single'] * (67-9-1-6) + ['Double'] * 9 + ['Triple'] * 1 + ['Home Run!!!'] * 6
baseF = ['Single'] * (111-21-7-10) + ['Double'] * 21 + ['Triple'] * 7 + ['Home Run!!!'] * 10
baseG = ['Single'] * (184-47-5-25) + ['Double'] * 47 + ['Triple'] * 5 + ['Home Run!!!'] * 25
baseH = ['Single'] * (50-8-4-6) + ['Double'] * 8 + ['Triple'] * 4 + ['Home Run!!!'] * 6
baseI = ['Single'] * (128-28-21) + ['Double'] * 28 + ['Triple'] * 0 + ['Home Run!!!'] * 21
baseJ = ['Single'] * (93-18-1-15) + ['Double'] * 18 + ['Triple'] * 1 + ['Home Run!!!'] * 15

Pfast = 'It looks like its a Fastball!'
Pcurve = 'It looks like its a Curveball!'
Pslider = 'It looks like its a Slider! Swing?'
Pchange = 'It looks like its a Change-Up! Swing?'
Pball = 'It looks like its going to be a Ball!'

battersAL = {
    'josh donaldson' : ['TOR', .417, baseA],
    'brock holt' : ['BOS', .400, baseB],
    'elvis andrus' : ['TEX', .364, baseC],
    'francisco lindor' : ['CLE', .323, baseD],
    'ezequiel carrera' : ['TOR', .303, baseE]
    }
battersNL = {
    'joe panik' : ['SF', .462, baseF],
    'daniel murphy' : ['WSH', .438, baseG],
    'conor gillaspie' : ['SF', .421, baseH],
    'jayson werth' : ['WSH', .389, baseI],
    'ryan zimmerman' : ['WSH', .353, baseJ]
    }


#List of AL/NL batters depending on which division the user chooses

strike = 0
ball = 0
hit = 0

def start(strike=0,ball=0,battersName=""):
    battersName = atBat(battersName)
    strike,ball,battersName = atThePlate(strike,ball,battersName)


def atBat(battersName):
    try:
        battersInfo = battersAL[battersName]
        print ('Batter: ' + battersName.title())
        print ('Team: ' + battersInfo[0])
        print ('Batting Avg: ' + str(battersInfo[1]))
    except:
        print('Please Try Again')

def atBatNL(battersName):
    try:
        battersInfoNL = battersNL[battersName]
        print ('Batter: ' + battersName.title())
        print ('Team: ' + battersInfo[0])
        print ('Batting Avg: ' + str(battersInfo[1]))
    except:
        print('Please Try Again')
#These will bring the basic information of the batter they choose before they proceed

pickDiv = True
while pickDiv == True:
    side = input('Pick your All-Star Division! AL or NL? : ').lower()
    if side == 'al':
        userWantsMoreAL = True
        userWantsMoreNL = False
        pickDiv = False
    elif side == 'nl':
        userWantsMoreNL = True
        userWantsMoreAL = False
        pickDiv = False
    else:
        print ("please try again")
        pickDiv = True
#This is what allows them to pick the division they want to play for in the game

def out(strike,ball,battersName):
    print("\nThree Strikes and YOUUUUURRRRR OUT")
    again(strike,ball,battersName)

def walk(strike,ball,battersName):
    print("\nYou got walked! Nice Pressure!")
    again(strike,ball,battersName)

def hit(strike,ball,battersName):
    print("\nNice Hit! Your team cheers you on!")
    again(strike,ball,battersName)

def again(strike,ball,battersName):
    stop = True
    while stop:
        choice = input("\Do you want to try another batter? (y/n)").lower()
        if choice == "y":
            reset(strike,ball,battersName)
            stop = False
        if choice == "n":
            print("\nSee you next time slugger")
            stop = False
            exit()
        else:
            print("\nPlease enter 'y' for yes or 'n' for no")

def reset(strike,ball,battersName):
    strike = 0
    ball = 0
    battersName = ""
    start(strike,ball,battersName)

def pitchOptions():
    x = [Pfast, Pcurve, Pslider, Pchange, Pball, Pball, Pball, Pball]   
    print(random.choice(x))


def atThePlate(strike,ball,battersName):
    atThePlate = True
    battersInfo = battersAL[battersName]
    while atThePlate == True:
        show_count(strike,ball,battersName) #Show the count before every pitch
        x = pitchOptions()
        print(x)
        swing = input("\nSwing? (y/n) : ").lower()
        if x == Pball and swing == "y":
            print("miss")
            strike = (strike + 1)
            atThePlate = True
        elif x == Pball and swing == "n":
            print("good eye")
            ball = (ball + 1)
            atThePlate == True
        elif x != Pball and swing == "y":
            print("hit")
            print (random.choice(battersInfo[2]))
            hit(strike,ball,battersName)
            atThePlate = False
        elif x != Pball and swing == "n":
            print("down the middle")
            strike = (strike + 1)
            atThePlate = True
        else:    
            print("select y or n")
            atThePlate = True
            
            
##        if pitchOptions == "It looks like its going to be a Ball! Swing? (y/n) :" and pitch == "y": #If they swing at the ball
##            print ("\nSwing and a Miss that's a STRIKE!")
##            strike = (strike + 1)
##            atThePlate = False
##        elif pitchOptions == "It looks like its going to be a Ball! Swing? (y/n) :" and pitch == "n": #If they don't swing at the ball
##            print("\nGood Eye! That's a BALL")
##            ball = (ball + 1)
##            atThePlate = False
##        elif pitchOptions != "It looks like its going to be a Ball! Swing? (y/n) :" and (battersInfo[1] > hitPer.hitPercent(0)) and pitch == "y": 
##            print("\nThat's a hit! You got a") #Measure's their hitting average against a random number from the hitPer.py file and in this one they hit
##            print (str(random.choice(battersInfo[2])))
##            hit = (hit + 1)
##            atThePlate = False
##        elif pitchOptions != "It looks like its going to be a Ball! Swing? (y/n) :" and (battersInfo[1] < hitPer.hitPercent(0)) and pitch == "y":
##            print("\nSwing and a Miss that's a STRIKE!") #Same as above except they roll poorly and will miss the pitch
##            strike = (strike + 1)
##            atThePlate = False
##        elif pitchOptions != "It looks like its going to be a Ball! Swing? (y/n) :" and (hitPer.hitPercent(0) > 0.444) and pitch == "n":
##            print("\nStraight up the Middle! STRIKE!") #Strike pitch but it isn't swung at
##            strike = (strike + 1)
##            atThePlate = False
##        elif pitchOptions != "It looks like its going to be a Ball! Swing? (y/n) :" and (hitPer.hitPercent(0) < 0.444) and pitch == "n":
##            print("\nGood Eye! That's a BALL") #Ball pitch that isn't swung at
##            ball = (ball + 1)
##            atThePlate = False
##        else:
##            print("\Press 'y' to swing at the pitch and 'n' to not swing at the pitch! Try again!")
##            atThePlate = False
##        score(strike,ball,battersName)
#This is the likely buggy game itself of pitching/batting

def score(strike,ball,battersName):
    if strike >= 3:
        out(strike,ball,battersName)
    if ball >= 4:
        walk(strike,ball,battersName)
    else:
        atThePlate(strike,ball,battersName)

def show_count(strike,ball,battersName):
    print("\n{}, your count is {}-{} (Strike-Balls).".format(battersName,strike,ball))

while userWantsMoreAL == True:
    battersName = input('Josh Donaldson \nBrock Holt \nElvis Andrus \nFrancisco Lindor \nEzequiel Carrera \nPlease select a batter: ').lower()
    atBat(battersName)
    searchAgain = input ('Do you want to bat with {}? (y/n) :'.format(battersName))
    if searchAgain == 'y':
        atThePlate(strike,ball,battersName)
        userWantsMoreAL = False
    elif searchAgain == 'n':
        userWantsMoreAL = True
    else:
        print ("Please Select a Valid Batter")
        userWantsMoreAL = False
#Selection and verification of the AL batter        

while userWantsMoreNL == True:
    battersName = input('Joe Panik \nDaniel Murphy \nConor Gillaspie \nJayson Werth \nRyan Zimmerman \nPlease select a batter: ').lower()
    atBatNL(battersName)
    searchAgain = input ('Do you want to bat with {}?'.format(battersName))
    if searchAgain == 'y':
        userWantsMoreNL = False
    elif searchAgain == 'n':
        userWantsMoreNL = True
    else:
        print ("Please Select a Valid Batter")
        userWantsMoreNL = False
#Selection and verification of the NL batter

def pitch_game(battersName):
    if name != "":
        print ('{} steps up the the plate!'.format(battersName))
        atThePlate = True
    else:
        pickDiv = True
        atThePlate = False
#Chains the batter selection to the actual game


if __battersName__ == "__main__":
    start()
