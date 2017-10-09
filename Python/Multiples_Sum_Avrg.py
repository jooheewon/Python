# Multiples
# Multiples Part I

for oddNum in range(1,1000,2):
    print oddNum

#Multiples Part II
for multiFive in range(5,1000000,5):
    print multiFive

#Sum List
a = [1,2,5,10,255,3]
sum = 0
for i in a:
    sum += i
print sum

#Average List
a = [1,2,4,10,255,3]
def avrg(a):
    return (sum(a) / len(a))
