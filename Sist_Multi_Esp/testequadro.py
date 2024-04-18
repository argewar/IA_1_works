import random
import abc

class AbstractEspecialista(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, quadro_negro):
        self.QuadroNegro = quadro_negro

    @property
    def eh_ativado(self):
        raise NotImplementedError('Deve fornecer implementação na subclasse.')

    @property
    def expertise(self):
        raise NotImplementedError('Deve fornecer implementação na subclasse.')

    @property
    def progresso(self):
        raise NotImplementedError('Deve fornecer implementação na subclasse.')

    @abc.abstractmethod
    def contribui(self):
        raise NotImplementedError('Deve fornecer implementação na subclasse.')


class QuadroNegro(object):
    def __init__(self):
        self.especialistas = []
        self.estadoCompartilhado = [
            {
                'problema': 'projeto',
                'instancias-de-problemas': [],
                'contribuicoes': [],
                'progresso': 0
            }
        ]

    def adicionaEspecialista(self, especialista):
        self.especialistas.append(especialista)

    def adicionaContribuicao(self, contribuicao):
        self.estadoCompartilhado[0]['contribuicoes'] += contribuicao

    def atualizaProgresso(self, progresso):
        self.estadoCompartilhado[0]['progresso'] += progresso

    def adicionaTarefa(self, tarefa, parametros):
        self.estadoCompartilhado[0]['instancias-de-problemas'] = parametros

    def pegaTarefa(self, tarefa):
        return self.estadoCompartilhado[0]['instancias-de-problemas']

    def mostraTarefas(self):
        print('problema:', self.estadoCompartilhado[0]['problema'])
        print('instancias-de-problemas:')
        for instancia in self.estadoCompartilhado[0]['instancias-de-problemas']:
            print(instancia)



class GeradorDeTarefa(object):
    def __init__(self, quadro_negro):
        self.QuadroNegro = quadro_negro

    def projeto(self):
        p = ()
        return p  # Ex: p = [14, 34]

    def adicionaTarefa(self):
        self.QuadroNegro.adicionaTarefa('projeto', self.projeto())


class EngEletricista(AbstractEspecialista):
    def __init__(self, quadro_negro):
        self.QuadroNegro = quadro_negro

    @property
    def eh_ativado(self):
        if 'projeto' in [problema['problema'] for problema in self.QuadroNegro.estadoCompartilhado]:
            return True
        else:
            return False

    @property
    def expertise(self):
        p = self.QuadroNegro.pegaTarefa('projeto')
        return 'projeto', p

    @property
    def progresso(self):
        return random.randint(1, 5)

    def contribui(self):
        self.QuadroNegro.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.QuadroNegro.atualizaProgresso(self.progresso)


# Controla o acesso de cada especialista ao quadro-negro para pegar uma tarefa da
# lista 'instancias-de-problemas', chama cada especialista a contribuir e
# adiciona o resultado/contribuição na lista de contribuições do quadro-negro.
class Controlador(object):
    def __init__(self, quadro_negro, GeradorDeTarefa, limite=1):
        self.QuadroNegro = quadro_negro
        self.GeradorDeTarefa = GeradorDeTarefa
        self.limite = limite    # limite para interromper a função loop

    def loop(self):
        while self.QuadroNegro.estadoCompartilhado[0]['progresso'] < self.limite:
            self.GeradorDeTarefa.adicionaTarefa()   # gera e adiciona tarefas no quadro-negro
            self.QuadroNegro.mostraTarefas()        # mostra a lista de tarefas a resolver
            for especialista in self.QuadroNegro.especialistas:
                if especialista.eh_ativado:         # testa se o especialista está ativo
                    especialista.contribui()        # chama o especialista a contribuir.
        # retorna todas as contribuições postadas no quadro-negro pelos especialistas.
        return self.QuadroNegro.estadoCompartilhado[0]['contribuicoes']


if __name__ == '__main__':
    quadro_negro = QuadroNegro()
    GeradorDeTarefa = GeradorDeTarefa(quadro_negro)

    quadro_negro.adicionaEspecialista(EngEletricista(quadro_negro))

    contribuicoes = Controlador(quadro_negro, GeradorDeTarefa, 1).loop()

    for x in contribuicoes:
        print(x[0])
        print('-' * 50)
        print(x[1])
