from django.conf.urls import url
from . import views as mascotas_views

urlpatterns = [

    # url(r'^listado$',
    #     mascotas_views.ListadoMascotasView.as_view(),
    #     name='listado_mascotas'),
    url(r'^nueva_mascota$',
        mascotas_views.FormularioFotoView.as_view(),
        name='crear_nueva_mascota'),
    url(r'^nueva_mascota/upload$',
        mascotas_views.UploadFotoView.as_view(),
        name='upload_nueva_mascota'),

]
