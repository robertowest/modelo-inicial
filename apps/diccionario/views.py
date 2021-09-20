from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from core.audit.views import AuditableMixin
from core.common.utils import PagedFilteredTableView

from .models import Diccionario
from .tables import DiccionarioTable
from .filters import DiccionarioFilter, DiccionarioFilterForm
from .forms import DiccionarioForm


class DiccionarioTemplateView(generic.TemplateView):
    """
    TemplateView se utiliza para la página de presentación del módulo.
    Si no existe página de presentación, se llamará a la función ListView
    """
    def get(self, request, *args, **kwargs):
        return DiccionarioListView.as_view()(request)


class DiccionarioListView(PagedFilteredTableView):
    """ListView se utiliza para la presentación de una tabla de contenido"""
    model = Diccionario
    table_class = DiccionarioTable
    filter_class = DiccionarioFilter
    formhelper_class = DiccionarioFilterForm
    template_name = 'comunes/tabla.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            from django.contrib.auth.models import Permission
            from django.contrib.contenttypes.models import ContentType
            content_type = ContentType.objects.get_for_model(Diccionario)
            # add, change, delete, view & custom
            if Permission.objects.get(codename="add_diccionario", content_type=content_type):
                context["add_permission"] = True
        return context


class DiccionarioDetailView(PermissionRequiredMixin, generic.DetailView):
    """DetailView se utiliza para la presentación de un registro de la tabla"""
    permission_required = '{domain}/view_{app}'.format(domain='diccionario', app='diccionario')
    model = Diccionario
    # template_name = '{app}/detalle.html'.format(app=model._meta.verbose_name.lower())
    template_name = 'comunes/detalle.html'


class DiccionarioCreateView(AuditableMixin, PermissionRequiredMixin, generic.CreateView):
    """CreateView formulario para la creación de un registro en la tabla"""
    model = Diccionario
    permission_required = '{domain}/add_{app}'.format(domain='diccionario', app='diccionario')
    form_class = DiccionarioForm
    template_name = 'comunes/formulario.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class DiccionarioUpdateView(AuditableMixin, PermissionRequiredMixin, generic.UpdateView):
    """UpdateView formulario para la modificación de un registro en la tabla"""
    model = Diccionario
    permission_required = '{domain}/change_{app}'.format(domain='diccionario', app='diccionario')
    form_class = DiccionarioForm
    template_name = 'comunes/formulario.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class DiccionarioDeleteView(PermissionRequiredMixin, generic.DeleteView):
    """DeleteView confirmación de eliminación de un registro en la tabla"""
    model = Diccionario
    permission_required = '{domain}/del_{app}'.format(domain='diccionario', app='diccionario')
    success_message = "Registro eliminado correctamente"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        redirect = self.request.GET.get('next')
        if redirect:
            return redirect
        #reverse_lazy('diccionario:detail', args=(self.object.pk,))
        return reverse_lazy('diccionario:list')
