import random
import abc

class Cliente(object):
    def __init__(self, kWh, preco, pay, pr, ir):
        self.kWh = kWh
        self.preco = preco
        self.pay = pay
        self.pr = pr
        self.ir = ir
    
    def consumo_diario(self):
        return self.kWh
    
    def tarifa(self):
        return self.preco
    
    def pagamento(self):
        return self.pay
    
    def performance(self):
        return self.pr
    
    def irrad(self):
        return self.ir

class projeto_(Cliente):
    def calculo(self, consumo, irrad, performance):
        self.performance = performance
        self.irrad = irrad
        self.consumo_diario = consumo
        return (self.consumo_diario/self.irrad)/self.performance

class GeradorDeTarefa(object):
    def __init__(self, quadro_negro):
        self.QuadroNegro = quadro_negro

    def projeto(self):
        calculado = projeto_()
        p = [calculado]
        return ["potência instalada (kWp): {:.4f}".format(p[0])]
    
    def potencia(self):
        calculado = projeto_()
        q = [calculado]
        return q
    
    def adicionaTarefa(self):
        self.QuadroNegro.adicionaTarefa('projeto', self.projeto())
        self.QuadroNegro.adicionaTarefa('potencia', self.potencia())

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
            },
            {
                'problema': 'potencia',
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
        if tarefa not in self.estadoCompartilhado[0]['instancias-de-problemas']:
            self.estadoCompartilhado[0]['instancias-de-problemas'].append(parametros)

    def pegaTarefa(self, tarefa):
        return self.estadoCompartilhado[0]['instancias-de-problemas'].pop(0)

    def mostraTarefas(self):
        print('problema:', self.estadoCompartilhado[0]['problema'])
        print('instancias-de-problemas:', end=' ')
        for instancia in self.estadoCompartilhado[0]['instancias-de-problemas']:
            print(instancia, end=' ')
        print('\n')

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

class EngenheiroFotovoltaico(AbstractEspecialista):
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

class PesquisadorMateriaisFotovoltaicos(AbstractEspecialista):
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

class EngenheiroControleSolar(AbstractEspecialista):
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

if __name__ == '__main__':
    cliente = Cliente(4.29, 0.89, 150, 0.82, 4.29)
    quadro_negro = QuadroNegro()
    GeradorDeTarefa = GeradorDeTarefa(quadro_negro)

    quadro_negro.adicionaEspecialista(EngenheiroFotovoltaico(quadro_negro))
    quadro_negro.adicionaEspecialista(PesquisadorMateriaisFotovoltaicos(quadro_negro))
    quadro_negro.adicionaEspecialista(EngenheiroControleSolar(quadro_negro))
    
    contribuicoes = Controlador(quadro_negro, GeradorDeTarefa, 1).loop()

    for x in contribuicoes:
        print(x[0])
        print('-' * 50)
        if isinstance(x[1], list):  # Verifica se x[1] é uma lista
            for item in x[1]:
                print(item)
        else:
            print(x[1])
