

from QuadroNegro import QuadroNegro
from Controlador import Controlador
from GeradorDeTarefa import GeradorDeTarefa
from Aluno import Aluno
from Estudante import Estudante
from Professor import Professor
from SuperAluno import SuperAluno
from SuperEstudante import SuperEstudante

if __name__ == '__main__':

    quadro_negro = QuadroNegro()
    GeradorDeTarefa = GeradorDeTarefa(quadro_negro)

    quadro_negro.adicionaEspecialista( Aluno(quadro_negro) )
    quadro_negro.adicionaEspecialista( Estudante(quadro_negro) )
    quadro_negro.adicionaEspecialista( Professor(quadro_negro) )

    quadro_negro.adicionaEspecialista( SuperAluno(quadro_negro) )
    quadro_negro.adicionaEspecialista( SuperEstudante(quadro_negro) )

    contribuicoes = Controlador(quadro_negro, GeradorDeTarefa, 120).loop()

    for x in contribuicoes:
        print(x)
