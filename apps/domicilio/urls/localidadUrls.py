from django.urls import path
from .views import localidadViews as views

# en template: request.resolver_match.app_name
app_name = "localidad"  # __package__.split('.')[1]

urlpatterns = [
    path('', views.LocalidadTemplateView.as_view(), name='index'),
    path('listado/', views.LocalidadListView.as_view(), name='list'),
    path('crear/', views.LocalidadCreateView.as_view(), name='create'),
    path('<int:pk>/', views.LocalidadDetailView.as_view(), name='detail'),
    path('<int:pk>/modificar/', views.LocalidadUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.LocalidadDeleteView.as_view(), name='delete'),
]
