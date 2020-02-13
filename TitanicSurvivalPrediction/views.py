from django.http import HttpResponse
from django.shortcuts import render
from TitanicSurvivalPrediction.forms import MakePredictions
from .titanic_model.predictive_model import PredictiveModel

predictive_model = PredictiveModel()

def index(request):
    return HttpResponse(render(request, 'TitanicSurvivalPrediction/index.html'))

def make_prediction(request):
    if request.method == 'POST':
        form = MakePredictions(request.POST)
        processed_form_data = process_form_data(form)
        prediction = predictive_model.make_prediction(processed_form_data)
        return render(request, 'TitanicSurvivalPrediction/show_prediction.html', {'prediction': prediction})
    else:
        form = MakePredictions()

    return render(request, 'TitanicSurvivalPrediction/make_prediction.html', {'form': form})

def process_form_data(form):
    p_class = int(form['p_class'].value())
    sex_type = int(form['sex_type'].value())
    embarked = int(form['embarked'].value())
    age = int(form['age_category'].value())
    fare = int(form['fare_category'].value())
    family_size = int(form['family_size'].value())

    return [[p_class, sex_type, embarked, age, fare, family_size]]
