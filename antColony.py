import hiperparametros as hp
import data
from Formiga import Formiga
import imagens


imagens.limpaHistorico()

formigueiro = list()
elitismo = list()

for busca in range(data.nBusca):

    for i in range(data.nGrafo):
        distTotal = 0
        formiga = Formiga(i, distTotal)
        formigueiro.append(formiga)

    for formiga in formigueiro:
        formiga.viagem()
        
    data.feromonios *= 1-hp.EVAPORACAO

    for formiga in formigueiro:
        if formiga.distTotal:
            formiga.depositarFeromonio()

    formigueiro.clear()
    data.inteligente.sort()

    imagens.imgGeracao(busca)
    elitismo.append(data.inteligente[0])
    data.inteligente.clear()


imagens.imgEvolucao(elitismo)
elitismo.sort()
print(elitismo[0].distTotal, end=' - ')
print(elitismo[0].caminho)

def caminhovalido(caminho):
    soma = 0
    for i in range(len(caminho)-1):
        print(data.dist[caminho[i]][caminho[i+1]], end=' ')
        soma += data.dist[caminho[i]][caminho[i+1]]
    return soma

caminhovalido(elitismo[0].caminho)