from fastapi import FastAPI
from typing import Literal , Annotated
from pydantic import BaseModel, Field , computed_field
import pandas as pd
import pickle

# Import the pickle model
with open('model.pkl','rb')as f:
    model=pickle.load(f)

app= FastAPI()

# Pydentic model to validate the input data
class input_data(BaseModel):
    age: Annotated[int,Field(...,gt=0,lt=120, description="Age of the person in years")]
    weight: Annotated[float,Field(...,gt=0,lt=250, description="Weight of the person in kg")]
    height: Annotated[float,Field(...,gt=0,lt=10, description="Height of the person in cm")]
    income_lpa: Annotated[float,Field(...,gt=0, description="Income in lakhs per annum")]
    smoker: Annotated[bool,Field(description="Whether the person is a smoker or not")]
    city: Annotated[str,Field(description="City of residence")]
    occupation:Annotated[Literal['retired','freelancer','student','government_job','business_owner','unemployed','private_job'],
                         Field(...,description="Occupation of the person")]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi>30:
            return 'high'
        elif self.smoker or self.bmi>27:
            return 'medium'
        else:
            return 'low'