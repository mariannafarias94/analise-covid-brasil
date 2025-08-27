# ANÁLISE DE DADOS COVID-19 POR CIDADE - BRASIL

## 📌 Descrição do Projeto
Este projeto tem como objetivo analisar os dados de COVID-19 por cidade no Brasil, utilizando **Python**, **Pandas**, **SQL** e visualização com **Matplotlib** e **Seaborn**.

O script realiza as seguintes operações:

- Leitura e limpeza do arquivo CSV `caso_full.csv.gz`.  
- Inserção dos dados em uma tabela MySQL (`covid_city`), com inserção em blocos para grandes volumes.  
- Geração de relatórios:  
  - Todos os casos de morte por cidade.  
  - População estimada antes e depois dos casos por cidade.  
  - Cidade com maior quantidade de casos.  
  - Cidade com menor quantidade de casos.  
- Visualização gráfica:  
  - Top 10 cidades por mortes.  
  - População estimada antes e depois dos casos (Top 10 cidades).  
  - Cidade com maior e menor quantidade de casos.  

---

## 📂 Arquivos no Repositório

- `covid.py` – Script principal para leitura, limpeza, inserção no MySQL e geração dos relatórios e gráficos.  
- `caso_full.csv.gz` – Dataset compactado com dados de COVID-19 por cidade.  
- `README.md` – Este arquivo explicativo.  
- `relatorio.pdf` – PDF contendo prints dos gráficos e tabelas geradas pelo script.  

---

## ⚙️ Pré-requisitos

Antes de rodar o projeto, instale as seguintes ferramentas e bibliotecas:

- [Python 3.13](https://www.python.org/downloads/)  
- [MySQL Server](https://dev.mysql.com/downloads/mysql/)  
- Bibliotecas Python:  

```bash
pip install pandas sqlalchemy mysql-connector-python matplotlib seaborn
```

---

## ▶️ Como Rodar

1. Certifique-se de que o MySQL está rodando.  
2. Crie o banco de dados:  

```sql
CREATE DATABASE covid_db;
```

3. Crie a tabela:  

```sql
CREATE TABLE covid_city (
    city VARCHAR(255),
    city_ibge_code INT,
    date DATE,
    estimated_population_2019 INT,
    last_available_confirmed INT,
    last_available_deaths INT
);
```

4. Ajuste a configuração do MySQL no script `covid.py`:  

```python
usuario = 'root'
senha = 'root'
host = 'localhost'
banco = 'covid_db'
```

5. Execute o script Python:  

```bash
python covid.py
```

O script irá:  
- Limpar a tabela `covid_city` caso já exista.  
- Inserir os dados do CSV no MySQL em blocos.  
- Gerar os relatórios e gráficos.  

---

## 📊 Resultados Esperados

- Gráfico **Top 10 cidades por mortes COVID**.  
- Gráfico **População estimada antes e depois dos casos (Top 10 cidades)**.  
- Gráfico da **Cidade com maior e menor quantidade de casos**.  
- Relatórios impressos no console.  

---

## 📝 Observações

- Para gerar o PDF do relatório final, capture os prints das tabelas e gráficos exibidos pelo script.  
