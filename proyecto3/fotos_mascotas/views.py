from django.views.generic import (
    TemplateView, View, FormView
)
from django.http import JsonResponse
from .forms import (
    UploadFotoForm
)


class FormularioFotoView(FormView):
    template_name = 'mascotas/subir_fotos.html'
    form_class = UploadFotoForm

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_anonymous():
            return super(FormularioFotoView, self).dispatch(
                request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(FormularioFotoView, self).get_context_data(**kwargs)
        # context['foto_ubicacion'] = self._compliance.dni_photo_location
        return context


class UploadFotoView(View):
    group_required = u'clients'
    raise_exception = True
    redirect_unauthenticated_users = True

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_anonymous():
            return super(UploadFotoView, self).dispatch(
                request, *args, **kwargs)

        return super(UploadFotoView, self).dispatch(
            request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = UploadFotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            response = JsonResponse(
                {
                    'status': 'OK',
                    'message': 'Archivo subido correctamente.'
                }
            )
        else:
            response = JsonResponse(form.errors)

        return response
