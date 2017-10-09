# Find and Replace
words = "It's thanksgiving day. It's my birthday, too!"
print words.replace("day", "month")

#Min and Max
x = [2,54,-2,7,12,98]
print max(x)
print min(x)

#First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[-1]

#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
first_list = x[:len(x)/2]
second_list = x[len(x)/2:]
print first_list
print second_list
second_list.insert(0, first_list)
print second_list
