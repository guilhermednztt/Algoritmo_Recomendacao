import mathematical as mtm
import database as dtb

# Pega o conjunto de avaliacoes de cada usuario em cada curso
dados = mtm.np.array(dtb.dados)

# Ignora os cursos em que o usuario ainda nao visualizou e refina o vetor
conteudoVisualizadoReduzido = [n for n in dtb.conteudoVisualizado if n > 0]

def calcularSemelhanca():
    """
    Calcula a semelhanca entre os usuarios baseado em suas avaliacoes.
    """
    for i in range(len(dados)):
        avaliacaoCurso = [x for x, y in zip(dados[i], dtb.conteudoVisualizado) if y > 0]
        dtb.semelhancaUsuarios[i] = mtm.formulaPearson(avaliacaoCurso, conteudoVisualizadoReduzido)
    

def calcularAvaliacoes():
    """
    Calcula a avaliacao de cada usuario em cada curso usando o grau de semelhance entre eles, ou
    o Coeficiente de Pearson.\n
    Para cada elemento da matriz, considera-se:\n
    Valor do índice * Conteudo Visualizado (Sim/Nao => 1/0) * Coeficiente de Pearson
    """
    avaliacoes = []
    for x in range(len(dtb.dados)):
        for y in range(len(dtb.conteudoVisualizado)):
            avaliacoes.append(dtb.dados[x][y] * dtb.conteudoNaoVisualizado[y] * dtb.semelhancaUsuarios[x])
        dtb.matrizAvaliativa.append(avaliacoes)
        avaliacoes = []

def calcularSemelhancaAvaliacao():
    """
    Multiplica a Semelhanca (coeficiente Pearson) por Verdadeiro/Falso (1/0)
    """
    dtb.pesoAvaliacoes = mtm.np.array(dtb.matrizAvaliativa)
    dtb.pesoAvaliacoes[dtb.pesoAvaliacoes > 0] = 1

    for x in range(len(dtb.pesoAvaliacoes)):
        for y in range(len(dtb.pesoAvaliacoes[0])):
            dtb.pesoAvaliacoes[x][y] *= dtb.semelhancaUsuarios[x]


def acumularValores():
    dtb.avaliacaoAcumulada = mtm.np.array(mtm.somaTransversal(dtb.matrizAvaliativa))
    dtb.semelhancaAcumulada = mtm.np.array(mtm.somaTransversal(dtb.pesoAvaliacoes))

def descobrirRelevancia():
    """
    Identifica qual coluna da matriz de conteudo possui melhor Avaliacao x Pearson
    """
    dtb.semelhancaAcumulada[dtb.semelhancaAcumulada <= 0] = -1
    vetorRelevancia = [x / y for x, y in zip(dtb.avaliacaoAcumulada, dtb.semelhancaAcumulada)]
    
    vetorRelevancia = mtm.np.argsort(vetorRelevancia)[::-1]
    
    return vetorRelevancia


def recomendarConteudo(vetorRelevancia, quantidade = 2):
    """
    Destaca o conteudo da matriz em ordem decrescente de relevancia, ou seja\n
    Mais Relevante em primeiro.
    """
    conteudos = []

    for i in range(quantidade):
        conteudos.append(dtb.nomeConteudos[vetorRelevancia[i]])
    
    return conteudos
    

# Executa as funcoes em direção da descoberta da melhor recomendacao.
calcularSemelhanca()
calcularAvaliacoes()
calcularSemelhancaAvaliacao()
acumularValores()
vetorRelevancia = descobrirRelevancia()
recomendacao = recomendarConteudo(vetorRelevancia)

# RESULTADO
print("\033[32m\n=> RESULTADO DA MELHOR RECOMENDAÇÃO (EM ORDEM):\n\n{}\n\033[0m".format(recomendacao))
