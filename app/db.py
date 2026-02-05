from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./EZkana.db"

class Kana(SQLModel, table=True):
    __tablename__ = "hiragana"
    id: Optional[int] = Field(default=None, primary_key=True)
    kana: str = Field(nullable=False)
    romaji: str = Field(nullable=False)
    type: str = Field(nullable=False)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# This is the function the error says is missing
def get_session():
    with Session(engine) as session:
        yield session