class LRUCache(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, size):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.size = size
        self.cache = {}

    def set(self, key, value):
        if len(self.cache) == self.size:
            remove_key = None
            for key, val in self.cache.items():
                val['order'] = val['order'] - 1
                if val['order'] < 0:
                    remove_key = key

            self.cache.pop(remove_key)

        self.cache[key] = {
            'value': value,
            'order': len(self.cache)
        }

    def get(self, key):
        order = self.cache.get(key)['order']

        for key, val in self.cache.items():
            if val['order'] > order:
                val['order'] = val['order'] - 1

        self.cache.get(key)['order'] = len(self.cache) - 1


























    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance
