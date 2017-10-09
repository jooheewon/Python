class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "The cost of this bike is $" + str(self.price)
        print "This bike goes " + str(self.max_speed) + " max"
        print "Total miles are " + str(self.miles)

        return self

    def ride(self):
        print "Riding"
        self.miles += 10

        return self

    def reverse(self):
        print "Reversing"
        self.miles -= 5

        return self

bike1 = Bike(200, "25mph")
bike1.ride().ride().ride().reverse().displayInfo()

bike2 = Bike(300, "50mph")
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3 = Bike(140, "20mph")
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()
