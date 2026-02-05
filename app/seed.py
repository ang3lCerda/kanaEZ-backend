import json
from sqlmodel import Session, SQLModel
from app.db import engine, Kana

def load_json(filename: str):
    try:
        with open(filename, encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return []

def seed_kana(filename: str):
    SQLModel.metadata.create_all(engine)
    
    data = load_json(filename)
    
    if not data:
        print(f"No data found in {filename}")
        return

    with Session(engine) as session:
        for item in data:
            kana_entry = Kana(
                kana=item["kana"],
                romaji=item["romaji"],
                type=item["type"],
                group=item["group"]
            )
            session.add(kana_entry)
        
        session.commit()
        print(f"Successfully seeded {len(data)} characters from {filename}")

if __name__ == "__main__":
    seed_kana("app/data/hiragana.json")
    seed_kana("app/data/katakana.json")