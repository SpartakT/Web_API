from fastapi import FastAPI
from routers import exchangers

app = FastAPI(
    title="BestChange API",
    description="API для получения данных обменников с BestChange",
    version="1.0.0"
)

app.include_router(exchangers.router, prefix="/api", tags=["exchangers"])

@app.get("/")
def root():
    return {"message": "BestChange API работает. Документация /docs"}