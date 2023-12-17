![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Spyder](https://img.shields.io/badge/Spyder-838485?style=for-the-badge&logo=spyder%20ide&logoColor=maroon)
 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
 ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
 ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
<img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" alt="Seaborn" width="90" height="45">
 ![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)
# Emergency_911_Calls
Projeto de análise de dados
# Ligação para o 911

## Descrição do Projeto
O propósito deste projeto é proporcionar prática em análise de dados reais. Vamos explorar dados de "chamadas para o 911" do Kaggle, buscando obter uma visão abrangente que destaque padrões temporais, razões comuns e outras informações essenciais.

## Dataset
O dataset utilizado é o "Emergency - 911 Calls", que pode ser baixado no site do Kaggle. Link: https://www.kaggle.com/datasets/mchirico/montcoalert/

## Campos do Dataset
Os dados contêm os seguintes campos:
- `lat`: Latitude
- `desc`: Descrição da chamada de emergência
- `zip`: CEP
- `titulo`: Título
- `timeStamp`: Data e hora no formato AAAA-MM-DD HH:MM:SS
- `twp`: Township
- `addr`: Endereço
- `e`: variável Dummy (sempre 1)

## Análise de Dados
A análise dos dados é realizada em várias etapas:

1. **Leitura do Dataset**: O dataset é lido e armazenado em um dataframe.
2. **Informações Básicas**: São exibidas informações básicas sobre o dataframe, como o número de linhas e colunas e os tipos de dados de cada coluna.
3. **Análise dos CEPs e Municípios**: São verificados os 5 CEPs e municípios mais frequentes nas chamadas 911.
4. **Análise dos Títulos**: É contada a quantidade de códigos de títulos exclusivos.
5. **Criação de Nova Coluna**: É criada uma nova coluna "Razão" que contém os tipos de chamada (EMS, Fire, Traffic).
6. **Análise da Nova Coluna**: É exibida a contagem de chamadas 911 por tipo de chamada.
7. **Visualização dos Dados**: É criado um countplot , utilizando a biblioteca Seaborn, com a contagem de chamadas 911 por tipo de chamada.
8. **Trabalhando com Informações de Tempo:**
    - Conversão da coluna 'timeStamp' para objetos DateTime.
    - Criação de novas colunas 'Hour', 'Month' e 'Day of Week' usando .apply().
    - Mapeamento do dia da semana para nomes reais.
    - Criação de countplots para 'Day of Week' e 'Month'.
9. **Análise de Dados Temporais:**
    - Criação de um objeto groupby ('byMonth') para contagem de chamadas por mês.
    - Criação de um plot linear para análise de tendências mensais usando lmplot().
10. **Agrupamento por Data:**
    - Criação da coluna 'Data' a partir da coluna 'timeStamp'.
    - Agrupamento por 'Data' e criação de gráfico de contagens de chamadas 911.
11. **Análise por Razão da Chamada:**
    - Criação de plots separados para cada razão de chamada ('EMS', 'Fire', 'Traffic').
12. **Mapas de Calor:**
    - Reestruturação do DataFrame para colunas de horas e índice de dia da semana.
    - Criação de mapas de calor e clustermap para análise visual.
13. **Análise Mensal com Mapas de Calor:**
    - Repetição dos passos anteriores para um DataFrame com meses como coluna.
   

As tecnologias utilizadas até o momento neste projeto são:

1. **IDE's: Jupyter Notebook e Spyder(anaconda)**
2. **Python**
3. **Pandas**
4. **Numpy**
5. **Matplotlib**
6. **Seaborn** 
7. **Kaggle**
