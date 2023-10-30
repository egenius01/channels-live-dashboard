from django.urls import path
from .views import main, dashboard, chart_data_view

app_name = "stats"
urlpatterns = [
    path("", main, name="main"),
    path("<slug>", dashboard, name="dashboard"),
    path("<slug>/chart", chart_data_view, name="chart"),
]
