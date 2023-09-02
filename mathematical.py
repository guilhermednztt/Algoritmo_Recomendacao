"""
Contas de Matematica
"""

import numpy as np
from math import sqrt

# formulaPearson
def formulaPearson(x, y):
    """
    Formula/Coeficiente de Pearson

    A fórmula de Pearson corresponde a:\n

    r =  Somatória (x - Media(X)) x (y - Media(Y))\n
        --------------------------------------------\n
        R.Quadrada (x - Media(X))² x (y - Media(Y))²\n
    """

    mediaX = np.average(x)
    mediaY = np.average(y)
    soma_produto_desvio = 0
    soma_quadrado_desvio = 0

    for i in range(len(x)):
        desvioX = (x[i] - mediaX)
        desvioY = (y[i] - mediaY)
        soma_produto_desvio += desvioX * desvioY
        soma_quadrado_desvio += pow(desvioX, 2) * pow(desvioY, 2)
        
    soma_quadrado_desvio = sqrt(soma_quadrado_desvio)

    return soma_produto_desvio / soma_quadrado_desvio


# somaTransversal
def somaTransversal(valores):
    """
    Soma os valores das colunas e retorna.\n
    """
    linhas = len(valores)
    colunas = len(valores[0])
    somatorio = [0] * colunas

    for x in range(linhas):
        for y in range(colunas):
            somatorio[y] += valores[x][y]
    
    return somatorio

