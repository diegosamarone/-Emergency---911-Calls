# Emergency_911_Calls
Projeto de análise de dados
# Ligação para o 911

## Descrição do Projeto
Este projeto tem como objetivo a prática em análise de dados reais. Estaremos analisando alguns dados de "chamada para o 911" do Kaggle.

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
5. **Criação de Nova Coluna**: É criada uma nova coluna "Razão" que contém o tipo de chamada (EMS, Fire, Traffic).
6. **Análise da Nova Coluna**: É exibida a contagem de chamadas 911 por tipo de chamada.
7. **Visualização dos Dados**: É criado um gráfico, utilizando a biblioteca Seaborn, com a contagem de chamadas 911 por tipo de chamada.


As tecnologias utilizadas até o momento neste projeto são:

1. **Python**
2. **Pandas**
3. **Matplotlib**
4. **Seaborn**
5. **Jupyter Notebook** (opcional)
6. **Kaggle** 
