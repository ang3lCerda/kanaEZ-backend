from sqlmodel import Session, SQLModel
from app.db import engine, Kana

def seed_kana():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        # Initial vowels
        vowels = [
            Kana(kana="あ", romaji="a", type="Hiragana"),
            Kana(kana="い", romaji="i", type="Hiragana"),
            Kana(kana="う", romaji="u", type="Hiragana"),
            Kana(kana="え", romaji="e", type="Hiragana"),
            Kana(kana="お", romaji="o", type="Hiragana"),
        ]
        session.add_all(vowels)
        session.commit()

if __name__ == "__main__":
    seed_kana()