from rest_framework import serializers
from forbidden.models import Prohibited, Request


def _get_client_ip(request):
    """
    returned non-auth client ip from request
    :param request: request
    :return: client ip
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class ProhibitedDetailSerializer(serializers.ModelSerializer):

    """
    serializer for create, read and edit prohibited item
    """

    class Meta:
        model = Prohibited
        fields = '__all__'


class RequestCreateSerializer(serializers.ModelSerializer):

    """ serializer for creating request"""

    class Meta:
        model = Request
        exclude = ('client_ip', 'status')  # filling automatically

    def create(self, validated_data):
        """
        creating a new request
        :param validated_data: serializer data
        :return: new Request object
        """
        client_ip = _get_client_ip(self.context['request'])  # getting client ip
        status = 3  # verifying

        new_request = Request(client_ip=client_ip, status=status, **validated_data)  # creating
        new_request.save()  # saving
        return new_request


class RequestDetailSerializer(serializers.ModelSerializer):

    """ serializer for edit requests """

    class Meta:
        #  there is only status field editable
        model = Request
        fields = '__all__'
        read_only_fields = ('credential_type', 'client_ip', 'client_email', 'credential', 'description')


class RequestListSerializer(serializers.ModelSerializer):

    """ serializer for list request representation"""

    class Meta:
        model = Request
        fields = ('id',  'client_ip', 'client_email', 'credential', 'status')
