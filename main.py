from fastapi import FastAPI
from routers.exchangers import router as exchangers_router  

app = FastAPI(
    title="BestChange API",
    description="API для получения данных обменников с BestChange",
    version="1.0.0"
)

app.include_router(exchangers_router, prefix="/api", tags=["exchangers"])

@app.get("/")
def root():
    return {"message": "BestChange API работает. Документация /docs"}