from django.urls import path
from .views import provinciaViews as views

# en template: request.resolver_match.app_name
app_name = "provincia"  # __package__.split('.')[1]

urlpatterns = [
    path('', views.ProvinciaTemplateView.as_view(), name='index'),
    path('listado/', views.ProvinciaListView.as_view(), name='list'),
    path('crear/', views.ProvinciaCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ProvinciaDetailView.as_view(), name='detail'),
    path('<int:pk>/modificar/', views.ProvinciaUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.ProvinciaDeleteView.as_view(), name='delete'),
]
