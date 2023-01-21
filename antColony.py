import numpy as np
import pandas as pd

nGrafo = '10' #input("Qual grafo deseja carregar:")
path = './entradasGrafos/Entrada ' + nGrafo + '.txt'
#data = pd.read_csv(path, index_col=None, header=0, sep=' ', false_values=np.NaN)
data = pd.read_csv(path, index_col=None, header=None)

class Formiga:
    def __init__(self, caminho, distancia):
        self.caminho = caminho
        self.distancia = distancia

    # def caminhar(self):
    #     print("Caminhei, foda")

# caminho = [
#  """ linha """ [3], [4]
# ]


# matriz caminho = list()
# inteiro distancia = 0
# for linha
#    int possibilidades = 0
#    for coluna
#      se data[linha][coluna] != 0
#         possibilidades++
#    chance = 1/possibilidades * 100
#    for coluna
#      # possibilidades caminhos : chance% cada
#      aleatorio = 0 a 99
#      se aleatorio < chance
#        caminho.append([linha, coluna])
#        distancia += data[linha][coluna]
# formiga1 = Formiga(caminho, distancia)
# formigas.append(formiga1)


# formiga.caminhar()

# #formiga.caminhar()
# formigas.append(formiga)

# print(formigas[0].distancia)
# formigas.clear()
