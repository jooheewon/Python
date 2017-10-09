Mixed = ['magical unicorns',19,'hello',98.98,'world']
Num = [2,3,1,7,4,12]
Str = ['magical','unicorns']

def listType(list):
    newlist = ""
    total = 0

    for value in list:
        if isinstance(value, int) or isinstance(value, float):
            total += value
        elif isinstance(value, str):
            newlist += value

    if newlist and total:
        print "The array you entered is a mixed type"
        print "String", newlist
        print "Total", total

    elif newlist:
        print "The array you entered is of string type"
        print "String",newlist

    else:
        print "The array you entered is a number(float or int)type"
        print "total", total

print listType(Mixed)
print listType(Num)
print listType(Str)
