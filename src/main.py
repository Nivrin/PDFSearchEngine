from fastapi import FastAPI
import uvicorn
from .api.pdf import pdf_router

app = FastAPI()

app.include_router(pdf_router.router)


@app.get("/isAlive")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    # Use uvicorn to run the FastAPI app
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)