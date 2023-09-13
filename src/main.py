from fastapi import FastAPI
import uvicorn
from auth.router import router as router_auth


app = FastAPI(
    title="Auth App"
)


def configure():
    configure_routing()


def configure_routing():
    app.include_router(router_auth)


if __name__ == '__main__':
    configure()
    uvicorn.run(app, host='127.0.0.1', port=8000)
else:
    configure()
