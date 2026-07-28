import datetime
from django.utils.deprecation import MiddlewareMixin

class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("Request received at:", datetime.datetime.now())
        return None
    
    def process_response(self, request, response):
        print("Response sent at:", datetime.datetime.now())
        return response
