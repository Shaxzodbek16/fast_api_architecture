from fastapi import FastAPI

def create_app() -> FastAPI:
    app_ = FastAPI(
        title="PDP's Hotel",
        description="This is a project for learning FastApi",
        version="0.1.0",
    )
    return app_
