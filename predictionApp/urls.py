from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('titanic-survival-predictions/', include('TitanicSurvivalPrediction.urls'))
]