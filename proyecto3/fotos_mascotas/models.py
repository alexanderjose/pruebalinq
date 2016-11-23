from __future__ import unicode_literals
import uuid
# from django.utils.encoding import python_2_unicode_compatible

from django.db import models


def directorio_fotos(instance, filename):
    # file will be uploaded to MEDIA_ROOT/application_<id>/<filename>
    return 'mascota_{0}/{1}'.format(str(instance.id), filename)


# @python_2_unicode_compatible
class FotoMascota(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    nickname = models.CharField(max_length=100)
    nombre_mascota = models.CharField(max_length=50)
    foto_ubicacion = models.FileField(
        upload_to=directorio_fotos,
        null=True
    )
    fecha_subida = models.DateTimeField(null=True)
    status = models.BooleanField(default=True)
