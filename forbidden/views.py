from rest_framework import generics
from forbidden.serializers import ProhibitedDetailSerializer, RequestCreateSerializer, RequestListSerializer,\
    RequestDetailSerializer
from forbidden.models import Prohibited, Request
from rest_framework.permissions import IsAdminUser, AllowAny
from django.core.mail import send_mail
from prohibited.settings import EMAIL_HOST


# Create your views here.


class ProhibitedCreateView(generics.CreateAPIView):
    """ adding an item to blocked """
    permission_classes = (IsAdminUser, )  # available to the administrator
    serializer_class = ProhibitedDetailSerializer


class ProhibitedListView(generics.ListAPIView):
    """ blocked item list view"""
    permission_classes = (IsAdminUser, )  # available to the administrator
    serializer_class = ProhibitedDetailSerializer
    queryset = Prohibited.objects.all()


class ProhibitedDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ prohibited item detail and edit view """
    permission_classes = (IsAdminUser, )  # available to the administrator
    serializer_class = ProhibitedDetailSerializer
    queryset = Prohibited.objects.all()


class RequestCreateView(generics.CreateAPIView):
    """ creating request view """
    permission_classes = (AllowAny, )  # available to everyone
    serializer_class = RequestCreateSerializer


class RequestListView(generics.ListAPIView):
    """ request items list view """
    permission_classes = (IsAdminUser, )  # available to the administrator
    serializer_class = RequestListSerializer
    queryset = Request.objects.all()


class RequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ request detail and edit status view """
    permission_classes = (IsAdminUser,)  # available to the administrator
    serializer_class = RequestDetailSerializer
    queryset = Request.objects.all()

    def put(self, request, *args, **kwargs):

        result = super().put(request, *args, **kwargs)  # calling super() put

        # sending the mail

        current: Request = self.get_object()
        send_mail(
            'You received a response to your request',  # mail title
            # mail text
            f'Your {current.get_credential_type_display()} {current.credential} prohibiting request has been '
            f'{current.get_status_display()}',
            EMAIL_HOST,
            [current.client_email, ],
            fail_silently=False  # disable re-sending on failure
        )
        return result  # return the result of the super method
