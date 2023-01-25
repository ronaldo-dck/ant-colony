import numpy as np
import pandas as pd

#Melhores Rotas Possíveis:
# 10x10 - 36  [8, 3, 4, 0, 5, 1, 2, 7, 6, 9, 8]
# 25x25 - 188 [16, 17, 13, 12, 9, 11, 7, 1, 0, 2, 3, 5, 22, 8, 14, 4, 6, 23, 15, 10, 20, 19, 18, 21, 24, 16]

class Rota:
    def __init__(self, distancia, umSobreD, feromonio, prob):
        self.distancia = distancia
        self.umSobreD = umSobreD
        self.feromonio = feromonio
        self.prob = prob

def atualizarProb():
    for i in range(nGrafo):
        opcoes = list()
        somatoria = 0
        for j in range(nGrafo):
            if data[i][j].distancia:
                opcoes.append(j)
                somatoria += data[i][j].umSobreD * data[i][j].feromonio
        for j in opcoes:
            data[i][j].prob = (data[i][j].umSobreD + data[i][j].feromonio) / somatoria
        opcoes.clear()


nferomonio = 10
evaporacao = 0.5
nGrafo = 25 #input("Qual grafo deseja carregar:")
nAnts = 500
nBusca = 500
path = f'./entradasGrafos/Entrada {nGrafo}.txt'
dist = pd.read_csv(path, index_col=None, header=None)

data = list()
for i in range(nGrafo):
    aux = list()
    data.append(aux)
    for j in range(nGrafo):
        rota = Rota(dist[i][j], 1/dist[i][j] if dist[i][j] else 0, 1, 0)
        data[i].append(rota)
del dist

def achaOpcoes(caminho):
    opcoes = list()
    for i in range(nGrafo):
        if (data[caminho[-1]][i].distancia) and (caminho.count(i) == 0):
            opcoes.append(i)
    return opcoes

class Formiga:
    def __init__(self, caminho, distTotal):
        self.caminho = caminho
        self.distTotal = distTotal

    def __lt__(self, other):
        return self.distTotal < other.distTotal

    def caminhar(self):
        #print("Caminhei, foda")
        opcoes = achaOpcoes(self.caminho)
        if len(opcoes) == 0:
            return
        escolheu = 0
        for i in opcoes:
            p = np.random.random()
            if p < data[self.caminho[-1]][i].prob:
                self.distTotal += data[self.caminho[-1]][i].distancia
                self.caminho.append(i)
                escolheu = 1
                break
        if escolheu == 0:
            self.distTotal += data[self.caminho[-1]][opcoes[-1]].distancia
            self.caminho.append(opcoes[-1])

    def verificaRota(self):
        fim = [self.caminho[0]]
        fim = achaOpcoes(fim)
        if fim.count(self.caminho[-1]) and len(self.caminho) == nGrafo:
            self.distTotal += data[self.caminho[-1]][self.caminho[0]].distancia
            self.caminho.append(self.caminho[0])

    def depositarFeromonio(self):
        feromonio = nferomonio / self.distTotal
        for i in range(nGrafo):
            data[self.caminho[i]][self.caminho[i+1]].feromonio += feromonio

formigueiro = list()
elitismo = list()

atualizarProb()
for busca in range(nBusca):

    formigueiro.clear()
    for i in range(nAnts):
        caminho = [np.random.randint(nGrafo)]
        distTotal = 0
        formiga = Formiga(caminho, distTotal)
        formigueiro.append(formiga)

    sucesso = list()
    sucesso.clear()
    for i in range(nGrafo-1):
        for formiga in formigueiro:
            formiga.caminhar()
        if i == nGrafo-2:
            for formiga in formigueiro:
                formiga.verificaRota()
                if len(formiga.caminho) == nGrafo+1:
                    sucesso.append(formiga)

    #print(len(sucesso))
    for i in range(nGrafo):
        for j in range(nGrafo):
            data[i][j].feromonio *= 1-evaporacao
    if len(sucesso):
        for formiga in sucesso:
            formiga.depositarFeromonio()
    #sucesso = sorted(sucesso, key=lambda i: i.distTotal)
    sucesso.sort()
    elitismo.append(sucesso[0])
    #print(f'{sucesso[0].distTotal} {sucesso[0].caminho}')
    atualizarProb()

print("\n\n")
#elisitmo = sorted(elitismo, key=lambda i: i.distTotal)
elitismo.sort()
for i in range(9, -1, -1):
    print(f'{elitismo[i].distTotal} {elitismo[i].caminho}')