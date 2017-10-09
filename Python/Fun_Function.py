#Odd/Even
def odd_even():
    for num in range(1,2001):
        if num % 2 == 0:
            print "Number is", num, "This is an even number"
        else:
            print "Number is", num, "This is an odd number"

#Multiply
def multiply(a):
    newList = []
    for i in a:
        newList.append(i*5)
    print (newList)

a = [2,4,10,16]
multiply(a)

#Hacker Challenge
