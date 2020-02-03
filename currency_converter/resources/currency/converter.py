from resources.base import BaseResourceHandler

class CurrencyConverterResourceHandler(BaseResourceHandler):

    def initialize(self, service):
        self.service = service

    async def post(self, currency, target):
        amount = self.json_args.get('amount', 1)
        value = await self.service.convert_currency(amount, currency, target)
        self.write({
            'amount': value
        })
        