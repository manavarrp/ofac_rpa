import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

URL_OFAC = "https://sanctionssearch.ofac.treas.gov/"