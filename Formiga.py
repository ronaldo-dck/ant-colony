import hiperparametros as hp
from numpy.random import choice 
import data


class Formiga:

    def __init__(self, inicio, distTotal):
        self.inicio = inicio
        self.caminho = [inicio]
        self.distTotal = distTotal

    def __lt__(self, other):
        return self.distTotal < other.distTotal

    def achaOpcoes(self, caminho):
        opcoes = list()
        for i in range(data.nGrafo):
            if (data.dist[caminho[-1]][i]) and (caminho.count(i) == 0):
                opcoes.append(i)
        return opcoes

    def atualizarProb(self, opcoes):
        probabilidades = list()
        somatoria = 0
        for j in opcoes:
            somatoria += data.tau[self.caminho[-1]][j]**hp.ALPHA * \
                data.feromonios[self.caminho[-1]][j]**hp.BETA
        for j in opcoes:
            prob = (data.tau[self.caminho[-1]][j]**hp.ALPHA *
                    data.feromonios[self.caminho[-1]][j]**hp.BETA) / somatoria
            probabilidades.append(prob)

        return probabilidades

    def passo(self):
        opcoes = self.achaOpcoes(self.caminho)

        if len(opcoes) == 0:
            self.caminho.clear()
            self.caminho.append(self.inicio)
            self.distTotal = 0
            return 1

        escolha = choice(opcoes, p=self.atualizarProb(opcoes))
        self.distTotal += data.dist[self.caminho[-1]][escolha]
        self.caminho.append(escolha)
        return 0

    def viagem(self, tentativa=0):

        while len(self.caminho) < data.nGrafo and tentativa < hp.MAX_TENTATIVA:
            if self.passo():
                tentativa += 1

        if self.verificaRota():
            data.inteligente.append(self)

    def depositarFeromonio(self):
        feromonio = hp.Q / self.distTotal
        for i in range(data.nGrafo):
            data.feromonios[self.caminho[i]][self.caminho[i+1]] += feromonio

    def verificaRota(self):
        i = self.caminho[0]
        f = self.caminho[-1]

        if data.dist[f][i] and len(self.caminho) == data.nGrafo:
            self.distTotal += data.dist[f][i]
            self.caminho.append(self.caminho[0])
            return True
        else:
            self.distTotal = False
            return False
