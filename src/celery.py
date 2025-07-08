from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "trading_bot",
    broker=REDIS_URL,
    backend=REDIS_URL
)

celery_app.conf.timezone = "UTC"

# 👇 Important: Ensure tasks get loaded
import src.bot.tasks
