from resources.base import BaseResourceHandler

class CurrencyResourceHandler(BaseResourceHandler):

    def initialize(self, service):
        self.service = service

    async def get(self):
        currencies = await self.service.find_all_currencies()
        self.write({
            'results': currencies
        })