import numpy as np
import pandas as pd

class Rotas:
    def __init__(self, distancia, umSobreD, feromonio):
        self.distancia = distancia
        self.umSobreD = umSobreD
        self.feromonio = feromonio

nGrafo = 10 #input("Qual grafo deseja carregar:")
nAnts = 10
path = f'./entradasGrafos/Entrada {nGrafo}.txt'
dist = pd.read_csv(path, index_col=None, header=None)

data = list()
for i in range(nGrafo):
    aux = list()
    data.append(aux)
    for j in range(nGrafo):
        rota = Rotas(dist[i][j], 1/dist[i][j] if dist[i][j] else 0, 1)
        data[i].append(rota)
del dist

class Formiga:
    def __init__(self, caminho, distTotal):
        self.caminho = caminho
        self.distTotal = distTotal

    def caminhar(self):
        print("Caminhei, foda")
        opcoes = list()
        for i in range(nGrafo):
            if data[self.caminho[-1][0]][i]:
                opcoes.append(i)
                #isso aq tá fazendo com que toda a vez q a formiga caminhe ela sempre vai pegar as possibilidades com base no último lugar q ela tá
                # dessa maneira toda vez q ela caminha ela faz a entrada desse número em 2 pontos ao mesmo tempo:
                # matriz caminho: [[0,0]] <-inicial
                # matriz caminho: [[0,x], [x]] <-escolheu o caminho x a partir do inicial
                # matriz caminho: [[0,x], [x, y], [y]] <-escolheu o caminho y a partir do x
                #....


popInicial = list()
for i in range(nAnts):
    caminho = [[0, 0]]
    distTotal = 0
    formiga = Formiga(caminho, distTotal)
    popInicial.append(formiga)

for formiga in popInicial:
    formiga.caminha()
# formiga1 = Formiga(null, null)
# formigas.append(formiga1)
# matriz caminho = list()
# inteiro distancia = 0
# for linha
#    int possibilidades = 0
#    opcoes = list()
#    for coluna
#      se data[linha][coluna] != 0
#         possibilidades++
#         opcoes.append([linha, coluna])
#    chance = 1/possibilidades * 100
#    # possibilidades caminhos : chance% cada
#    for i in possibilidades
#      aleatorio = 0 a 99
#      se aleatorio < chance
#         caminho.append(opcoes[i])
#         distancia += data[opcoes[i][0]][opcoes[i][1]]
#         break

# formiga.caminhar()

# #formiga.caminhar()
# formigas.append(formiga)

# print(formigas[0].distancia)
# formigas.clear()