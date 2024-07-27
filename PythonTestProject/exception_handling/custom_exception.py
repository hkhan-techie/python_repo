class CurrencyDoNotMatchException(Exception):
    def __init__(self, message):
        super().__init__(message)
        # print(message)


class Amount:

    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        return repr((self.currency, self.amount))

    def add(self, that):
        if self.currency == that.currency:
            self.amount += that.amount
        else:
            raise CurrencyDoNotMatchException(self.currency + ' ' + that.currency)


amount1 = Amount('INR', 100)
amount2 = Amount('EUR', 50)
try:
    amount2.add(amount1)
except CurrencyDoNotMatchException as error:
    print(f'exception : {error}')
finally:
    print(f' finally {amount2}')
