from tornado.testing import AsyncTestCase, gen_test
from services.currency import CurrencyService

class FakeRatesService:

    async def get_latest_rate(self, currency, target):
        return 1.0

class TestCurrencyService(AsyncTestCase):

    def setUp(self):
        super(TestCurrencyService, self).setUp()
        self.service = CurrencyService(FakeRatesService())

    @gen_test
    def test_convert_currency(self):
        amount = yield self.service.convert_currency(5, 'EUR', 'USD')
        self.assertEqual(amount, 5)
        