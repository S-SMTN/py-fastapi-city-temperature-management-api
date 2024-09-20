from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def main() -> dict:
    return {"message": "Hello world"}
