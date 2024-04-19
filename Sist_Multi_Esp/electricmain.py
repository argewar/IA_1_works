from BancoDados import Cliente
from QuadroNegro import QuadroNegro
from Controlador import Controlador
from GeradorDeTarefa import GeradorDeTarefa
from EngEletricista import EngEletricista
from OutroEspecialista import AnalistaComercial
from Outro2Especialista import AnalistaMaterial


if __name__ == '__main__':
    cliente = Cliente.__init__(4.29, 0.89, 990, 0.82, 4.29)
    quadro_negro = QuadroNegro()
    GeradorDeTarefa = GeradorDeTarefa(quadro_negro)

    quadro_negro.adicionaEspecialista(EngEletricista(quadro_negro))
    quadro_negro.adicionaEspecialista(AnalistaComercial(quadro_negro))
    quadro_negro.adicionaEspecialista(AnalistaMaterial(quadro_negro))
    
    contribuicoes = Controlador(quadro_negro, GeradorDeTarefa, 1).loop()

    for x in contribuicoes:
        print('-' * 50)
        print(x[0])
        if isinstance(x[1], list):  # Verifica se x[1] é uma lista
            for item in x[1]:
                print(item)
        else:
            print(x[1])