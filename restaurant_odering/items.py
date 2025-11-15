from restaurant_odering.menu_items import MenuItems


class Biriyani(MenuItems):
    def __init__(self, name, price, type):
        super().__init__(name, price)
        self.type = type

    def get_item_details(self):
        return f"{self.type} Biriyani {self.get_price()}"

class Chicken65(MenuItems):
    def __init__(self, name, price, type):
        super().__init__(name, price)
        self.type = type

    def get_item_details(self):
        return f"{self.type} Chicken65 {self.get_price()}"


class MuttonCola(MenuItems):
    def __init__(self, name, price, type):
        super().__init__(name, price)
        self.type = type

    def get_item_details(self):
        return f"{self.type} Mutton Cola {self.get_price()}"


class Drink(MenuItems):
    def __init__(self, name, price, type):
        super().__init__(name, price)
        self.type = type

    def get_item_details(self):
        return f"{self.type} Lemon Soda {self.get_price()}"


