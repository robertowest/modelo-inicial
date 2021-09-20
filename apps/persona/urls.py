from django.urls import path
from . import views

app_name = __package__.split('.')[1]    # en template: request.resolver_match.app_name

urlpatterns = [
    path('', views.PersonaTemplateView.as_view(), name='index'),
    path('listado/', views.PersonaListView.as_view(), name='list'),
    path('crear/', views.PersonaCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PersonaDetailView.as_view(), name='detail'),
    path('<int:pk>/modificar/', views.PersonaUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.PersonaDeleteView.as_view(), name='delete'),
]
