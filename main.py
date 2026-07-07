import uvicorn
from fastapi import FastAPI

from controlador.controlador_agente_menu import router as agente_menu_router

app = FastAPI()

app.include_router (agente_menu_router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        port = 80,
        reload = True
    )