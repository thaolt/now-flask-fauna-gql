from dotenv import load_dotenv
from pathlib import Path 

def load_env():
    env_path = (Path('.') / '.env').resolve()
    load_dotenv(dotenv_path=env_path)