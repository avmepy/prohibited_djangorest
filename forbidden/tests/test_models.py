from django.test import TestCase
from forbidden.models import Prohibited, Request


# testing models

class ProhibitedModelTest(TestCase):
    """ Prohibited model testing """

    @classmethod
    def setUpTestData(cls):
        """
        creating 2 different objects (different by credential type)
        :return: None
        """
        # Set up non-modified objects used by all test methods
        Prohibited.objects.create(credential_type=2, credential='google.com')
        Prohibited.objects.create(credential_type=1, credential='127.0.0.1')

    def test_credential_type_label(self):
        """
        checking credential type label
        :return: None
        """
        prohibited1 = Prohibited.objects.get(id=1)
        prohibited2 = Prohibited.objects.get(id=2)
        field_label1 = prohibited1._meta.get_field('credential_type').verbose_name
        field_label2 = prohibited2._meta.get_field('credential_type').verbose_name
        self.assertEquals(field_label1, 'ip/domain')
        self.assertEquals(field_label2, 'ip/domain')

    def test_credential_label(self):
        """
        checking credential label
        :return: None
        """
        prohibited1 = Prohibited.objects.get(id=1)
        prohibited2 = Prohibited.objects.get(id=2)
        field_label1 = prohibited1._meta.get_field('credential').verbose_name
        field_label2 = prohibited2._meta.get_field('credential').verbose_name
        self.assertEquals(field_label1, 'ip or domain')
        self.assertEquals(field_label2, 'ip or domain')

    def test_credential_max_length(self):
        """
        checking credential max_length
        :return: None
        """
        prohibited1 = Prohibited.objects.get(id=1)
        prohibited2 = Prohibited.objects.get(id=2)
        max_length1 = prohibited1._meta.get_field('credential').max_length
        max_length2 = prohibited2._meta.get_field('credential').max_length
        self.assertEquals(max_length1, 200)
        self.assertEquals(max_length2, 200)


class RequestModelTest(TestCase):
    """ Request model testing """

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        # creating test request object
        Request.objects.create(client_ip='192.168.0.102',
                               client_email="test@gmail.com",
                               credential_type=1,  # ip
                               credential="127.0.0.1",
                               description=" simple long description " * 100,
                               status=3  # verifying
                               )

    def test_client_ip_label(self):
        """
        checking client ip label
        :return: None
        """
        request = Request.objects.get(id=1)
        field_label = request._meta.get_field('client_ip').verbose_name
        self.assertEquals(field_label, 'client ip')

    def test_client_email_label(self):
        """
        checking client email label
        :return: None
        """
        request = Request.objects.get(id=1)
        field_label = request._meta.get_field('client_email').verbose_name
        self.assertEquals(field_label, 'client email')

    def test_credential_type_label(self):
        """
        checking credential type label
        :return: None
        """
        request = Request.objects.get(id=1)
        field_label = request._meta.get_field('credential_type').verbose_name
        self.assertEquals(field_label, 'ip/domain')

    def test_credential_label(self):
        """
        checking credential label
        :return: None
        """
        request = Request.objects.get(id=1)
        field_label = request._meta.get_field('credential').verbose_name
        self.assertEquals(field_label, 'ip or domain')

    def test_description_label(self):
        """
        checking description label
        :return: None
        """
        request = Request.objects.get(id=1)
        field_label = request._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_client_ip_max_length(self):
        """
        checking client ip max_length
        :return: None
        """
        request = Request.objects.get(id=1)
        max_length = request._meta.get_field('client_ip').max_length
        self.assertEquals(max_length, 100)

    def test_client_email_max_length(self):
        """
        checking client email max_length
        :return: None
        """
        request = Request.objects.get(id=1)
        max_length = request._meta.get_field('client_email').max_length
        self.assertEquals(max_length, 100)

    def test_credential_max_length(self):
        """
        checking credential max_length
        :return: None
        """
        request = Request.objects.get(id=1)
        max_length = request._meta.get_field('credential').max_length
        self.assertEquals(max_length, 200)
