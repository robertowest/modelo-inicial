MODELO PARA LA CREACION DE PROYECTOS 

Framework: Django 3.1

Lo utilizo para no comenzar desde cero cada nuevo proyecto. 

Nota:

```
# ---------------------------------------------------------------------
# registra todos los modelos
# se debe ejecutar al final de todo, por si ya existe alguna definición
# ---------------------------------------------------------------------
from django.apps import apps
from django.contrib import admin

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
```

Nota:

```
    {# cargamos el template del directorio local de la aplicación #}
    {% with appname|add:"/comunes_formulario.html" as template_name %}
        {% if template_name|file_exists %}
            <!-- agregamos funciones personalizadas -->
            {% include template_name %}
        {% endif %}
    {% endwith %}
```

Nota:

```
from django.contrib.auth import authenticate
user = authenticate(username='admin', password='admin')

from apps.persona.models import Persona
p = Persona.objects.get(id=1)

print( p.modified_on, p.modified_by )
p.save()
print( p.modified_on, p.modified_by )
```