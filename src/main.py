from fastapi import FastAPI
import uvicorn
from src.auth.router import router as router_auth


app = FastAPI(
    title="Auth App"
)


@app.get('/')
async def root():
    server_status = {
        'status': 'running',
        'api_version': '0.1',
        'message': 'Welcome to the IVLEV_AUTH!'
    }
    return server_status


def configure():
    configure_routing()


def configure_routing():
    app.include_router(router_auth)


if __name__ == '__main__':
    configure()
    uvicorn.run(app, host='127.0.0.1', port=8000)
else:
    configure()
