<h1 align="center">Algoritmo de Recomendação</h1>
<p align="center">Colaborativo: baseado no coeficiente Pearson dos elementos, ou grau de semelhança entre os mesmos.<br><br>
<img src="https://www.transparentpng.com/thumb/networking/networking-vector-6.png" width="300" height="200"></p>

<b><h3>I. Introdução</h3></b>
<p>Algoritmos de recomendação são técnicas de <b>Inteligência Artificial</b> que visam encontrar em um conjunto de dados elementos que se relacionam melhor e oferecer um ao outro, considerando que quanto maior a semelhança entre eles, maior será a chance de aceitação entre ambos. O modelo usado nesse repositório é o <b>COLABORATIVO</b>, que considera a interação dos diferentes indivíduos para identificar os que possuem interações semelhantes e assim fazer a combinação. A título de curiosidade, outros modelos são:
<u>
  <li><b>Filtragem por Conteúdo:</b> conteúdos semelhantes aos consumidos anteriormente por um indivíduo podem ser recomendados.</li>
  <li><b>Filtragem por Popularidade:</b> conteúdos em alta podem ser recomendados independente da afinidade entre o indivíduo e o conteúdo.</li>
</u></p>

<br>

<b><h3>II. Revisão Matemática</h3></b>
<p>Para identificar a semelhança entre os indivíduos, considerou-se a avaliação que cada um fez em supostos cursos em uma plataforma de cursos. Assim, foi gerado uma <b>matriz</b> contendo as avaliações: cada linha da matriz representa a avaliaçâo de um usuário, e cada coluna representa o curso avaliado. Exemplo:

```py
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
```
Observa-se que coletamos avaliação de 9 usuários em 5 cursos diferentes. E também foi coletado um vetor com a avaliação de um usuário alvo, a qual queremos recomendar um curso:

```py
conteudoVisualizado = [8, 0, 2, 3, 0]
```
Nesse caso, o usuário a quem vamos recomendar algum curso, indica não ter feito 2 cursos: da segunda e última coluna (indicados por 0). Nossa missão é escolher qual curso dos que ainda não foram vistos devemos recomendar.

<b><li>Coeficiente Pearson:</b> verifica a relação entre duas variáveis (lineares) e obtém a intensidade (grau de semelhança) entre -1 e 1, indicando total diferença à total semelhança. Dada pela fórmula:<br>
<p align="center"><b>&#8721; (x - &#772;x) * (y - &#772;y) /<br> &#8730; &#8721; (x - &#772;x)² * &#8721; (y - &#772;y)²</b></p><br>
Representado na programação da seguinte forma:<br>

```py
def formulaPearson(x, y):
    mediaX = np.average(x)
    mediaY = np.average(y)
    desvioX = []
    desvioY = []
    soma_produto_desvio = 0
    soma_quadrado_desvio = 0

    for i in range(len(x)):
        desvioX.append(x[i] - mediaX)
        desvioY.append(y[i] - mediaY)
    
    soma_produto_desvio = sum([a * b for a, b in zip(desvioX, desvioY)])
    soma_quadrado_desvio = sum([pow(a, 2) for a in desvioX]) * sum([pow(a, 2) for a in desvioY])
    soma_quadrado_desvio = sqrt(soma_quadrado_desvio)

    return soma_produto_desvio / soma_quadrado_desvio
```

</li>
</p>

<br>

<b><h3>III. Relacionamento</h3></b>
<p>
  Uma vez que o grau de semelhança é conhecido, multiplicamos o valor da avaliação pelo coeficiente Pearson de cada usuário nos cursos em que o <b>usuário alvo</b> também estudou e avaliou, obtendo a avaliação ponderada.<br>
  <blockquote>
    Se um curso X recebeu nota máxima de um usuário que possui baixa semelhança com o usuário alvo, este curso não é tão recomendável quanto parece. Um curso mal avaliado por um usuário muito semelhante ao usuário alvo tem mais valor (tende a ter).
  </blockquote>
  Após ter a matriz com as avaliações ponderadas pelo coeficiente Pearson, podemos somar quais cursos acumulam a melhor revisão de outros usuários. Os que tiverem melhor revisão (avaliação) serão os mais indicados a recomendação.
</p>

<br>

<b><h3>IV. Resultado</h3></b>
<p>
  Indivíduos de preferências semelhantes serão identificadas pelo modelo aqui desenvolvido. Essa informação será útil para sugerir os próximos conteúdos ao usuário alvo, mantendo-o cada vez mais ligado aos conteúdos oferecidos. Vale ressaltar que a cada recálculo da matriz, o grau de semelhança pode mudar e assim o algoritmo se adpata em tempo real às preferências do indivíduo.
</p>

<br><br>

<a href="https://sol.sbc.org.br/journals/index.php/reic/article/view/2144">
<p align="center">
  <b>Python, Inteligência Artificial, Algoritmo de Recomendação, Pearson.</b><br>
  Guilherme Donizetti - 2023.
</p></a>
