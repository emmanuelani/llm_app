from model import chat_bot
import os
from fastapi import FastAPI, requests, HTTPException
from fastapi.responses import StreamingResponse, PlainTextResponse
import groq
from dotenv import load_dotenv

load_dotenv()

# initializing the app
app = FastAPI()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
client = groq.Groq(api_key=GROQ_API_KEY)

@app.route("/chat_batch", method=["POST"])
async def chat_batch(request: Request):
    user_i