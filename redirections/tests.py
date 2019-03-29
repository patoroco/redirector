from django.test import TestCase
from django.urls import reverse

from .models import Redirection


class RedirectionViewTests(TestCase):
    def response_gen(self, host, path):
        return self.client.get(
            reverse('redirect', args=(path,)),
            HTTP_HOST=host
        )

    def setUp(self):
        Redirection(
            host='myhost.test',
            path='mypath',
            redirection='http://myredirection.test/index.html?abcd'
        ).save()

    def test_redirect_for_existent_domain_and_path(self):
        existent = self.response_gen('myhost.test', 'mypath')
        self.assertRedirects(
            existent, 'http://myredirection.test/index.html?abcd', status_code=301)

    def test_404_for_not_existent_domain_or_path(self):
        bad_domain = self.response_gen('notexistentdomain.test', 'whatever')
        self.assertEqual(bad_domain.status_code, 404)

        bad_path = self.response_gen('myhost.test', 'not_existent')
        self.assertEqual(bad_path.status_code, 404)

    def test_redirect_for_default_path(self):
        """
        If user tries to access to a not existent path, but the domain has a default redirect,
        he will be redirected to that `default` place.
        """
        Redirection(
            host='myhost.test',
            path=Redirection.DEFAULT_KEY,
            redirection='http://this_is_the_default_site.test'
        ).save()

        not_existent = self.response_gen('myhost.test', 'not_existent')
        self.assertRedirects(
            not_existent, 'http://this_is_the_default_site.test', status_code=301, fetch_redirect_response=False)

        #         self.assertRedirects(
        # not_existent, 'http://this_is_the_default_site.test', status_code=301, fetch_redirect_response=False)
