from django.apps import AppConfig
import .TitanicSurvivalPrediction.titanic_model.prediction_model as pm


class PredictionappConfig(AppConfig):
    name = 'predictionApp'

    def ready(self):
        pm.get_predictive_model()
