import pandas as pd
from sqlalchemy import create_engine, text
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# CONFIGURAÇÃO DO MYSQL
# ----------------------------
usuario = 'root'
senha = 'root'
host = 'localhost'
banco = 'covid_db'

engine = create_engine(f'mysql+mysqlconnector://{usuario}:{senha}@{host}/{banco}')

# ----------------------------
# LEITURA DO CSV
# ----------------------------
caminho_csv = r"C:\Users\Marianna\Desktop\Analise de Dados e Big Data\analise-covid-brasil\caso_full.csv.gz"

colunas = [
    'city', 
    'city_ibge_code', 
    'date', 
    'last_available_confirmed', 
    'last_available_deaths', 
    'estimated_population_2019'
]

print("⌛ Lendo o CSV...")
df = pd.read_csv(caminho_csv, compression='gzip', usecols=colunas, encoding='utf-8')
print(f"✅ CSV carregado com {len(df)} linhas")

# ----------------------------
# LIMPEZA DOS DADOS
# ----------------------------
df = df.dropna(subset=['city_ibge_code', 'date'])
df['city_ibge_code'] = df['city_ibge_code'].astype(int)
df['last_available_confirmed'] = df['last_available_confirmed'].fillna(0).astype(int)
df['last_available_deaths'] = df['last_available_deaths'].fillna(0).astype(int)
df['estimated_population_2019'] = df['estimated_population_2019'].fillna(0).astype(int)
df['date'] = pd.to_datetime(df['date'])
print("✅ Dados limpos e tipos ajustados")

# ----------------------------
# LIMPAR TABELA ANTES DE INSERIR
# ----------------------------
with engine.connect() as conn:
    conn.execute(text("TRUNCATE TABLE covid_city"))
    conn.commit()
    print("🗑️ Tabela 'covid_city' limpa antes da inserção")

# ----------------------------
# INSERÇÃO EM BLOCOS NO MYSQL
# ----------------------------
tamanho_bloco = 100000
for i, inicio in enumerate(range(0, len(df), tamanho_bloco)):
    fim = inicio + tamanho_bloco
    bloco = df.iloc[inicio:fim]
    bloco.to_sql('covid_city', con=engine, if_exists='append', index=False)
    print(f"✅ Bloco {i+1} inserido: linhas {inicio} a {fim-1}")

print("🎉 Todos os dados foram inseridos no MySQL com sucesso!")

# ----------------------------
# RELATÓRIOS
# ----------------------------
df_mysql = pd.read_sql('SELECT * FROM covid_city', con=engine)

# 1️⃣ Todos os casos de morte por cidade (cumulativo)
mortes_por_cidade = df_mysql.groupby('city')['last_available_deaths'].max().sort_values(ascending=False)
print("\n💀 Casos de morte por cidade (Top 10):")
print(mortes_por_cidade.head(10))

# Gráfico mortes
plt.figure(figsize=(12,6))
sns.barplot(x=mortes_por_cidade.head(10).values, y=mortes_por_cidade.head(10).index, palette="Reds_r")
plt.title("Top 10 cidades por mortes COVID")
plt.xlabel("Número de mortes")
plt.ylabel("Cidade")
plt.show()

# 2️⃣ População estimada antes e depois dos casos (cumulativo)
populacao = df_mysql.groupby('city')[['estimated_population_2019', 'last_available_confirmed']].max()
populacao['pop_apos_casos'] = populacao['estimated_population_2019'] - populacao['last_available_confirmed']
print("\n👥 População estimada antes e depois dos casos (Top 10 cidades):")
print(populacao.head(10))

# Gráfico população vs casos (Top 10)
top10_pop = populacao.sort_values('estimated_population_2019', ascending=False).head(10)
plt.figure(figsize=(12,6))
sns.barplot(x=top10_pop['estimated_population_2019'], y=top10_pop.index, palette="Blues_r", label="População")
sns.barplot(x=top10_pop['pop_apos_casos'], y=top10_pop.index, palette="Greens_r", label="População após casos")
plt.title("Top 10 cidades: População antes e depois dos casos")
plt.xlabel("População")
plt.ylabel("Cidade")
plt.legend()
plt.show()

# 3️⃣ Cidade com maior quantidade de casos
maior_cidade = df_mysql.groupby('city')['last_available_confirmed'].max().idxmax()
quant_maior = df_mysql.groupby('city')['last_available_confirmed'].max().max()
print(f"\n🏙️ Cidade com maior quantidade de casos: {maior_cidade} ({quant_maior} casos)")

# 4️⃣ Cidade com menor quantidade de casos (com pelo menos 1 caso)
df_com_casos = df_mysql[df_mysql['last_available_confirmed'] > 0]
menor_cidade = df_com_casos.groupby('city')['last_available_confirmed'].max().idxmin()
quant_menor = df_com_casos.groupby('city')['last_available_confirmed'].max().min()
print(f"🏘️ Cidade com menor quantidade de casos: {menor_cidade} ({quant_menor} casos)")

# Gráfico maior e menor cidade em casos
plt.figure(figsize=(8,4))
sns.barplot(x=[quant_maior, quant_menor], y=[maior_cidade, menor_cidade], palette=["green","orange"])
plt.title("Cidade com maior e menor quantidade de casos")
plt.xlabel("Número de casos")
plt.ylabel("Cidade")
plt.show()
