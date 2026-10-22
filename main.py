#I have 18 total functions and 4 with parameters
#my special feature is a typewriter effect that prints text from left to right as if you were typing on a typewriter
#timing: YES
#spacing: YES
#color on choices: YES     colorfunction on Schoology: YES
#invalid choices repeat function: YES
#lowercase and uppercase responses same: Yes
#name repeated: Yes
#code is mine: Yes



import time

class fg:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

class bg:
    BLACK   = '\033[40m'
    RED     = '\033[41m'
    GREEN   = '\033[42m'
    YELLOW  = '\033[43m'
    BLUE    = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN    = '\033[46m'
    WHITE   = '\033[47m'
    RESET   = '\033[49m'

class style:
    BRIGHT    = '\033[1m'
    DIM       = '\033[2m'
    NORMAL    = '\033[22m'
    RESET_ALL = '\033[0m'

#this is a function with 3 parameters
def color(tColor,bColor,text):
    #return means "give back" something at the line
    #where you call the function
  return tColor+bColor+text+fg.RESET+bg.RESET

# Start of story
def askForName():
    global name
    name = input("What is your name? ")
    placeLines(1)
    print("Hello " + name + ", it is nice to meet you.")
  
def missionIntro():
    print(name + ", your mission is to infiltrate a tech corporate campus and steal their designs.")
    print("You have two options to get inside the facility.")
    placeLines(1)
    time.sleep(1)
    choice = input("\n\nYou can " + color(fg.RED,bg.BLACK,"cut") + " through the fence, OR " + color(fg.RED,bg.BLACK,"hide") + " in a van entering the building: ")
   
    if choice.upper() == "CUT": #also check for lowercase/uppercase
      print("Great choice")
      placeLines(1)
      time.sleep(2)
      cut()
    elif choice.upper() == "HIDE":
      print("Great Choice")
      placeLines(1)
      time.sleep(2)
      hide()
    else:
      print("\n\nInvalid choice")
      placeLines(1)
      missionIntro()

def cut():
    print("\n\nYou have two options to get inside the laboratory.")
    placeLines(1)
    time.sleep(1)
    choice = input("\nYou can " + color(fg.RED,bg.BLACK,"sneak") + " through the fence, OR " + color(fg.RED,bg.BLACK,"walk") + " past everyone, pretending to be a custodian: ")
   
    if choice.upper() == "SNEAK":
      print("Great choice")
      placeLines(1)
      time.sleep(2)
      sneak()
    elif choice.upper() == "WALK":
      print("Great Choice")
      placeLines(1)
      time.sleep(2)
      walk()
    else:
      print("\nInvalid choice")
      placelines(1)
      cut()

def hide():
    print("\n\nYou sneak into a delivery van entering the facility.")
    print("The delivery van stops suddenly! The driver gets out and looks straight at you!")
    placeLines(1)
    time.sleep(1)
    choice = input("\nYou can " + color(fg.RED, bg.BLACK, "ask") + " where the restroom is, OR " + color(fg.RED, bg.BLACK, "hide") + " behind shipping pallets: ")
   
    if choice.upper() == "ASK":
      print("Great choice")
      placeLines(1)
      time.sleep(2)
      askRestroom()
    elif choice.upper() == "HIDE":
      print("Great Choice")
      placeLines(1)
      time.sleep(2)
      palletHide()
    else:
      print("\nInvalid choice")
      hide()

def sneak():
    print("\n\nThe guard passes by. You slip through a side door into a quiet corridor, " + name + ".")
    print("You find an empty security desk with a keycard and a camera tablet.")
    placeLines(1)
    time.sleep(1)
    choice = input("\nYou can " + color(fg.RED, bg.BLACK, "swipe") + " the card and move, OR " + color(fg.RED, bg.BLACK, "check") + " guard routes on the tablet: ")

    if choice.upper() == "SWIPE":
        print("Keycard grabbed! You bypass security and move straight to the core.")
        placeLines(1)
        time.sleep(2)
        dataCore()
    elif choice.upper() == "CHECK":
        print("You memorize patrol routes and learn the code for the breakroom door!")
        place  
        time.sleep(2)
        breakroom()
    else:
        print("\nInvalid choice")
        sneak()

def walk():
    print("\n\nThe custodian disguise fails! A guard demands an ID badge you don't have, " + name + "!")
    time.sleep(1)
    choice = input("\nYou can " + color(fg.RED, bg.BLACK, "sprint") + " for the exit, OR " + color(fg.RED, bg.BLACK, "walk") + " backward out the door apologizing: ")

    if choice.upper() == "SPRINT":
        print(color(fg.RED, bg.BLACK, "\nLaser barriers activate! You are forced to restart at the previous stage."))
        time.sleep(2)
        missionIntro()  #loop back
    elif choice.upper() == "WALK":
        print(color(fg.RED, bg.BLACK, "\nThe guard escorts you completely off the campus perimeter. You are forced to restart at the previous stage"))
        time.sleep(2)
        missionIntro()  #loop back
    else:
        print("\nInvalid choice")
        walk()

