"""
Aqui consta o conjunto de dados exemplo/ficticio para simulacao do algoritmo
"""

# Avaliacao dos usuarios em cada conteudo.
# linha = usuario | coluna = conteudo
dados = [
    [8, 0, 3, 4, 6],
    [5, 6, 1, 8, 9],
    [8, 0, 0, 5, 10],
    [8, 0, 3, 6, 8],
    [5, 6, 5, 9, 4],
    [7, 7, 2, 2, 1],
    [9, 8, 6, 7, 0],
    [5, 6, 4, 3, 0],
    [6, 4, 1, 6, 3]
]

# Arranjo da avaliacao que o usuario alvo fez.
# 0 = conteudo nao visualizado (ainda)
conteudoVisualizado = [8, 0, 2, 3, 0]

# Arranjo de 0 e 1 (verdadeiro/falso) para identificar se o usuario alvo consumiou
# ou nao o conteudo.
conteudoNaoVisualizado = [0, 1, 0, 0, 1]

# Cada nome representa um conteudo.
nomeConteudos = [
    'Projetos para PyPi.org', 'Python para DataScience', 'Algoritmos Genéticos: Têmpera Simulada',
    'Thmpson Sampling para Sistemas de Recomendação' ,'NoSQL InfluxDB - Série Temporal & e IA'
]

# Coeficiente Pearson / grau de Semelhanca entre os usuarios e o usuario alvo
semelhancaUsuarios = [0] * len(dados)

# Matriz com as avaliacoes de cada usuario multiplicado pelo grau de semelhanca com o 
# usuario alvo.
matrizAvaliativa = []

# Somatoria das avaliacoes da matriz avaliativa por coluna.
avaliacaoAcumulada = [0] * len(conteudoNaoVisualizado)

# Somatoria do coeficiente Pearson em cada coluna.
semelhancaAcumulada = [0] * len(conteudoNaoVisualizado)

# Somatoria das Semelhancas em cada coluna. Onde na matriz avaliativa for 0 não entra na soma.
pesoAvaliacoes = []
