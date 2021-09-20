from django.urls import path
from .views import paisViews as views

# en template: request.resolver_match.app_name
app_name = "pais"  # __package__.split('.')[1]

urlpatterns = [
    path('', views.PaisTemplateView.as_view(), name='index'),
    path('listado/', views.PaisListView.as_view(), name='list'),
    path('crear/', views.PaisCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PaisDetailView.as_view(), name='detail'),
    path('<int:pk>/modificar/', views.PaisUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.PaisDeleteView.as_view(), name='delete'),
]
