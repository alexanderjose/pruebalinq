from django import forms


class UploadFotoForm(forms.Form):
    nickname = forms.CharField(
        max_length=100,
        label='Nickname',
        error_messages={
            'required': 'Debe indicar su Nickname'
        }
    )
    nombre_mascota = forms.CharField(
        max_length=50,
        label='Nombre de la Mascota',
        error_messages={
            'required': 'Debe indicar el nombre de la mascota'
        }
    )
    foto_mascota = forms.ImageField(
        error_messages={
            'invalid': 'Error al subir la foto'
        }
    )
