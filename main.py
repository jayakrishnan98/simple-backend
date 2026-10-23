from fastapi import FastAPI

app = FastAPI(title="aws-learning-fastapi")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/hello")
def hello(name: str = "world"):
    return {"message": f"Hello, {name}!"}
