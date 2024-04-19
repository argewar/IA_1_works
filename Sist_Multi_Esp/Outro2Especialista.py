import random
from AbstractEspecialista import AbstractEspecialista

class AnalistaMaterial(AbstractEspecialista):
    def __init__(self, quadro_negro):
        self.QuadroNegro = quadro_negro

    @property
    def eh_ativado(self):
        if 'material ' in [problema['problema'] for problema in self.QuadroNegro.estadoCompartilhado]:
            return True
        else:
            return False

    @property
    def expertise(self):
        c = self.QuadroNegro.pegaTarefa('material ')
        return 'material ', c

    @property
    def progresso(self):
        return random.randint(1, 5)

    def contribui(self):
        self.QuadroNegro.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.QuadroNegro.atualizaProgresso(self.progresso)