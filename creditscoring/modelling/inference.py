import pandas as pd
from sklearn.pipeline import Pipeline
from creditscoring.settings import Settings
from creditscoring.modelling.utils import load_model

s = Settings()


def inference(data: pd.DataFrame, model: Pipeline=None):
	if model is None:
		model = load_model()
	return model.predict_proba(data)
