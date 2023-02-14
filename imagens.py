from hiperparametros import PORCENTAGEM_IMAGENS
from math import floor
import matplotlib.pyplot as plt
import seaborn as sb
import data
import os

imgRate = floor(100 / PORCENTAGEM_IMAGENS) 

def limpaHistorico():
    """Exclui todas as imagens presentes na pasta 'Img'"""
    if os.path.isdir("./Img"):
        for arquivo in os.listdir("./Img/"):
            os.remove("./Img/" + arquivo)
    else:
        os.mkdir("Img")

def imgGeracao(busca):
    if busca%imgRate == 0:
        heatmap=sb.heatmap(data.feromonios, vmin=0, vmax=data.nBusca) 
        heatmap.set_title(f'{busca} - {data.inteligente[0].distTotal} == {data.inteligente[0].caminho}')
        imagem = heatmap.get_figure()
        imagem.savefig(f"Img/heatmap{busca}.png")
        plt.close()

def imgEvolucao(elitismo):
    valor = list()
    for i in range(len(elitismo)):
        valor.append(elitismo[i].distTotal)
    plt.plot(range(len(valor)), valor)
    plt.savefig("Img/Evolucao.jpg")
    plt.close()