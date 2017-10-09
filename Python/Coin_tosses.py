import random

def cointosses(reps):
    attempt = 1
    head = 0
    tail = 0
    result = ""

    for i in range(1, reps):
        toss = random.randint(0,1)
        if toss == 1:
            head += 1
            result = "head"
            print "Attempt #", attempt, ": Throwing a coin... It's a ", result, "! God ", head, "head(s) so far and", tail, "tail(s) so far"
        else:
            tail += 1
            result = "tail"
            print "Attempt #", attempt, ": Throwing a coin... It's a ", result, "! God ", head, "head(s) so far and", tail, "tail(s) so far"
        attempt += 1

cointosses(5001)
