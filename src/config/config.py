# config.py
from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

dotenv_path = PROJECT_ROOT / ".env"
if not find_dotenv(str(dotenv_path), raise_error_if_not_found=False):
    raise FileNotFoundError(f".env file not found at {dotenv_path}")
load_dotenv(dotenv_path=dotenv_path)


def get_settings():
    return {
        "openai": os.getenv("OPENAI_API_KEY"),
        "anthropic": os.getenv("ANTHROPIC_API_KEY"),
        "gemini": os.getenv("GEMINI_API_KEY"),
        "debug": os.getenv("DEBUG", "False").lower() == "true",
        "env": os.getenv("ENV", "development"),
    }


# Validate on import
settings = get_settings()


def validate_settings(settings):
    if not settings["openai"]:
        raise ValueError("OpenAI API key missing in .env")
    if not settings["anthropic"]:
        raise ValueError("Anthropic API key missing in .env")
