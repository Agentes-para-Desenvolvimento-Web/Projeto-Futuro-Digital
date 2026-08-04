from fastapi import FastAPI
import uvicorn
from routers.agente import router as agente_router

app = FastAPI()

app.include_router(agente_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=80, reload=True)