import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Título
st.title("📊 Dashboard COVID-19 Brasil")

# Conexão com o MySQL
engine = create_engine("mysql+mysqlconnector://root:Lucas2025%40@localhost/covid_dashboard")

# Consulta SQL
query = """
    SELECT date, state, city, confirmed, deaths, estimated_population
    FROM casos_covid
"""
df = pd.read_sql(query, engine)

# Filtros interativos
ufs = sorted(df["state"].unique())
uf_selecionado = st.selectbox("Selecione o estado (UF):", ufs)

df_uf = df[df["state"] == uf_selecionado]

# Total por cidade (top 10)
df_top_cidades = (
    df_uf.groupby("city")[["confirmed", "deaths"]]
    .max()
    .sort_values("confirmed", ascending=False)
    .head(10)
)

# Gráfico de evolução
df_evolucao = (
    df_uf.groupby("date")[["confirmed", "deaths"]]
    .sum()
    .reset_index()
)

# Exibe os gráficos
st.subheader(f" Top 10 cidades com mais casos confirmados em {uf_selecionado}")
st.bar_chart(df_top_cidades["confirmed"])

st.subheader(f"📈 Evolução diária em {uf_selecionado}")
st.line_chart(df_evolucao.set_index("date"))

# Rodapé
st.caption("Fonte: Brasil.IO — Dados públicos de COVID-19")
