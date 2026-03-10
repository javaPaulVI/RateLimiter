from fastapi import FastAPI

import endpoints.v1 as v1

app = FastAPI()


@app.get("/test/{word}")
async def test(word: str):
    return {"message": word+"!"}


app.include_router(v1.V1)
