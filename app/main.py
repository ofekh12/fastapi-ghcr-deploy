import logging
from fastapi import FastAPI
import os

LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(f"{LOG_DIR}/app.log"), 
        logging.StreamHandler()                    
    ]
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="My Professional FastAPI Project",
    description="A simple API to demonstrate CI/CD with Docker and GHCR",
    version="1.0.0"
)

@app.get("/")
def read_root():
    logger.info("Root endpoint was accessed")
    return {"message": "Welcome to my API!"}

@app.get("/health")
def health_check():
    logger.info("Health check performed")
    return {"status": "healthy"}