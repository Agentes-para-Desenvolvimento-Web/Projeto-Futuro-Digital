import asyncio
from app.database import engine, Base

import app.models

async def init_db():
    async with engine.begin() as conn:
        # run_sync permite executar comandos síncronos (como create_all) no modo async
        await conn.run_sync(Base.metadata.create_all)
    print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    asyncio.run(init_db())