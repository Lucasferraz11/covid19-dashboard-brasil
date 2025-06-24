# 🦠 Dashboard COVID-19 Brasil – Python + MySQL + Power BI + Streamlit

Este projeto realiza a extração, tratamento, armazenamento e visualização de dados reais da COVID-19 no Brasil. A base é carregada com Python, armazenada em MySQL e visualizada por meio de um dashboard interativo desenvolvido com **Streamlit** e **Power BI**.

---

## 🎯 Objetivo

Fornecer um painel interativo com informações relevantes sobre a pandemia no Brasil, permitindo análise por data, estado e cidade com base em dados reais e públicos.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.13**
  - `pandas`
  - `sqlalchemy`
  - `mysql-connector-python`
  - `streamlit`
- **MySQL 8.0**
- **Power BI Desktop**
- **Fonte de dados**: [Brasil.IO – caso_full.csv.gz](https://data.brasil.io/dataset/covid19/caso_full.csv.gz)

---

## 📁 Estrutura do Projeto

dashboards_dados_reais/
├── caso_full.csv.gz # Base de dados original
├── carregar_covid_csv.py # Script Python para carregar dados no MySQL
├── app.py # Aplicação interativa em Streamlit
└── README.md # Este arquivo

---

## ⚙️ Como Executar

### 1. Instale as dependências
```bash
pip install pandas sqlalchemy mysql-connector-python streamlit

2. Crie o banco de dados no MySQL
CREATE DATABASE covid_dashboard;

3. Execute o script Python para carregar os dados
python carregar_covid_csv.py

4. Rode o dashboard com Streamlit
streamlit run app.py

🗂️ Estrutura da Tabela no MySQL
Coluna	Tipo	Descrição
date	DATE	Data do registro
state	VARCHAR(2)	Sigla do estado (UF)
city	VARCHAR	Nome da cidade
confirmed	INT	Casos confirmados acumulados
deaths	INT	Mortes acumuladas
estimated_population	INT	População estimada

📊 Visualizações Power BI
✅ Cartão: Total de Casos Confirmados

✅ Cartão: Total de Óbitos

✅ Gráfico de Linha: Evolução por Data

✅ Segmentação por Estado (UF)



🌐 Visualizações com Streamlit
Dashboard interativo criado com Python, exibido no navegador com:

Filtro de estado (UF)

Gráfico de linha com evolução por data

Gráfico de barras com Top 10 cidades

📌 Fonte dos Dados
Dados públicos extraídos do repositório Brasil.IO, com base nos boletins das Secretarias Estaduais de Saúde.

👨‍💻 Autor
Lucas Ferraz