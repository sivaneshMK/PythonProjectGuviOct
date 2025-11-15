from restaurant_odering.items import Biriyani, Chicken65, MuttonCola, Drink
from restaurant_odering.order_management import Order
from restaurant_odering.payment import CardPayment

biriyani = Biriyani("Biriyani", 250, "Dum")
chicken65 = Chicken65("Chicken65", 150, "Bone less")
muttoncola = MuttonCola("Mutton Cola ball", 200, "Big Ball")
drink = Drink("Lemon Soda", 80, "Sweet")

order = Order()
order.add_item(biriyani)
order.add_item(chicken65)
order.add_item(muttoncola)
order.add_item(drink)

total_amount = order.show_bill()

payment_method = CardPayment()
payment_method.make_payment(total_amount)