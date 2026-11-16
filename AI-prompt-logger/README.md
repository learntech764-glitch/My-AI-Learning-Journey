## AI-Prompt-Logger
(This is an async approach where all prompts are executed and logged one at a time)
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
                │
                ├── app/
                │   ├── main.py
                │   ├── gemini_client.py
                │   ├── config.py
                │   ├── models.py
                │   ├── logger.py
                │
                ├── logs/
                │   └── prompts.jsonl
                │
                ├── tests/
                │
                ├── .env
                ├── .gitignore
                ├── requirements.txt
                ├── README.md
                └── run.py

        2. Update below in requirements .txt
                google-generativeai
                python-dotenv
                pydantic
                aiofiles
                tenacity
        3. Create a virtual env using "python -m venv .venv"
        4. Activate the virtual env using ".venv/Scripts/Activate"
        5. use command "pip install -r requirements.txt" to install all required libraries
        6. Create .env file
        7. Create config.py
        8. Create models.py
        9. Create logger.py
        10. Create gemini_client.py
        11. Create main.py
        12. Create run.py

   NOTE: This run one prompt at a time and logs its response

 # Env file structure 

     GEMINI_API_KEY=<your-api--key>
     MODEL_NAME=<your-model>
