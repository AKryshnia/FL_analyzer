from fastapi import FastAPI
from backend.app.api.v1 import endpoints

app = FastAPI(
    title="Freelancer Earnings Analyzer API",
    version="1.0"
)

app.include_router(endpoints.router, prefix="/api/v1")
