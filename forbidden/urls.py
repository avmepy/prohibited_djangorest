from django.urls import path
from forbidden.views import ProhibitedCreateView, ProhibitedListView, RequestCreateView, RequestListView, \
    ProhibitedDetailView, RequestDetailView

app_name = 'forbidden'

urlpatterns = [
    path('prohibited/create/', ProhibitedCreateView.as_view()),
    path('prohibited/all/', ProhibitedListView.as_view()),
    path('prohibited/detail/<int:pk>/', ProhibitedDetailView.as_view()),
    path('request/create/', RequestCreateView.as_view()),
    path('request/all/', RequestListView.as_view()),
    path('request/detail/<int:pk>/', RequestDetailView.as_view()),
]
