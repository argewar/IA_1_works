
class QuadroNegro(object):
    def __init__(self):
        self.especialistas = []
        self.estadoCompartilhado = [
            {
                'problema': 'projeto ',
                'instancias-de-problemas': [],
                'contribuicoes': [],
                'progresso': 0
            },
            {
                'problema': 'analise ',
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
        for i in range(2):
            print('problema:', self.estadoCompartilhado[i]['problema'])
        print('instancias-de-problemas:', end='')
        for instancia in self.estadoCompartilhado[0]['instancias-de-problemas']:
            print(instancia, end='')
        print('\n')
