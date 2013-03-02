words = ["You", "really", "believed", "it", "would", "be", "that", "easy.", "Wrong."]
wordlist = []
import math
import time
import sys
import random
global username
username = "user"
global wordcount
wordcount = 1

def finish():
    print "Ah,", username, "You Finished!"
    print "The Sentence was..."
    for i in wordlist[:]:
        print i
    time.sleep(3)
    print "To be Continued..."
    raw_input("Press Enter to Return to game mode. Read those Witty Comments You Missed!")
    
def startmessage():
    print "Owww... My Head Hurts"
    time.sleep(2)
    print "Aaargh! I can't see anything! I've gone blind!"
    time.sleep(2)
    print "Wait... I'm just in a dark room, that's all. My eyes need time to adjust to the light."
    time.sleep(2)
    print "What's this on the floor... It's a book!"
    time.sleep(2)
    print "Oh. It's Empty"
    time.sleep(2)
    print "Well, I'm gonna be stuck in here for a while... so I'd better make it my diary!"
    time.sleep(2)
    print "Wait... It does have writing on the inside front cover."
    time.sleep(2)
    print ""
    print ""
    indp = open('dear_prisoner.txt', 'r')
    for i in indp:
        print i
        time.sleep(2)
    indp.close()
    print "+-"*240
    time.sleep(2)
    print "Oh Man, How did I end up here?"
    time.sleep(2)
    print "I always was a good boy."
    time.sleep(2)
    print "I brushed my teeth for two minutes each day."
    time.sleep(2)
    print "I didn't talk back to my parents."
    time.sleep(2)
    print "I didn't cover my sister's doll in petrol and set it alight (well, maybe I did, but it was worth it!)."
    time.sleep(2)
    print "All I did was write a book, and I ended up here."
    time.sleep(2)
    print "Well, if I have to look for words, I'd better start looking."
    chamberone()
    return None

def chamberone():
    print ""
    print "Chamber One"
    global wordcount
    if wordcount == 4:
        print "Word 4 Found"
        word = words[wordcount - 1]
        wordlist.append(word)
        wordcount = wordcount + 1
        
    else:
        print "What the heck? How can I know I find something if I can't see it?"
        
    direction = raw_input("Type N to go North or E to go East: ")
    if direction == "N":
        chamberfour()
    elif direction == "E":
        chambertwo()
    else:
        print "You can't even type in a letter correctly. Let's try this chamber again."
        chamberone()    
    return None

def chambertwo():
    print ""
    print "Chamber Two"
    global wordcount
    if wordcount == 2:
        print "Word 2 Found"
        word = words[wordcount - 1]
        wordlist.append(word)
        wordcount = wordcount + 1
        
    else:
        print "Yikes!!! Thats a skull!"
        print "Oh wait, it's just a rock. No words here though"
        
    direction = raw_input("Type N to go North, E to go East, or W to go West: ")
    if direction == "N":
        chamberfive()
    elif direction == "E":
        chamberthree()
    elif direction == "W":
        chamberone()
    else:
        print "You can't even type in a letter correctly. Let's try this chamber again."
        chambertwo()
    return None

def chamberthree():
    print ""
    print "Chamber Three"
    global wordcount
    if wordcount == 6:
        print "Word 6 Found"
        word = words[wordcount - 1]
        wordlist.append(word)
        wordcount = wordcount + 1
        
    else:
        print "I'm surprised the ceiling on this room is still intact. If I jump it might come down on my head by the looks of it!"
        
    direction = raw_input("Type N to go North or W to go West: ")
    if direction == "N":
        chambersix()
    elif direction == "W":
        chambertwo()
    else:
        print "You can't even type in a letter correctly. Let's try this chamber again."
        chamberthree()
    return None

def chamberfour():
    print ""
    print "Chamber Four"
    global wordcount
    if wordcount == 5:
        print "Word 5 Found"
        word = words[wordcount - 1]
        wordlist.append(word)
        wordcount = wordcount + 1
        
    else:
        print "Yuk! A mouldy sandwich. It smells of the cheese my granny has in her socks."
        print "But there's no words. How hard can they be to find?"
        
    direction = raw_input("Type N to go North, E to go East, or S to go South: ")
    if direction == "N":
        chamberseven()
    elif direction == "E":
        chamberfive()
    elif direction == "S":
        chamberone()
    else:
        print "You can't even type in a letter correctly. Let's try this chamber again."
        chamberfour()
    return None

