class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """Crate a new credit card instance.
        
        The initial balance is zero.

        customer    the name of the customer (e.g., 'John Do')
        bank        the name of the bank (e.g., 'CBA')
        acnt        the account identifer (e.g., '685431')
        limit       credit limit
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank
    
    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit
    
    def get_balance(self):
        """Reutrn current balance."""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assumoing sufficient credit limit
        
        Return True if charge was processed; False if charge was denied
        """
        if price + self._balance > self._limit: # if charge would exceed limit
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('JD','CS','1234',2500))
    wallet.append(CreditCard('JDe','CS1','567',3500))
    wallet.append(CreditCard('JDeez','CS2','890',5000))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =',wallet[c].get_bank())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)0
            print('New balance =', wallet[c].get_balance())
        print()
