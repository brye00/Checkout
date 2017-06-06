class Cart(object):
    chai_price = 3.11
    apple_price = 6.00
    coffee_price = 11.23
    milk_price = 4.75
    oatmeal_price = 3.69

    def __init__(self):
        self.contents = []
        self.total = 0.0
        self.num_apples = 0
        self.num_chai = 0
        self.num_coffee = 0
        self.num_milk = 0
        self.num_oatmeal = 0

    def add_item(self, item):
        if item == "CH1":
            self.num_chai += 1
            self.contents.append(item)
        elif item == "AP1":
            self.num_apples += 1
            self.contents.append(item)
        elif item == "CF1":
            self.num_coffee += 1
            self.contents.append(item)
        elif item == "MK1":
            self.num_milk += 1
            self.contents.append(item)
        elif item == "OM1":
            self.num_oatmeal += 1
            self.contents.append(item)

    def print_receipt(self):
        self.total = 0.0
        discount_apples = self.num_oatmeal #APOM
        free_milk = (self.num_chai >= 1) #CHMK
        free_coffee = int(self.num_coffee / 2) #BOGO

        print("{0}{1:>19}".format("item", "price"))
        print("{0}{1:>19}".format("----", "-----"))

        for item in self.contents:
            if item == "CH1":
                self.total += Cart.chai_price
                print("{0}{1:>20.2f}".format(item, Cart.chai_price))
            elif item == "AP1":
                self.total += Cart.apple_price
                print("{0}{1:>20.2f}".format(item, Cart.apple_price))
                if self.num_apples >= 3:
                    self.total -= 1.50
                    print("{0:>10}{1:>13.2f}".format("APPL", -1.50))
                if discount_apples > 0:
                    self.total -= Cart.apple_price * .5
                    print("{0:>10}{1:>13.2f}".format("APOM", -Cart.apple_price * .5))
                    discount_apples -= 1
            elif item == "CF1":
                self.total += Cart.coffee_price
                print("{0}{1:>20.2f}".format(item, Cart.coffee_price))
                if free_coffee > 0:
                    self.total -= Cart.coffee_price
                    free_coffee -= 1
                    print("{0:>10}{1:>13.2f}".format("BOGO", -Cart.coffee_price))
            elif item == "MK1":
                self.total += Cart.milk_price
                print("{0}{1:>20.2f}".format(item, Cart.milk_price))
                if free_milk:
                    self.total -= Cart.milk_price
                    free_milk = False
                    print("{0:>10}{1:>13.2f}".format("CHMK", -Cart.milk_price))
            elif item == "OM1":
                self.total += Cart.oatmeal_price
                print("{0}{1:>20.2f}".format(item, Cart.oatmeal_price))

        self.total = round(self.total, 2)
        print("-----------------------")
        print("{0:>23.2f}\n".format(self.total))


def main():
    my_cart = Cart()
    while True:
        item = input("Please input an item (CH1, AP1, CF1, MK1, OM1), print, or checkout\n")
        if item == "checkout":
            my_cart.print_receipt()
            print("Thank you for shopping!")
            break
        elif item == "print":
            my_cart.print_receipt()
        elif item in "CH1, AP1, CF1, MK1, OM1":
            my_cart.add_item(item)
        else:
            print("Please input a valid item (CH1, AP1, CF1, MK1, OM1), print, or checkout\n")

if __name__ == '__main__':
    main()
