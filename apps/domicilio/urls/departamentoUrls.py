from django.urls import path
from .views import departamentoViews as views

# en template: request.resolver_match.app_name
app_name = "departamento"  # __package__.split('.')[1]

urlpatterns = [
    path('', views.DepartamentoTemplateView.as_view(), name='index'),
    path('listado/', views.DepartamentoListView.as_view(), name='list'),
    path('crear/', views.DepartamentoCreateView.as_view(), name='create'),
    path('<int:pk>/', views.DepartamentoDetailView.as_view(), name='detail'),
    path('<int:pk>/modificar/', views.DepartamentoUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.DepartamentoDeleteView.as_view(), name='delete'),
]
