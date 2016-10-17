from django.conf.urls import url
from apps.logistica.views import \
    IncidenteCreate, IncidenteList, IncidenteUpdate, IncidenteDelete, \
    TipoIncidenteCreate, TipoIncidenteList, TipoIncidenteUpdate, TipoIncidenteDelete, \
    AsignacionIncidenteCreate

urlpatterns = [

    url(r'^incidente/$', IncidenteList.as_view(), name='incidente'),
    url(r'^incidente/nuevo/$', IncidenteCreate.as_view(), name='incidente_crear'),
    url(r'^incidente/editar/(?P<pk>\d+)/$', IncidenteUpdate.as_view(), name='incidente_editar'),
    url(r'^incidente/eliminar/(?P<pk>\d+)/$', IncidenteDelete.as_view(), name='incidente_eliminar'),

    url(r'^tipoincidente/$', TipoIncidenteList.as_view(), name='tipo_incidente'),
    url(r'^tipoincidente/nuevo/$', TipoIncidenteCreate.as_view(), name='tipo_incidente_crear'),
    url(r'^tipoincidente/editar/(?P<pk>\d+)/$', TipoIncidenteUpdate.as_view(), name='tipo_incidente_editar'),
    url(r'^tipoincidente/eliminar/(?P<pk>\d+)/$', TipoIncidenteDelete.as_view(), name='tipo_incidente_eliminar'),

    url(r'^asignacionincidente/nuevo/$', AsignacionIncidenteCreate.as_view(), name='tipo_incidente_crear'),

    ]