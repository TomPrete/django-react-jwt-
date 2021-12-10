from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import current_user, UserList

urlpatterns = [
    path('current-user/', current_user),
    path('users/', UserList.as_view()),
]
