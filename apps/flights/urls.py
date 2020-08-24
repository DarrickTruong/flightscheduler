from django.conf.urls import url, include
from . import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    # url(r'^$', views.index),
    # url(r'', include(router.urls))

    url(r'^$', views.flight_list),
    url(r'^(?P<primary_key>[0-9]+)$', views.flight_detail)

]
