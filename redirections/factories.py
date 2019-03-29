from .models import Redirection


class RedirectionFactory(object):

    @staticmethod
    def get_with_fallback(host, path):
        """
        Look for a pair (host, path), and if it's not found, it will return `default` value.
        If at the end it doesn't have a `default` value, a DoesNotExist exception will be raised.
        """
        try:
            return Redirection.objects.get(host=host, path=path)
        except Redirection.DoesNotExist:
            return Redirection.objects.get(host=host, path=Redirection.DEFAULT_KEY)
