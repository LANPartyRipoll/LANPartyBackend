from django.conf.urls import url
from LANPartyBackend import views

urlpatterns = [
    url(r'^inscripcions/$', views.inscripcio_list),
    url(r'^inscripcions/(?P<pk>[0-9]+)/$', views.inscripcio_detail),
    url(r'^tiquets/$', views.tiquets_list),
    url(r'^tiquets/(?P<qr_id>.+)/$', views.tiquet_by_qr.as_view()),
]