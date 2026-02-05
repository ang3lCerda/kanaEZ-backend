from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from app.db import get_session, engine, Kana
from app.schemas import KanaResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "welcome to the EZkana api"}

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