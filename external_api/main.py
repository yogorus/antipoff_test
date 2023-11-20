from fastapi import FastAPI
import uvicorn
from routers.cadastral import router

app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
