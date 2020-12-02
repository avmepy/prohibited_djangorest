from rest_framework.test import APIClient, APITestCase

# testing api requests


class RequestTest(APITestCase):
    """ testing Request(model) requests """

    def test_request_post(self):
        """
        checking post (create) request from non-auth user
        :return: None
        """
        client = APIClient()  # creating client
        request_data = {'client_email': 'test@mail.com',
                        'credential_type': 2,
                        'credential': 'apple.com',
                        'description': 'I like pears more',
                        }

        url = '/api/forbidden/request/create/'
        request = client.post(url, request_data, format='json')
        self.assertEqual(request.status_code, 201)  # expecting status 201 - created

    def test_request_post_invalid_email(self):
        """
        checking post (create) request from non-auth user with invalid mail
        :return: None
        """
        client = APIClient()  # creating client
        request_data = {'client_email': 'invalid email',  # invalid format email
                        'credential_type': 2,
                        'credential': 'apple.com',
                        'description': 'I like pears more',
                        }
        url = '/api/forbidden/request/create/'
        request = client.post(url, request_data, format='json')
        self.assertEqual(request.status_code, 400)  # expecting status 400 - bad request

    def test_request_all_non_auth(self):
        """
        testing access to list of requests from non-auth user
        :return: None
        """
        client = APIClient()
        url = '/api/forbidden/request/all/'
        request = client.get(url)
        self.assertEqual(request.status_code, 403)  # expecting status 403 - forbidden

    def test_request_detail_non_auth(self):
        """
        testing access to detail of requests from non-auth user
        :return: None
        """
        client = APIClient()
        url = '/api/forbidden/request/detail/1/'
        request = client.get(url)
        self.assertEqual(request.status_code, 403)  # expecting status 403 - forbidden


class ProhibitedTest(APITestCase):
    """ prohibited (model) requests testing """

    #  testing access from non-auth user, expecting 403 - forbidden

    def test_prohibited_create_non_auth(self):
        client = APIClient()
        url = '/api/forbidden/prohibited/create/'
        request = client.get(url)
        self.assertEqual(request.status_code, 403)

    def test_prohibited_all_non_auth(self):
        client = APIClient()
        url = '/api/forbidden/prohibited/all/'
        request = client.get(url)
        self.assertEqual(request.status_code, 403)

    def test_prohibited_detail_non_auth(self):
        client = APIClient()
        url = '/api/forbidden/prohibited/detail/1/'
        request = client.get(url)
        self.assertEqual(request.status_code, 403)
