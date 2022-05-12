from fastapi import FastAPI

from api.responses import CustomJSONResponse

app = FastAPI(
    default_response_class=CustomJSONResponse
)


@app.get("/")
async def root():
    return {"status": "ok"}

