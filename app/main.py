from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
import os
import socket

# Load environment variables from .env
load_dotenv()

app = FastAPI()

# Read environment variables
APP_NAME = os.getenv("APP_NAME", "Unknown App")
APP_VERSION = os.getenv("APP_VERSION", "0.0.0")


@app.get("/")
async def root():
    return {"message": "Hello from FastAPI CICD Project!"}


@app.get("/health")
async def health():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return {
        "app_name": APP_NAME,
        "app_version": APP_VERSION,
        "container_hostname": hostname,
        "container_ip": ip_address
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
