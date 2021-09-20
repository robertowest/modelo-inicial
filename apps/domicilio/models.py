from django.db import models

from core.audit.models import Auditable
from apps.diccionario.models import Diccionario


class Domicilio(Auditable):
    TIPO = (('avda', 'Avenida'), ('barrio', 'Barrio'), ('calle', 'Calle'),
            ('pje', 'Pasaje'), ('ruta', 'Ruta'))

    tipo = models.ForeignKey(Diccionario, on_delete=models.CASCADE,
                             null=True, blank=True, default=1,
                             limit_choices_to={'tabla': 'domicilio', 'active': True})
    tipo_calle = models.CharField(max_length=6, choices=TIPO, default='calle')
    nombre = models.CharField(max_length=80, null=True, blank=True)
    numero = models.IntegerField('Número', null=True, blank=True)
    piso = models.CharField(max_length=2, null=True, blank=True)
    puerta = models.CharField(max_length=2, null=True, blank=True)
    barrio = models.CharField(max_length=40, null=True, blank=True)
    # pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    # provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE,
    #                               null=True, blank=True,
    #                               limit_choices_to={'active': True})
    # departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE,
    #                                  null=True, blank=True,
    #                                  limit_choices_to={'active': True})
    # localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE,
    #                               null=True, blank=True,
    #                               limit_choices_to={'active': True})
    provincia_texto = models.CharField(max_length=50, null=True, blank=True)
    departamento_texto = models.CharField(max_length=50, null=True, blank=True)
    localidad_texto = models.CharField(max_length=50, null=True, blank=True)
    observacion_texto = models.TextField('Nota', null=True, blank=True)

    # configuración para admin
    date_hierarchy = ''
    exclude = []
    list_display = ['id', 'tipo', 'nombre', 'numero', 'piso', 'puerta', 'active']
    list_display_links = ['id']
    list_filter = ['provincia']
    ordering = ['tipo', 'nombre', 'numero']
    search_fields = ['nombre']

    class Meta:
        db_table = 'domicilio'
        verbose_name = 'Domicilio'
        verbose_name_plural = 'Domicilios'

    def __str__(self):
        texto = self.nombre
        if self.numero:
            texto += " " + str(self.numero)
        if self.piso:
            texto += " - %s piso, puerta %s" % (self.piso, self.puerta)
        return texto
