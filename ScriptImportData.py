#!bin/bash/python3

from pymongo import MongoClient, ASCENDING
from datetime import date

MONGO_URI   = "mongodb://admin:G5g56@localhost:27017"   # ou sua string Atlas
DB_NAME     = "local"
COLLECTION  = "Rotina"

YEAR  = 2026
MONTH = 5          # maio

# Abreviação usada no caderno → nome no banco
CATEGORIES = {
    "V":  "vicio",
    "ET": "estudo_tecnico",
    "EC": "estudo_cultural",
    "R":  "relacionamento",
    "O":  "descontracao",
    "T":  "trabalho",
    "Sm": "saude_mental",
    "H":  "hidratacao",
    "S":  "sono_descanso",
}

# Um valor por dia (índice 0 = dia 1).  None = não preenchido.
DATA = {
    #         d1  d2  d3  d4  d5  d6  d7  d8  d9 d10 d11 d12 d13 d14 d15 d16 d17 d18 d19 d20 d21 d22 d23 d24 d25 d26 d27 d28 d29 d30 d31
    "EC": [    0,  0,  2,  0,  0,  0,  0,  1,None,  2,  2,  3,  3,  0,  1,  0,  0,  0,  2,  2,  1,  0,  2,None,  0,  1,  0,  2,  2,  2,  2],
    "ET": [    2,  1,  1,  2,  1,  2,  2,  0,None,  2,  3,  3,  0,  1,  0,  0,  1,  0,  2,  2,  0,  2,  1,None,  3,  0,  2,  1,  0,  0,  0],
    "V":  [    0,  0,  0,  1,  2,  0,  0,  2,None,  4,  3,  3,  2,  2,  3,  2,  4,  3,  1,  0,  0,  0,  0,None,  0,  0,  0,  2,  0,  2,  2],
    "O":  [    1,  2,  3,  2,  0,  2,  2,  2,None,  3,  3,  2,  3,  3,  3,  3,  4,  2,  2,  4,  1,  1,  2,None,  3,  3,  3,  3,  3,  4,  1],
    "R":  [    2,  2,  3,  1,  2,  2,  3,  2,None,  4,  3,  3,  2,  3,  3,  3,  3,  3,  1,  2,  4,  1,  2,None,  3,  3,  2,  2,  2,  3,  3],
    "T":  [    2,  3,  0,  3,  3,  4,  4,  4,None,  0,  4,  0,  3,  3,  3,  3,  4,  2,  0,  3,  3,  3,  4,None,  0,  4,  4,  4,  4,  0,  0],
    "Sm": [    4,  3,  4,  3,  3,  2,  2,  3,None,  3,  2,  3,  3,  3,  3,  3,  4,  3,  3,  3,  4,  3,  3,None,  3,  3,  3,  2,  2,  4,  4],
    "S":  [    3,  2,  2,  3,  3,  3,  2,  2,None,  4,  3,  3,  3,  3,  3,  3,  3,  3,  4,  3,  3,  3,  3,None,  3,  2,  2,  3,  3,  3,  3],
    "H":  [    2,  3,  2,  3,  3,  3,  3,  2,None,  2,  2,  4,  2,  3,  2,  2,  2,  2,  3,  2,  3,  3,  2,None,  2,  2,  2,  2,  2,  2,  2],
}

# ── FIM DA EDIÇÃO ───────────────────────────────────────────────────────────

for k, v in DATA.items():
	print(k, len(v))

def main():
    col = MongoClient(MONGO_URI)[DB_NAME][COLLECTION]
    col.create_index([("category", ASCENDING), ("date", ASCENDING)], unique=True)

    records = [
        {
            "category": CATEGORIES[abbr],
            "date":     date(YEAR, MONTH, day_idx + 1).isoformat(),
            "year":     YEAR,
            "month":    MONTH,
            "day":      day_idx + 1,
            "score":    score,
        }
        for abbr, values in DATA.items()
        for day_idx, score in enumerate(values)
        if score is not None
    ]

    ok = fail = 0
    for rec in records:
        try:
            col.update_one(
                {"category": rec["category"], "date": rec["date"]},
                {"$set": rec},
                upsert=True,
            )
            ok += 1
        except Exception as e:
            print(f"  Erro em {rec['category']} {rec['date']}: {e}")
            fail += 1

    print(f"\n✓ {ok} registros inseridos/atualizados  |  ✗ {fail} erros")
    print(f"  Coleção: {DB_NAME}.{COLLECTION}\n")


if __name__ == "__main__":
    main()
