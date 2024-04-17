import random
from AbstractEspecialista import AbstractEspecialista

# Aluno 'é-um' AbstractEspecialista
class EngEletricista(AbstractEspecialista):

    # Testa se a especialidade do 'Aluno' está presente na lista de problemas a serem resolvidos
    @property
    def eh_ativado(self):
        if 'projeto' in self.QuadroNegro.estadoCompartilhado['problemas']:
            return True
        else:
            return False

    # implementação da expertise do 'Aluno'; como ele realiza sua tarefa
    @property
    def expertise(self):
        p = self.QuadroNegro.pegaTarefa('projeto')
        return 'projeto', p

    # Quanto a realização da tarefa so Aluno contribui com o avanço geral da solução do problema.
    @property
    def progresso(self):
        print("oi")
        return random.randint(1, 5)


    # Atualiza o quadro-negro com a contribuição do 'Aluno'
    def contribui(self):
        self.QuadroNegro.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.QuadroNegro.atualizaProgresso(self.progresso)