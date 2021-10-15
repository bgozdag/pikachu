from django.urls import path
from .views import index, baristas, history, createbarista, createrecord, barista

urlpatterns = [
    path('', index, name="index"),
    path('baristas', baristas, name="baristas"),
    path('history', history, name="history"),
    path('baristas/create', createbarista, name="createbarista"),
    path('createrecord', createrecord, name="createrecord"),
    path('baristas/<slug:barista_name>', barista, name="barista")
]
