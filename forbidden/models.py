from django.db import models

# Create your models here.

_CREDENTIAL_TYPES = ((1, 'ip'), (2, 'domain'))  # possible types for credential ip/domain
_STATUS_TYPES = ((1, 'confirmed'), (2, 'rejected'), (3, 'verifying'))  # possible statuses for requests


class Prohibited(models.Model):

    """
    Prohibited model implementation
    """

    credential_type = models.IntegerField(verbose_name="ip/domain", choices=_CREDENTIAL_TYPES)
    credential = models.CharField(max_length=200, unique=True, blank=False, verbose_name="ip or domain")

    #  for representation
    def __str__(self):
        return self.credential

    def __repr__(self):
        return self.credential


class Request(models.Model):

    """
    Request model implementation
    """

    client_ip = models.CharField(max_length=100, verbose_name="client ip", blank=True)
    client_email = models.EmailField(max_length=100, verbose_name="client email")
    credential_type = models.IntegerField(verbose_name="ip/domain", choices=_CREDENTIAL_TYPES)
    credential = models.CharField(max_length=200, blank=False, verbose_name="ip or domain")
    description = models.TextField(verbose_name="description")
    status = models.IntegerField(verbose_name='status', choices=_STATUS_TYPES)

    #  for representation

    def __str__(self):
        return f"request {self.credential} from client {self.client_ip}, {self.client_email}"

    def __repr__(self):
        return f"request {self.credential} from client {self.client_ip}, {self.client_email}"
