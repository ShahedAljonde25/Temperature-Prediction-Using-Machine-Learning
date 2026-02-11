from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

class ModelInput(BaseModel):
    AWND: float
    PGTM: float
    PRCP: float
    SNOW: float
    SNWD: float
    TMAX: float
    TMIN: float
    WDF5: float
    WSF5: float
    U_Component: float
    V_Component: float

weather_model = pickle.load(open(r"C:\Users\LOQ\Desktop\weather_prediction\weather_prediction.sav", "rb"))

@app.post("/weather_predict")
def weather_pred(input: ModelInput):
    input_dec = input.dict()
    
    input_list = [
        input_dec['AWND'],
        input_dec['PGTM'],
        input_dec['PRCP'],
        input_dec['SNOW'],
        input_dec['SNWD'],
        input_dec['TMAX'],
        input_dec['TMIN'],
        input_dec['WDF5'],
        input_dec['WSF5'],
        input_dec['U_Component'],
        input_dec['V_Component']
    ]
    
    prediction = weather_model.predict([input_list])
    
    return {"prediction": float(prediction[0])}
