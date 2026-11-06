 ## My understanding on Environment variables and .env file
   
    - Reference video : https://www.bing.com/videos/riverview/relatedvideo?q=Environment+Variables+in+Python.&&mid=A5330FC1009FF95DF0CFA5330FC1009FF95DF0CF&churl=https%3a%2f%2fwww.youtube.com%2fchannel%2fUCOtLXcr9o6G6pj-kgAYiPWw&FORM=VRDGAR

# Steps to use the .env files
    - Create a .env file
    - Create an environment "python -m venv .venv"
    - Activate the environment ".venv/Scripts/activate"
    - pip install python-dotenv
    - do not push to Git add in .gitignore so that the API keys are not disclosed
    - for custom env files use dotenv_path in load_dotenv
    - in production values are stored in Azure App Services and passwords and keys in Azure key vault

# Fromat of .env file
    - Naming convention .env
       Note : if u give a custom name like .env.custom then specify in load_dotenv
    - Syntax
        variable=value

# How to use it inside a py file
        - load load_dotenv package using "from dotenv import load_dotenv"
        - load os package using "import os" 
        - call unctopn load_dotenv()
        - os.getenv("variable")