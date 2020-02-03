from services.errors import ServiceError

class CurrencyServiceError(ServiceError):
    pass

class CurrencyNotSupportedError(CurrencyServiceError):
    pass

class InvalidRateEntryError(CurrencyServiceError):
    pass