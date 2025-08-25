ANÁLISE DE DADOS COVID-19 POR CIDADE - BRASIL

DESCRIÇÃO DO PROJETO
Este projeto tem como objetivo analisar os dados de COVID-19 por cidade no Brasil, utilizando Python, Pandas, SQL e visualização com Matplotlib e Seaborn.

O script realiza as seguintes operações:
1. Leitura e limpeza do arquivo CSV 'caso_full.csv.gz'.
2. Inserção dos dados em uma tabela MySQL ('covid_city'), com inserção em blocos para grandes volumes.
3. Geração de relatórios:
   - Todos os casos de morte por cidade.
   - População estimada antes e depois dos casos por cidade.
   - Cidade com maior quantidade de casos.
   - Cidade com menor quantidade de casos.
4. Visualização gráfica:
   - Top 10 cidades por mortes.
   - População estimada antes e depois dos casos (Top 10 cidades).
   - Cidade com maior e menor quantidade de casos.

ARQUIVOS NO REPOSITÓRIO
- covid.py – Script principal para leitura, limpeza, inserção no MySQL e geração dos relatórios e gráficos.
- caso_full.csv.gz – Dataset compactado com dados de COVID-19 por cidade.
- README.txt – Este arquivo explicativo.
- relatorio.pdf – PDF contendo prints dos gráficos e tabelas geradas pelo script.

PRÉ-REQUISITOS
Antes de rodar o projeto, instale as seguintes ferramentas e bibliotecas:

- Python 3.13
- MySQL Server
- Bibliotecas Python:
    pip install pandas sqlalchemy mysql-connector-python matplotlib seaborn

COMO RODAR
1. Certifique-se de que o MySQL está rodando e crie o banco de dados:
    CREATE DATABASE covid_db;

2. Ajuste a configuração do MySQL no script 'covid.py':
    usuario = 'root'
    senha = 'root'
    host = 'localhost'
    banco = 'covid_db'

3. Execute o script Python:
    python covid.py

O script irá:
- Limpar a tabela 'covid_city' caso já exista.
- Inserir os dados do CSV no MySQL em blocos.
- Gerar os relatórios e gráficos.

RESULTADOS ESPERADOS
- Gráfico Top 10 cidades por mortes COVID
- População estimada antes e depois dos casos (Top 10 cidades)
- Cidade com maior e menor quantidade de casos
- Relatórios impressos no console

OBSERVAÇÕES
- Para gerar o PDF do relatório final, capture os prints das tabelas e gráficos exibidos pelo script.
- Suba o PDF e o link do repositório para a entrega.

