from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))

try:
    with open("db.sql", encoding="utf-8") as sql:
        create_db = sql.read()

    with engine.begin() as con:
        con.execute(text("DROP SCHEMA IF EXISTS public CASCADE; CREATE SCHEMA public;"))
        con.execute(text(create_db))
        print("Foi")
    engine.dispose()

except Exception as e:
    print(e)