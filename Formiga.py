import hiperparametros as hp
from numpy.random import choice
import numpy as np
import data


class Formiga:

    def __init__(self, inicio, distTotal):
        self.inicio = inicio
        self.caminho = [inicio]
        self.node_atual = inicio
        self.distTotal = distTotal

    def __lt__(self, other):
        return self.distTotal < other.distTotal

    def achaOpcoes(self):
        #preenche possiveis com os indices dos caminhos existentes
        possiveis = np.asarray(data.dist[self.node_atual]).nonzero()
        #checa quais desses caminhos não foram visitados, trocando o índice por -1 caso foi
        possiveis = np.where(np.isin(possiveis, self.caminho, invert=True), possiveis, -1)
        #mantém em possiveis apenas os valores válidos
        possiveis = possiveis[np.where(possiveis != -1)]

    

        return possiveis

    def atualizarProb(self, opcoes):
        somatoria = 0

        somatoria = np.sum(data.tau[self.caminho[-1]][opcoes]**hp.ALPHA *
                           data.feromonios[self.caminho[-1]][opcoes]**hp.BETA)
        
        probabilidades = (data.tau[self.caminho[-1]][opcoes]**hp.ALPHA *
                          data.feromonios[self.caminho[-1]][opcoes]**hp.BETA) / somatoria

        return probabilidades


    def passo(self):
        opcoes = self.achaOpcoes()

        if len(opcoes) == 0:
            self.caminho.clear()
            self.caminho.append(self.inicio)
            self.distTotal = 0
            self.node_atual = self.inicio
            return 1

        escolha = choice(opcoes, p=self.atualizarProb(opcoes))
        
        self.distTotal += data.dist[self.node_atual][escolha]
        self.node_atual = escolha

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

        if data.dist[self.node_atual][self.inicio] and len(self.caminho) == data.nGrafo:
            self.distTotal += data.dist[self.node_atual][self.inicio]
            self.caminho.append(self.caminho[0])
            return True
        else:
            self.distTotal = False
            return False
