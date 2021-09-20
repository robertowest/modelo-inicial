from django.urls import path, re_path
from . import views

app_name = "UI"

urlpatterns = [

    # The home page
    path('', views.index, name='ui_home'),
    # path('charts/', views.charts, name='ui_charts'),
    # path('tables/', views.tables, name='ui_tables'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]
