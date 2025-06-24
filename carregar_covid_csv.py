import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("caso_full.csv.gz", compression='gzip', low_memory=False)

df = df[(df["is_last"] == True) & (df["place_type"] == "city")]

df = df[[
    "date", "state", "city",
    "last_available_confirmed",
    "last_available_deaths",
    "estimated_population"
]]

df.rename(columns={
    "last_available_confirmed": "confirmed",
    "last_available_deaths": "deaths"
}, inplace=True)

engine = create_engine("mysql+mysqlconnector://root:Lucas2025%40@localhost/covid_dashboard")

df.to_sql(name="casos_covid", con=engine, if_exists="replace", index=False)

print("✅ Dados carregados no banco com sucesso!")
