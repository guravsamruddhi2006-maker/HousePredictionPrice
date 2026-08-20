import io
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel, Field
from fastapi.responses import StreamingResponse
app = FastAPI()
model = joblib.load("house_model.joblib")
features = joblib.load("house_features.joblib")
class HouseFeatures(BaseModel):
    MedInc: float = Field(gt=0, description="Medium Income of Neighbourhood")
    HouseAge: float = Field(ge=0, description="Average age of house in the block")
    AveRooms: float = Field(gt=0, description="Average number of rooms")
    AveBedrms: float = Field(gt=0, description="Average number of Bedrooms")
    Population: float = Field(gt=0, description="Total population")
    AveOccup: float = Field(gt=0, description="Average number of occupants")
    Latitude: float = Field(gt=0, description="Latitude of the area")
    Longitude: float = Field(gt=0, description="Longitude of the area")
@app.get("/")
def home():
    return{
        "message":"california house prediction API",
        "status":"running",
        "endpoint":"send post request to predict"
    }
@app.get("/health")
def health():
    return {
        "status":"running",
        "model":"RandomForestRegressor",
        "features":features,
        "avg-error":"$39000"
    }
@app.post("/predict")
def predict(house:HouseFeatures):
    try:
        input_data = pd.DataFrame([{
            "MedInc":house.MedInc,
            "HouseAge":house.HouseAge,
            "AveRooms":house.AveRooms,
            "AveBedrms":house.AveBedrms,
            "Population":house.Population,
            "AveOccup":house.AveOccup,
            "Latitude":house.Latitude,
            "Longitude":house.Longitude
        }])
        predicted = model.predict(input_data)[0]
        price_usd = predicted*100000
        return {
            "predicted_price":f"${price_usd:,.0f}",
            "predict_price_short":f"${predicted:.2f}hundred thousands",
            "confidence_range":f"${price_usd-39000:,.0f} to ${price_usd + 39000:,.0f}"
        }
    except Exception as e:
        raise HTTPException(
            status_code = 500,
            detail = f"Prediction faild:{str(e)}"
        )
@app.post("/predict-file")
async def predict_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code = 400,
            detail = "Please upload a csv file only"
        )
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    required_columns = [
        "MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"
    
    ]
    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]
    if missing_columns:
        raise HTTPException(
            status_code = 400,
            detail = f'these columns are missing from your file {missing_columns}'
        )
    if len(df) == 0:
        raise HTTPException(
            status_code = 400,
            detail = 'the uploaded file has no data rows'
        )
    try:
        predictions = model.predict(df[required_columns])
        df["predicted_columns_usd"] = predictions * 100000
        df["predicted_price"] = df["predicted_columns_usd"].apply(lambda value: f"${value:,.0f}")
        output = df.to_csv(index = False)
        return StreamingResponse(io.StringIO(output), media_type="text/csv",
                                headers = {
                                    "Content-Disposition": "attachment; filename=prediction.csv"
                                }
        )
    except Exception as e:
        raise HTTPException(
            status_code = 500,
            detail = f"Prediction failed:{str(e)}"
        )