from pymongo import MongoClient, ASCENDING
from datetime import date
import pandas as pd
import matplotlib.pyplot as pltr

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

MONGO_URI   = "mongodb://admin:G5g56@localhost:27017/?authSource=admin"   # ou sua string Atlas
DB_NAME     = "local"
COLLECTION  = "Rotina"

print("Conectando ao MongoDB...")
col = MongoClient(MONGO_URI)[DB_NAME][COLLECTION]
print("Conexão estabelecida.")

query = col.find({"year": 2026, "month": 5})

documents = list(query)

DATA = pd.DataFrame(documents)
print(DATA)

with open("Dados_Mongo_DB.txt", "w") as f:
    f.write(str(DATA))
