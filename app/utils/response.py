import uuid
from datetime import datetime
import os


class Response(object):
    APP_NAME = os.getenv("INSTANCE_NAME")

    def __init__(self, status, description, message, transaction=None):
        self.status = status
        self.description = description
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.transaction = str(uuid.uuid4()) if not transaction else transaction
        self.app_name = self.APP_NAME
        self.message = message


class Success(Response):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def serialize(self):
        return {
            'timestamp': self.timestamp,
            'status': self.status,
            'description': self.description,
            'transaction': self.transaction,
            'exception': None,
            'app_name': self.app_name,
            'data': self.message
        }


class Error(Response):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def serialize(self):
        return {
            'timestamp': self.timestamp,
            'status': self.status,
            'description': self.description,
            'transaction': self.transaction,
            'exception': self.message,
            'app_name': self.app_name,
            'data': None
        }


class PageNotFound(Error):
    def __init__(self):
        context = {}
        context["status"] = 404
        context["description"] = "Not found Error"
        context["message"] = {
            "status": 404,
            "message": "Url not found"
        }
        super().__init__(**context)


class MethodNotAllowed(Error):
    def __init__(self):
        context = {}
        context["status"] = 405
        context["description"] = "Method Not Allowed"
        context["message"] = {
            "status": 405,
            "message": "Method Not Allowed"
        }
        super().__init__(**context)


class UnknownError(Error):
    def __init__(self):
        context = {}
        context["status"] = 500
        context["description"] = "Unknown Error"
        context["message"] = {
            "status": 500,
            "message": "Unknown Error"

        }
        super().__init__(**context)

