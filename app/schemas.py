from pydantic import BaseModel

class KanaBase(BaseModel):
    kana: str
    romaji: str
    type: str
    group: str


class KanaCreate(KanaBase):
    pass

class KanaResponse(KanaBase):
    id: int
    class Config:
        from_attributes = True