from fastapi import FastAPI

from endpoints.v1 import V1

app = FastAPI()


@app.get("/test/{word}")
async def test(word: str):
    return {"message": word+"!"}


app.include_router(V1)
