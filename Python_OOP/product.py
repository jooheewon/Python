class product(object):
    def __init__(self, price, item_name, weight, brand, cost, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"

    def sell(self):
        self.status = "sold"

        return self

    def tax(self):
        print "Tax: " + str(0.15)

    def Return(self, reason):
        self.reason = reason
        if self.reason == "defective":
            self.price = 0
        elif self.reason == "opened":
            self.price = self.price - (self.price * 0.20)
        else:
            self.status = "for sale"

    def display_info(self):
        print "Price: " + str(self.price)
        print "Item Name: " + str(self.item_name)
        print "Weight: " + str(self.weight)
        print "Brand: " + str(self.brand)
        print "Cost: " + str(self.cost)
        print "Status: " + str(self.status)


product1 = product(50, "Lego", "5lbs", "Lego", 25, "for sale")
product1.sell()
product1.tax()
product1.Return("defective")
product1.display_info()
