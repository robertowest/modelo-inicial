from django.db import models

from core.audit.models import Auditable


class Diccionario(Auditable):
    TABLA = (
        ('comunicacion', 'Comunicaciones'),
        ('tipo_domicilio', 'Tipo de Domicilio'),
        ('tipo_calle', 'Tipo de Calle'),
        ('tipo_documento', 'Tipo de Documento'),
    )

    texto = models.CharField(max_length=150)
    codigo = models.CharField(max_length=5, null=True, blank=True, unique=True)
    tabla = models.CharField(max_length=45, choices=TABLA, default='comunicacion')

    class Meta:
        db_table = 'diccionario'
        verbose_name = 'Diccionario'
        verbose_name_plural = 'Diccionarios'

    def __str__(self):
        # return "%s (%s)" % (self.texto, self.get_tabla_display())
        return self.texto

    def get_texto(self):        
        # return "{0} ({1})".format(self.texto, self.get_tabla_display())
        return str(self.texto).capitalize()
