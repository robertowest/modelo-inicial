"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('core.authentication.urls')),

    path('',             include('apps.home.urls')),
    path('diccionario/', include('apps.diccionario.urls')),
    path('persona/',     include('apps.persona.urls')),
    path('domicilio/',   include('apps.domicilio.urls.domicilioUrls')),
]


from django.contrib.auth.views import LogoutView
from core.authentication.views import login_view, register_user, login_redirect

urlpatterns += [
    path('login/',    login_view,           name='login'),
    path('register/', register_user,        name='register'),
    path('logout/',   LogoutView.as_view(), name='logout'),
    path('redirect/', login_redirect,       name='redirect'),
]


from django.conf import settings
if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns += [
            path('__debug__/', include(debug_toolbar.urls))
        ]

    # urlpatterns += [
    #     path("ui/", include("core.UI.urls")),
    # ]

    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
