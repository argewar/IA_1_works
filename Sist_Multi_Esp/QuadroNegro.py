
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
                'progresso': 1
            },
            {
                'problema': 'material ',
                'instancias-de-problemas': [],
                'contribuicoes': [],
                'progresso': 2
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
        for prob in self.estadoCompartilhado:
            print('problema:', prob['problema'])
        print('instancias-de-problemas:', end='')
        for instancia in self.estadoCompartilhado[0]['instancias-de-problemas']:
            print(instancia, end='')
        for instancia in self.estadoCompartilhado[0]['contribuicoes']:
            print(instancia, end='')
        print('\n')
