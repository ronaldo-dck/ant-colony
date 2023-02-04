import numpy as np
import pandas as pd

# Melhores Rotas Possíveis:
# 10x10 - 36  [8, 3, 4, 0, 5, 1, 2, 7, 6, 9, 8]
# 25x25 - 188 [16, 17, 13, 12, 9, 11, 7, 1, 0, 2, 3, 5, 22, 8, 14, 4, 6, 23, 15, 10, 20, 19, 18, 21, 24, 16]

maxTentativa = 10
nferomonio = 0.1
evaporacao = 0.01
Q = 10 
ALPHA = 1
BETA = 1
nGrafo = 10  # input("Qual grafo deseja carregar:")
nBusca = 10

path = f'./Grafos/Entrada {nGrafo}.txt'
dist = np.loadtxt(path, skiprows=1)


tau = np.where(dist, 1/dist, 0)
feromonios = np.where(dist, nferomonio, 0)


inteligente = list()



class Formiga:

    def __init__(self, inicio, distTotal):
        self.inicio = inicio
        self.caminho = [inicio]
        self.distTotal = distTotal

    def __lt__(self, other):
        return self.distTotal < other.distTotal

    def achaOpcoes(self, caminho):
        opcoes = list()
        for i in range(nGrafo):
            if (dist[caminho[-1]][i]) and (caminho.count(i) == 0):
                opcoes.append(i)
        return opcoes

    def atualizarProb(self, opcoes):
        probabilidades = list()
        somatoria = 0
        for j in opcoes:
            somatoria += tau[self.caminho[-1]][j] * feromonios[self.caminho[-1]][j]
        for j in opcoes:
            prob = (tau[self.caminho[-1]][j] * feromonios[self.caminho[-1]][j]) / somatoria
            probabilidades.append(prob)
        
        return probabilidades

    def passo(self):
        opcoes = self.achaOpcoes(self.caminho)

        if len(opcoes) == 0:
            self.caminho.clear()
            self.caminho.append(self.inicio)
            return 1 

        escolha = np.random.choice(opcoes, p=self.atualizarProb(opcoes))
        self.distTotal += dist[self.caminho[-1]][escolha]
        self.caminho.append(escolha)
        return 0

    def viagem(self, tentativa=0):

        while len(self.caminho) < nGrafo and tentativa < maxTentativa:
            if self.passo():
                tentativa += 1

                
        if self.verificaRota():
            print("pré")
            print(self.caminho)
            inteligente.append(self)
            print("pós")
            print(self.caminho)
            self.depositarFeromonio()



    def depositarFeromonio(self):
        feromonio = Q / self.distTotal
        for i in range(nGrafo):
            feromonios[self.caminho[i]][self.caminho[i+1]] += feromonio

    def verificaRota(self):
        i = self.caminho[0]
        f = self.caminho[-1]
        #fim = [i]


        #opcao = self.achaOpcoes(fim)
        if dist[i][f] and len(self.caminho) == nGrafo:
            print(dist[i][f], i, f, self.caminho[0])
            self.distTotal += dist[f][i]
            self.caminho.append(self.caminho[0])
            return True
        else:
            return False

formigueiro = list()

for busca in range(10):


    for i in range(nGrafo):
        distTotal = 0
        formiga = Formiga(i, distTotal)
        formigueiro.append(formiga)


    for formiga in formigueiro:
        formiga.viagem()

    feromonios *= 1-evaporacao

print()
print(len(inteligente))
for i in range(len(inteligente)):
    print(i, inteligente[i].caminho)
inteligente.sort()
print(inteligente[-1].distTotal)
print(inteligente[0].distTotal)
