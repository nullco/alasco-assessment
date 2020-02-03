import json
import tornado.web
from tornado.web import HTTPError

class BaseResourceHandler(tornado.web.RequestHandler):
    
    def prepare(self):
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            try:
                self.json_args = json.loads(self.request.body)
            except:
                raise HTTPError(400, 'Invalid JSON')
        else:
            self.json_args = {}


    def write_error(self, status_code, exc_info=None):
        message = None
        _, error, _ = exc_info
        try:
            raise error
        except HTTPError as e:
            message = e.log_message
        except Exception:
            message = str(e)
        finally:
            self.set_status(status_code)
            self.write({
                'code': status_code,
                'message': message
            })