import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
from services.currency import CurrencyRatesService
from services.currency import CurrencyService
from resources.currency import CurrencyConverterResourceHandler
from resources.currency import CurrencyResourceHandler
from views.convert import ConvertViewHandler

define("port", default=8888, help="run on the given port", type=int)

def get_resource_handlers():
    rates_service = CurrencyRatesService()
    currency_service = CurrencyService(rates_service)

    return [
        (r"/api/currencies/{0,1}", CurrencyResourceHandler, {
            'service': currency_service
        }),
        (r"/api/currencies/([A-Z]{3})/to/([A-Z]{3})", CurrencyConverterResourceHandler, {
            'service': currency_service
        })
    ]

def get_view_handlers():
    return [
        (r"/{0,1}", ConvertViewHandler)
    ]

def get_settings():
    return dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True,
    )

def main():
    tornado.options.parse_command_line()
    handlers = []
    handlers.extend(get_resource_handlers())
    handlers.extend(get_view_handlers())
    settings = get_settings()
    application = tornado.web.Application(handlers, **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()