from django.conf.urls import url
from LANPartyBackend import views

urlpatterns = [
    url(r'^inscripcions/(?P<qr>.+)/$', views.inscripcio_detail),
]