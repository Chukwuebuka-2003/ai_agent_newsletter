from fastapi import FastAPI
from pydantic import BaseModel
from main import NewsletterCrew

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Now access variables using os.getenv()
import os

app = FastAPI()

class NewsletterRequest(BaseModel):
    user_input: str

@app.post("/generate-newsletter/")
def generate_newsletter(request: NewsletterRequest):
    crew = NewsletterCrew(inputs=request.user_input)
    result = crew.run()
    return {"newsletter": result}

@app.get("/")
def home():
    return {"message": "Welcome to the AI-Powered Newsletter API"}