def chamberfive():
    print ""
    print "Chamber Five"
    global wordcount
    if wordcount == 9:
        print "Word 9 Found"
        word = words[wordcount - 1]
        wordlist.append(word)
        finish()
        
    else:
        print "This room is bigger than the others *Clang!* *OW!*"
        print "And as my head just discovered, there are chains hanging from the ceiling!"
        
    direction = raw_input("Type N to go North, E to go East, S to go South or W to go West: ")
    if direction == "N":
        chambereight()
    elif direction == "E":
        chambersix()
    elif direction == "S":
        chambertwo()
    elif direction == "W":
        chamberfour()
    else:
        print "You can't even type in a letter correctly. Let's try this chamber again."
        chamberfive()
    return None

def chambersix():
    print ""
    print "Chamber Six"
    global wordcount
    if wordcount == 8:
        print "Word 8 Found"
        word = words[wordcount - 1]
        wordlist.append(word)
        wordcount = wordcount + 1
        
    else:
        print "Words, Words, I hate Words."
        print "Cavemen had the right idea with their pictures!"
    direction = raw_input("Type N to go North, W to go West, or S to go South: ")
    if direction == "N":
        chambernine()
    elif direction == "W":
        chamberfive()
    elif direction == "S":
        chamberthree()
    else:
        print "You can't even type in a letter correctly. Let's try this chamber again."
        chambersix()
    return None
def chamberseven():
    print ""
    print "Chamber Seven"
    global wordcount
    if wordcount == 1:
        print "Word 1 Found"
        word = words[wordcount - 1]
        wordlist.append(word)
        wordcount = wordcount + 1
        
    else:
         print "I hope I don't die in here"
         print "I would hate to die, alone in the dark and the cold."
        
    direction = raw_input("Type E to go East, or S to go South: ")
    if direction == "E":
        chambereight()
    elif direction == "S":
        chamberfour()
    else:
        print "You can't even type in a letter correctly. Let's try this chamber again."
        chamberseven()
    return None
def chambereight():
    print ""
    print "Chamber Eight"
    global wordcount
    if wordcount == 7:
        print "Word 7 Found"
        word = words[wordcount - 1]
        wordlist.append(word)
        wordcount = wordcount + 1
        
    else:
        print "OH NO! I'm Trapped!"
        print "It's cobwebs... Wait I can cut them with this rock. Stupid Arachnida."
        
    direction = raw_input("Type W to go West, E to go East, or S to go South: ")
    if direction == "W":
        chamberseven()
    elif direction == "E":
        chambernine()
    elif direction == "S":
        chamberfive()
    else:
        print "You can't even type in a letter correctly. Let's try this chamber again."
        chambereight()
    return None
def chambernine():
    print ""
    print "Chamber Nine"
    global wordcount
    if wordcount == 3:
        print "Word 3 Found"
        word = words[wordcount - 1]
        wordlist.append(word)
        wordcount = wordcount + 1
        
    else:
        print "I wonder where I can buy a postcard?"
        print "Dear Mom, I'm starving to death in a mouldy dungeon, hope you had a nice weekend, see you soon."

    direction = raw_input("Type W to go West, or S to go South: ")

    if direction == "W":
        chambereight()
    elif direction == "S":
        chambersix()
    else:
        print "You can't even type in a letter correctly. Let's try this chamber again."
        chambernine()
    return None
    
def start():
    print "+-+-+-+-+-+-+-+-"*480
    inlogo = open('logo.txt', 'r')
    for i in inlogo:
        print i
    inlogo.close()
    print ""
    print ""
    print "A OneTen Production"
    def choice():
        userchoice = raw_input("Type P to Play!!!")
        if userchoice == "P":
            global username
            username = raw_input("How do they call you in the lands you are from: ")
            skipin = raw_input("Would You like to skip the intro? (Y/N): ")
            if skipin == "Y":
                chamberone()
            else:
                startmessage()
        else:
            choice()
    choice()
        
start()
