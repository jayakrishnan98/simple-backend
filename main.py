from fastapi import APIRouter, FastAPI

app = FastAPI(title="aws-learning-fastapi")
api = APIRouter(prefix="/api")


@api.get("/health")
def health():
    return {"status": "ok"}


@api.get("/hello")
def hello(name: str = "world"):
    return {"message": f"Hello, {name} Deployed!"}


app.include_router(api)
