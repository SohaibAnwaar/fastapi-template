from starlette.config import Config

from dotenv import load_dotenv

load_dotenv()
config = Config(".env")


