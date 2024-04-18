import random
from AbstractEspecialista import AbstractEspecialista

# Aluno 'é-um' AbstractEspecialista
class EngEletricista(AbstractEspecialista):
    def __init__(self, quadro_negro):
        self.QuadroNegro = quadro_negro

    @property
    def eh_ativado(self):
        if 'projeto ' in [problema['problema'] for problema in self.QuadroNegro.estadoCompartilhado]:
            return True
        else:
            return False

    @property
    def expertise(self):
        p = self.QuadroNegro.pegaTarefa('projeto ')
        return 'projeto ', p

    @property
    def progresso(self):
        return random.randint(1, 5)

    def contribui(self):
        self.QuadroNegro.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.QuadroNegro.atualizaProgresso(self.progresso)