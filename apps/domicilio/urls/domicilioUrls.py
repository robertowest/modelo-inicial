from django.urls import path
from apps.domicilio.views import domicilioViews as views

# en template: request.resolver_match.app_name
app_name = "domicilio"  # __package__.split('.')[1]

urlpatterns = [
    path('', views.DomicilioTemplateView.as_view(), name='index'),
    path('listado/', views.DomicilioListView.as_view(), name='list'),
    path('crear/', views.DomicilioCreateView.as_view(), name='create'),
    path('<int:pk>/', views.DomicilioDetailView.as_view(), name='detail'),
    path('<int:pk>/modificar/', views.DomicilioUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.DomicilioDeleteView.as_view(), name='delete'),
]
