## utilities
import os
import pickle

## constants import
from config.constants import CONSTANTS

## db functions
from core.db.db_student import get_student_by_id

## package imports
import pandas as pd



preprocessor = None
estimator = None


## loading preprocessor
with open(os.path.join(CONSTANTS["MODELS_PATH"], "student_data_preprocessor.pickle"), "rb") as file:
    preprocessor = pickle.load(file)

## loadin estimator    
with open(os.path.join(CONSTANTS["MODELS_PATH"], "grade_predictor.pickle"), "rb") as file:
    estimator = pickle.load(file)
    
    
    
def get_performance_prediction(data):
    processed = preprocessor.transform(pd.DataFrame(data, index=[0]))
    return {"prediction": estimator.predict(processed)[0]}

# 97dbc32c-e75b-48f9-99a7-1681ccd27dd5