#Example of encapsulation
class Transaction:
    def __init__(self, merchant: str, amount: int, cardNumber: str):
        self.merchant = merchant
        self.amount = amount
        self._cardNumber = cardNumber

    def display_transaction(self) -> None:
        print(f"Merchant: {self.merchant}")
        print(f"Transaction Amount: {self.amount}")
        print(f"Credit Card Number: {self.cardNumber}") #here cardNumber is defined in line 13, from the property decorator

    @property
    def cardNumber(self) -> str:
        masked_cardNumber = "XXXX-XXXX-XXXX-" + self._cardNumber[-4:]
        return masked_cardNumber
    
def main() -> None:
    #Creating an instance of the Transaction class
    transaction1 = Transaction("Home Depot", 421, "1234-5678-9012-3456")

    transaction1.display_transaction()

    print(transaction1._cardNumber)

if __name__ == "__main__":
    main()