import numpy as np
import hiperparametros as hp
import data
import Formiga

import matplotlib.pyplot as mp 
import seaborn as sb 

formigueiro = list()
elitismo = list()

for busca in range(data.nBusca):

    for i in range(data.nGrafo):
        distTotal = 0
        formiga = Formiga.Formiga(i, distTotal)
        formigueiro.append(formiga)

    for formiga in formigueiro:
        formiga.viagem()
        
    data.feromonios *= 1-hp.EVAPORACAO

    for formiga in formigueiro:
        if formiga.distTotal:
            formiga.depositarFeromonio()

    formigueiro.clear()
    data.inteligente.sort()
    elitismo.append(data.inteligente[0])
    data.inteligente.clear()



valor = list()
for i in range(len(elitismo)):
    valor.append(elitismo[i].distTotal)
mp.plot(range(len(valor)), valor)
mp.show()
mp.close()


elitismo.sort()
print(elitismo[0].distTotal)

heatmap=sb.heatmap(data.feromonios, annot=False) 
heatmap.set_title(f'{elitismo[0].distTotal} == {elitismo[0].caminho}')

#mp.show()
imagem = heatmap.get_figure()
imagem.savefig("Img/heatmap.png")



