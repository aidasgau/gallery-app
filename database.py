import json
from sqlalchemy import create_engine

# Load configuration from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

db_user = config["db_user"]
db_pass = config["db_pass"]
db_host = config["db_host"]
db_name = config["db_name"]

# Create the database engine
db_url = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}?charset=utf8mb4"
engine = create_engine(db_url)
