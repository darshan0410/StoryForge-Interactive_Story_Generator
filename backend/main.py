from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import requests
from core.config import settings
from routers import story,job
from db.database import create_tables

create_tables()

# Load environment variables
load_dotenv()

# Get OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(story.router,prefix=settings.API_PREFIX)
app.include_router(job.router,prefix=settings.API_PREFIX)

class StoryRequest(BaseModel):
    prompt: str
