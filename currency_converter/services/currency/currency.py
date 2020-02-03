from services.currency.errors import CurrencyNotSupportedError

CURRENCIES = {
    'EUR': {
        'name': "Euro"
    },
    'USD': {
        'name': "US Dollar"
    },
    'JPY': {
        'name': "Yen"
    }
}

class CurrencyService:
    """ This class provides some services around currencies.

    It controls access to the different supported currencies
    and also provides a conversion method between two currencies.
    """


    def __init__(self, rates_service):
        self.rates_service = rates_service

    async def convert_currency(self, amount, source, target):
        """ Converts amounts among currencies
        
        Converts an amount in a source currency to its respective amount in the
        target currency
        """
        for currency in [source, target]:
            if currency not in CURRENCIES:
                raise CurrencyNotSupportedError(f"The currency {currency} is not supported")
        latest_rate = await self.rates_service.get_latest_rate(source, target)
        return amount * latest_rate

    async def find_all_currencies(self):
        return [ {'_id': k, 'name': v['name']} for k, v in CURRENCIES.items()]