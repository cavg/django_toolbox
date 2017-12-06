from django.conf import settings
import sys, traceback
import errbit_reporter as errbit

class ErrbitExceptionHandler(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        config = errbit.Configuration(
            api_key=settings.ERRBIT_API_KEY,
            errbit_url=settings.ERRBIT_URL,
            environment_name=settings.ERRBIT_ENVIRONMENT
        )
        client = errbit.Client(config)

        params = None
        if request.method == 'GET':
            params = dict(request.GET)
        else:
            params = dict(request.POST)


        client.notify(exc_info=None, request_url=request.get_raw_uri(), component=None,
               action=str(request.method), params=params, session=request.session, cgi_data={}, timeout=None)

        return None




