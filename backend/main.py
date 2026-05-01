from fastapi import FastAPI
from pydantic import BaseModel
from agents import diagnosis_agent, recommendation_agent, followup_agent
from db import Session, User

app = FastAPI()

class InputData(BaseModel):
    skin_type: str
    symptoms: str

@app.post("/analyze")
def analyze(data: InputData):
    diagnosis = diagnosis_agent(data.skin_type, data.symptoms)
    routine = recommendation_agent(diagnosis)

    session = Session()
    user = User(
        skin_type=data.skin_type,
        symptoms=data.symptoms,
        diagnosis=diagnosis,
        routine=routine
    )
    session.add(user)
    session.commit()

    return {
        "diagnosis": diagnosis,
        "routine": routine
    }


class FeedbackData(BaseModel):
    feedback: str

@app.post("/followup")
def followup(data: FeedbackData):
    updated = followup_agent(data.feedback)
    return {"updated_routine": updated}
