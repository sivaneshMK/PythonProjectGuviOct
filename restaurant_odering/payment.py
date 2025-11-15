from abc import ABC, abstractmethod


# abstract
class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class CashPayment(Payment):
    def make_payment(self, amount):
        print(f"Payment of ${amount} received in cash.")

class CardPayment(Payment):
    def make_payment(self, amount):
        print(f"Payment of ${amount} done using cred/debit card.")


