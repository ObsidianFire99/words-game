import math
import random
import datetime
import resources
output = []

def check(checknum):
    breakfunc = "F"
    for i in output[:]:
        if i == checknum:
            breakfunc = "T"
        if i == 0:
            breakfunc = "T"
    return breakfunc

def wcreate(seed):
    seed = seed*seed
    seed = seed*seed
    seed = seed*seed
    seedlist = resources.splitdig(seed)
    wcount = 1
    try:
        for i in seedlist[:]:
            if i == 0:
                seedlist.remove(i)
        while not len(output) == 9:
            if seedlist[wcount - 1]%2 == 0:
                if not check(seedlist[-wcount]) == "T":
                    output.append(seedlist[-wcount])
                else:
                    pass
            else:
                if not check(seedlist[-wcount + 1]) == "T":
                    output.append(seedlist[-wcount + 1])
                else:
                     pass
            wcount = wcount + 1
    except IndexError:
        print "Please Enter another seed, your last one was broken"
        customseed()
    return output[:]

def customseed():
    cseed = input("Enter a number with more than five digits and less than ten: ")
    load = list(wcreate(cseed))
    return load
