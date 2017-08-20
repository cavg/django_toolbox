from django.conf import settings
import sys, traceback
import errbit_reporter as errbit

class ErrbitExceptionHandler(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):

        config = errbit.Configuration(
            api_key=settings.ERRBIT_API_KEY,
            errbit_url=settings.ERRBIT_URL,
            environment_name=settings.ERRBIT_ENVIRONMENT
        )

        client = errbit.Client(config)

        _type, _value, _traceback = sys.exc_info()
        backtrace = traceback.extract_tb(_traceback)

        notice = errbit.Notice(config, _type.__name__, str(_value), backtrace)

        client.send_notice(notice)

        return None



