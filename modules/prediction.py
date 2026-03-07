import pandas as pd
from pycaret.classification import load_model, predict_model

model = load_model("model_programming")

def predict_risk(data):

    df = pd.DataFrame(data)

    prediction = predict_model(model, data=df)

    result = prediction["prediction_label"][0]
    prob = prediction["prediction_score"][0]

    return result, prob