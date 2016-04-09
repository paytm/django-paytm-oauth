from django.conf.urls import url

from .views import paytm_oauth

urlpatterns = [

    url(r'^callback', paytm_oauth),

]