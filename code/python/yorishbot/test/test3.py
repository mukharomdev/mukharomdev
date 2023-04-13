import os
from dotenv import load_dotenv
load_dotenv()

config = os.environ

print(config["LINE_CHANNEL_SECRET"])