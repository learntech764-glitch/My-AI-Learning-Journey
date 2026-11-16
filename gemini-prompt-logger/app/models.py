from pydantic import BaseModel
from datetime import datetime


class PromptLog(BaseModel):

    timestamp: datetime

    prompt: str

    response: str

    latency: float