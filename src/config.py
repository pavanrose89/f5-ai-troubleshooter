import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration management using environment variables
OLLAMA_URL = os.getenv('OLLAMA_URL')
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL')
AI_TIMEOUT = int(os.getenv('AI_TIMEOUT', 30))  # Default to 30 seconds if not set
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')  # Default to 'INFO' if not set
