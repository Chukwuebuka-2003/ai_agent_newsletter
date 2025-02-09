from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from main import NewsletterCrew
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NewsletterRequest(BaseModel):
    user_input: str

@app.post("/generate-newsletter/")
async def generate_newsletter(request: NewsletterRequest):
    crew = NewsletterCrew(inputs=request.user_input)
    result = await crew.run()  # Await the async execution
    return {"newsletter": result}

@app.get("/")
def home():
    return {"message": "Welcome to the AI-Powered Newsletter API"}
