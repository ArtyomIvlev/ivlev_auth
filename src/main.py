from fastapi import FastAPI
from src.auth.router import router as router_auth


app = FastAPI(
    title="Auth App"
)

app.include_router(router_auth)
