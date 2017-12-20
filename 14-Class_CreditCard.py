# Code to demonstrate credit card functionality
class creditCard:
    """ A consumer credit card."""
    def __init__(self, customer, bank, acnt, limit):
        
        """Create a new credit card instance.
           The initial balance is zero.

           custmer name (John, ali etc)
           bank name of bank (SBI, ICICI, HDFC etc)
           account number (12345678911)
           credit limit ($1000)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    
    def get_customer(self):
        """Return name of customer """
        return self._customer

    def get_bank(self):
        """Return bank account """
        return self._bank

    def get_account(self):
        """Return account number """
        return self._account

    def get_limit(self):
        """Return crdit limit"""
        return self._limit

    def charge(self, price):
        """charge given price to credit card assuming
           sufficient balance. True is charge is proceed
           else denied using false 
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_Payment(self, amount):
        """Deduct amount from credit"""
        self._balance -= amount
cc = creditCard( 'John Doe', '1st Bank' , '5391 0375 9387 5309' , 1000)
