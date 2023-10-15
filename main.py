import time

import uvicorn as uvicorn
from fastapi import FastAPI

from config.celery_utils import create_celery
from routers import mews


def create_app() -> FastAPI:
    current_app = FastAPI(title="Parser microservice which receives data from Fetcher microservice ",
                          description="Parser microservice which receives data from Fetcher and send to Sender Micro "
                                      "service through celery and RabbitMQ",
                          version="1.0.0", )

    current_app.celery_app = create_celery()
    current_app.include_router(mews.router)
    return current_app


app = create_app()
celery = app.celery_app


@app.middleware("http")
async def add_process_time_header(request, call_next):
    print('inside middleware!')
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(f'{process_time:0.4f} sec')
    print('Processing time', str(f'{process_time:0.4f} sec'))
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", port=8100, reload=True)
