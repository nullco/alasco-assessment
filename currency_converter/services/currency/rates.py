from tornado.httpclient import AsyncHTTPClient
from tornado.escape import json_decode
from services.currency.errors import InvalidRateEntryError, CurrencyServiceError

API_ENDPOINT = "https://api.exchangeratesapi.io/latest?base={currency}&symbols={target}"

class CurrencyRatesService:
    """ Offers information about rates across different currencies
    """

    async def get_latest_rate(self, currency, target):
        """ Gets the last information from rates between two currencies
        """
        client = AsyncHTTPClient()
        endpoint = API_ENDPOINT.format(currency=currency, target=target)
        response = await client.fetch(endpoint)
        if response.code == 200:
            json_response = json_decode(response.body)
            return json_response['rates'][target]
        if response.body:
            json_response = json_decode(response.body)
            if response.code == 200:
                return json_response['rates'][target]
            elif response.code == 400:
                raise InvalidRateEntryError(json_response['error'])
            else:
                raise CurrencyServiceError(json_response['error'])
        else:
            raise CurrencyServiceError("Unkown error when calling the external rates API")

        
