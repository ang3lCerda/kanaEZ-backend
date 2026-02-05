from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from sqlmodel import Session, SQLModel, select

from app.db import engine, get_session, Kana
from app.seed import seed_kana
from app.schemas import KanaResponse
from typing import List

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    
    # 2. Check if we need to seed (to avoid duplicates every restart)
    with Session(engine) as session:
        existing = session.exec(select(Kana)).first()
        if not existing:
            print("Database empty. Seeding...")
            seed_kana("app/data/hiragana.json")
            seed_kana("app/data/hiragana.json")
        else:
            print("Database already has data. Skipping seed.")
    
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "welcome to the EZkana api"}

# ... rest of your endpoints

# Endpoint to get all Kana characters
@app.get("/kana", response_model=List[KanaResponse])
async def get_all_kana(session: Session = Depends(get_session)):
    # Standard SQL select statement similar to your previous logic
    kana_list = session.exec(select(Kana)).all()
    return kana_list

# Endpoint to get a specific character by its ID
@app.get("/kana/{id}", response_model=KanaResponse)
async def get_kana_by_id(id: int, session: Session = Depends(get_session)):
    kana = session.get(Kana, id)
    
    if not kana:
        raise HTTPException(status_code=404, detail="Kana not found")
    
    return kana