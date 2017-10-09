class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

    def display_all(self):
        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed)
        print "Fuel " + str(self.fuel)
        print "Mileage " + str(self.mileage)

    def tax(self):
        if self.price >= 10000:
            print "Tax: " + str(0.15)
        else:
            print "Tax: " + str(0.12)



car1 = car(2000, "35mph", "Full", "15mpg")
car1.display_all()
car1.tax()

car2 = car(12000, "50mph", "Not Full", "20mpg")
car2.display_all()
car2.tax()

car3 = car(5020, "145mph", "Empty", "60mpg")
car3.display_all()
car3.tax()

car4 = car(1500, "20mph", "Full", "14mpg")
car4.display_all()
car4.tax()

car5 = car(10500, "320mph", "Full", "214mpg")
car5.display_all()
car5.tax()

car6 = car(1900, "10mph", "Full", "148mpg")
car6.display_all()
car6.tax()
