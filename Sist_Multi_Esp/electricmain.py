from BancoDados import Cliente
from QuadroNegro import QuadroNegro
from Controlador import Controlador
from GeradorDeTarefa import GeradorDeTarefa
from EngEletricista import EngEletricista
from OutroEspecialista import AnalistaComercial
from ComMat import ComMat


if __name__ == '__main__':
    cliente = Cliente()
    quadro_negro = QuadroNegro()
    GeradorDeTarefa = GeradorDeTarefa(quadro_negro)

    quadro_negro.adicionaEspecialista(EngEletricista(quadro_negro))
    quadro_negro.adicionaEspecialista(AnalistaComercial(quadro_negro))
    
    contribuicoes = Controlador(quadro_negro, GeradorDeTarefa, 1).loop()

    for x in contribuicoes:
        print('-' * 50)
        print(x[0])
        if isinstance(x[1], list):  # Verifica se x[1] é uma lista
            for item in x[1]:
                print(item)
        else:
            print(x[1])