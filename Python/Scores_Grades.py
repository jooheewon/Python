import random

def transcript(list):
    for i in range(0, list):
        score = random.randint(60, 101)
        if score >= 60 and score <= 69:
            print "Score: ", score, "; Your grade is D"
        elif score >= 70 and score <= 79:
            print "Score: ", score, "; Your grade is C"
        elif score >= 80 and score <= 89:
            print "Score: ", score, "; Your grade is B"
        else:
            print "Score: ", score, "; Your grade is A"

transcript(10)
