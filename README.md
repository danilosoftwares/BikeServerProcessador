# Api ETL feita em python

## Resumo
Esta API foi desenvolvida com critério educativo.
Basicamente se trata de uma api que contem essencialmente 3 rotinas
- Ler e processar um arquivo csv e gravar no banco de dados
- Gerar um relatorio dos dados importados
- Apagar os dados caso deseje re-importar

## Banco de dados
A api tem uma classe de conexão e funções de acesso ao banco, o banco utilizado foi um banco mysql, nesta classe tem as rotinas:
 - Geração de banco, rotina que gera a estrutura do banco com base nas planilhas que seguem nas pasta de exemplo, ou seja, o banco foi desenvolvido préviamente pensado já nas planilhas
```python
def Create():
```
 - Rotina de gravação e leituras genericas
```python
def Set(comando, _conn=None):
def Get(comando, _conn=None):
```
 - Função de conexão para ser reaproveitada em funções que tem rotinas em lista
```python
def GetConnector():
```
 - Função de block (descontinuada)
```python
def SetBlock(_lista, _conn=None):
```

## Relatório
Basicametne a API monta um relatorio simples em html baseando-se em um scritp sql tambem simples

## Processamento
A Rotina de processamento basicamente ao ler os dados coloca os mesmos numa classe que analisa os dados conforme o pré entendimento dos campos da tabela. A gravação é feita em blocos, onde os mesmos são definidos conforme o tipo da tabela, esses blocos de inserção somente gravam e não fazem duplicidade nem alteração dos dados, por isso existe um botão de exclusão dos dados, visto que se trata de uma rotina simples

## Utilizando
![](demonstracao.gif)
