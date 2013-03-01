def startmessage(name):
    print "Ah, it is good to see you well,", name
    return None
def chamberone():
    # Placeholder
    return None
def chambertwo():
    # Placeholder
    return None
def chamberthree():
    # Placeholder
    return None
def chamberfour():
    # Placeholder
    return None
def chamberfive():
    # Placeholder
    return None
def chambersix():
    # Placeholder
    return None
def chamberseven():
    # Placeholder
    return None
def chambereight():
    # Placeholder
    return None
def chambernine():
    # Placeholder
    return None
    
def start():
    inlogo = open('logo.txt', 'r')
    for i in inlogo:
        print i
    print ""
    print ""
    print "A OneTen Production"
    def choice():
        userchoice = raw_input("Type P to Play!!!")
        if userchoice == "P":
            username = raw_input("How do they call you in the lands you are from: ")
            startmessage(username)
        else:
            choice()
    choice()
        
start()
