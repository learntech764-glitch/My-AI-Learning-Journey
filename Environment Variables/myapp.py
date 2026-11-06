from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_Key")
db_user = os.getenv("DB_User")
db_password = os.getenv("DB_Password")

print(f"API Key: {api_key}")
print(f"Database User: {db_user}") 
print(f"Database Password: {db_password}")

 # use custom environment variables file in your application
load_dotenv(dotenv_path=".env.custom")

env = os.getenv("ENV")

print(f"Environment: {env}")