from restaurant_odering.items import Biriyani, Chicken65, MuttonCola, Drink
from restaurant_odering.payment import CardPayment


class Order:
    TAX_RATE = 0.05
    def __init__(self):
        self.items=[]

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        sub_total = sum(item.get_price() for item in self.items)
        tax = sub_total*self.TAX_RATE
        return sub_total+tax

    def show_bill(self):
        print("-------------Bill---------------------------")
        for item in self.items:
            print(item.get_item_details())
        total = self.calculate_total()
        print(f"Total (incl. GST): ${round(total, 2)}")
        return total

