## AI-Prompt-Logger
(This is an async approach where all prompts are executed and logged at once)
   # Objective
        - Build a production-style AI application that:
        - Uses Gemini API
        - Handles multiple prompts asynchronously
        - Logs all requests/responses
        - Tracks latency
        - Stores results in JSONL
        - Loads secrets from .env
        - Uses Pydantic validation
        - Has structured logging
    
   # Steps to create this project

        1. Create below folder structure
            gemini-prompt-logger/
               ├── app/
               │   ├── config.py
               │   ├── gemini_client.py
               │   ├── logger.py
               │   ├── models.py
               │   ├── metrics.py
               │   └── api.py
               │
               ├── tests/
               │   ├── test_models.py
               │   ├── test_metrics.py
               │   └── test_api.py
               │
               ├── logs/
               │   └── prompts.jsonl
               │
               ├── .env
               ├── requirements.txt
               ├── run_batch.py
               └── README.md

        2. Update below in requirements .txt
               google-generativeai
               python-dotenv
               pydantic
               fastapi
               uvicorn
               pytest
               httpx
               tenacity
               google-genai
        3. Create a virtual env using "python -m venv .venv"
        4. Activate the virtual env using ".venv/Scripts/Activate"
        5. use command "pip install -r requirements.txt" to install all required libraries
        6. Create all .Py files

   NOTE: This run all prompt at a time and logs its response

   # Env file structure 

     GEMINI_API_KEY=<your-api--key>
     MODEL_NAME=<your-model>
