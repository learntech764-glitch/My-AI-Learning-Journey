from fastapi import FastAPI

from pydantic import BaseModel

from app.gemini_client import ask_gemini

app = FastAPI()


class PromptRequest(
    BaseModel
):

    prompt: str


@app.get("/health/ready")
async def readiness():
    await ask_gemini("Reply with OK.")
    return {"status": "healthy", "gemini": "reachable"}


@app.post("/ask")
async def ask(
    request: PromptRequest
):

    return await ask_gemini(
        request.prompt
    )