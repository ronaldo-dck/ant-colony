import hiperparametros as hp
import numpy as np

nGrafo = int(input("Digite o grafo desejado: "))
nBusca = int(input("Digite o número de buscas: "))
path = f'./Grafos/Entrada {nGrafo}.txt'
dist = np.loadtxt(path, skiprows=1)

tau = np.where(dist, 1/dist, 0)
feromonios = np.where(dist, hp.N_FEROMONIO, 0)

inteligente = list()