def askRestroom():
    print("\n\nThe employee points down the hall. You enter the lounge, but the exit door requires a code.")
    print(name + ", you see a sticky note with numbers scribbled on it on the table.")
    time.sleep(1)
    choice = input("\nYou can " + color(fg.RED, bg.BLACK, "enter") + " the code from the sticky note, OR " + color(fg.RED, bg.BLACK, "use") + " a credit card to jam the lock: ")

    if choice.upper() == "ENTER":
        print("Success! The door clicks open.")
        placeLines(1)
        time.sleep(2)
        dataCore()
    elif choice.upper() == "USE":
        print("The card snaps in the lock and triggers a local alarm! You hurry into the server hall.")
        placeLines(1)
        time.sleep(2)
        serverCorridor()
    else:
        print("\nInvalid choice")
        askRestroom()

def palletHide():
    print("\n\nYou hide successfully and slip into the server corridor.")
    print("Suddenly, a fire alarm flashes and locks down the magnetic doors!")
    placeLines(1)
    time.sleep(1)
    choice = input("\nYou can " + color(fg.RED, bg.BLACK, "break") + " the glass case for an axe, OR " + color(fg.RED, bg.BLACK, "cut") + " power at the electrical panel: ")

    if choice.upper() == "BREAK":
        print("Smashing the glass triggers heavy metal shutters! Path blocked!")
        print("You are forced to restart at the previous stage.")
        placeLines(1)
        time.sleep(1)
        hide()  #loop back
    elif choice.upper() == "CUT":
        print("Power cut! The magnetic locks release with a click.")
        placeLines(1)
        time.sleep(1)
        dataCore()
    else:
        print("\nInvalid choice")
        palletHide()

def placeLines(num):
    for i in range(num):
        print("------------------------------------------------------")



def typeWriter(text, delay):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(delay)
    print() 

def printHeader(stageTitle):
    placeLines(1)
    print("******************************************************")
    print(color(fg.CYAN, bg.BLACK, "=== " + stageTitle + " ==="))
    print("******************************************************")
    time.sleep(1)

def breakroom():
    printHeader("STAGE 6: THE BREAKROOM")
    askRestroom()

def serverCorridor():
    printHeader("STAGE 7: THE SERVER CORRIDOR")
    palletHide()

def dataCore():
    printHeader("STAGE 8: THE DATA CORE")

    typeWriter(color(fg.GREEN, bg.BLACK, "\n[CONNECTING TO CENTRAL TERMINAL...]"), 0.03)
    typeWriter(color(fg.GREEN, bg.BLACK, "SYSTEM ACCESS GRANTED."), 0.03)
    
    print("\nYou made it inside the server room, " + name + "!")
    print("A flash drive is plugged into the main console with your stolen research.")
    placeLines(1)

    typeWriter(color(fg.YELLOW, bg.BLACK, "\n[!] WARNING: AUTOMATED DATA WIPE IN PROGRESS [!]"), 0.02)
    typeWriter(color(fg.RED, bg.BLACK, "60 SECONDS UNTIL DRIVE PURGE..."), 0.03)

    time.sleep(1)
    choice = input("\nYou can " + color(fg.RED, bg.BLACK, "pull") + " the drive immediately, OR " + color(fg.RED, bg.BLACK, "unmount") + " safely unmount it via terminal: ")

    if choice.upper() == "PULL":
        print("Great choice")
        placeLines(1)
        time.sleep(2)
        pullDrive()
    elif choice.upper() == "UNMOUNT":
        print("Great Choice")
        placeLines(1)
        time.sleep(2)
        unmountDrive()
    else:
        print("\nInvalid choice")
        dataCore()

def pullDrive():
    typeWriter(color(fg.RED, bg.BLACK, "\n\nMISSION END: PARTIAL VICTORY"), 0.04)
    print("You pulled the drive and ran, " + name + "!")
    print("You escaped, but pulling it mid-transfer corrupted some research files.")
    placeLines(1)
    playAgain()

def unmountDrive():
    typeWriter(color(fg.GREEN, bg.BLACK, "\n\nMISSION END: PERFECT VICTORY!"), 0.04)
    print("Great work, Agent " + name + "!")
    print("You unmounted the drive safely, erased your digital tracks, and escaped undetected!")
    placeLines(1)
    playAgain()

def displayTitle():
    typeWriter(color(fg.BLUE, bg.BLACK, "=========================================="), 0.01)
    typeWriter(color(fg.BLUE, bg.BLACK, "       THE CORPORATE BREACH ADVENTURE      "), 0.02)
    typeWriter(color(fg.BLUE, bg.BLACK, "=========================================="), 0.01)

def playAgain():
    again = input("\nWould you like to play again, " + name + "? (YES/NO): ")
    if again.upper() == "YES":
        missionIntro()
    else:
        endGame()

def endGame():
    typeWriter("\nThanks for playing, " + name + "!", 0.03)

def main():
    displayTitle()
    askForName()
    missionIntro()

main()
