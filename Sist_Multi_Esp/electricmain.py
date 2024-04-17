from BancoDados import Cliente
from QuadroNegro import QuadroNegro
from Controlador import Controlador
from GeradorDeTarefa import GeradorDeTarefa
from EngEletricista import EngEletricista
from AnaCom import AnaCom
from ComMat import ComMat


if __name__ == '__main__':

    quadro_negro = QuadroNegro()
    GeradorDeTarefa = GeradorDeTarefa(quadro_negro)

    quadro_negro.adicionaEspecialista( EngEletricista(quadro_negro) )
    #quadro_negro.adicionaEspecialista( AnaCom(quadro_negro) )
    #quadro_negro.adicionaEspecialista( ComMat(quadro_negro) )

    contribuicoes = Controlador(quadro_negro, GeradorDeTarefa, 1).loop()
        
    for x in contribuicoes:
        print(x[0])
        print('-'*50)
        print(x[1])