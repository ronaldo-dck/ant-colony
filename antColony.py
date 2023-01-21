import numpy as np
import pandas as pd

nGrafo = 10 #input("Qual grafo deseja carregar:")
path = f'./entradasGrafos/Entrada {nGrafo}.txt'
#data = pd.read_csv(path, index_col=None, header=0, sep=' ', false_values=np.NaN)
data = pd.read_csv(path, index_col=None, header=None)


# teste = np.zeros((nGrafo,nGrafo))
# print(teste[1])

# teste[1][2] = 7

# print(teste[1])


class Rotas:
    def __init__(self, distancia, umSobreD, feromonio):
        self.distancia = distancia
        self.umSobreD = umSobreD
        self.feromonio = feromonio

teste = list()
for i in range(nGrafo):
    aux = list()
    teste.append(aux)
    for j in range(nGrafo):
        teste[i].append(0)
        
for i in range(nGrafo):
    for j in range(nGrafo):
        rota = Rotas(data[i][j], 1/data[i][j] if data[i][j] else 0, 1)
        teste[i][j] = rota
        
print(teste[0][3].distancia)
print(teste[0][4].distancia)


class Formiga:
    def __init__(self, caminho, distancia):
        self.caminho = caminho
        self.distancia = distancia

    # def caminhar(self):
    #     print("Caminhei, foda")

# caminho = [
#  """ linha """ [3], [4]
# ]

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
