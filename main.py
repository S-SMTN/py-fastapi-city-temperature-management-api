from fastapi import FastAPI
from City_app.router import city_router
from Temperature_app.router import temperature_router


app = FastAPI()

app.include_router(city_router)
app.include_router(temperature_router)


@app.get("/")
def main() -> dict:
    return {"message": "Hello world"}
