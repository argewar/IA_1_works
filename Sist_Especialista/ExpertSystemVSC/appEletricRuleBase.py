from esBooleanRuleBase import BooleanRuleBase
from esRuleVariable import RuleVariable
from esCondition import Condition
from esRule import Rule
from esClause import Clause

class RuleBaseEletric:

    def __init__(self, nome, listaDeObjetivos):
        self.br = BooleanRuleBase(nome)
        self.lista_de_objetivos = listaDeObjetivos

    def get_goal_list(self):
        return self.lista_de_objetivos
    
    def create(self):
        #regras e variáveis para problema iluminção
        #trabalhar problemas nos tipos de interruptores (simples, duplo, triplo, paralelo)

        problema_iluminacao = RuleVariable(self.br, "iluminacao")
        problema_iluminacao.set_labels("problema eletrico na iluminacao")
        problema_iluminacao.set_prompt_text("qual falha eletrica a iluminacao esta apresentando?{iluminacao }")

        tp_interruptor = RuleVariable(self.br, "tp_interruptor")
        tp_interruptor.set_labels("simples duplo paralelo")
        tp_interruptor.set_prompt_text("qual tipo de interruptor? {simples duplo paralelo}")

        tr_iluminacao = RuleVariable(self.br, "tr_iluminacao")
        tr_iluminacao.set_labels("troca da iluminacao")
        tr_iluminacao.set_prompt_text("lampada ja foi trocada? {sim nao}")

        qt_teclas = RuleVariable(self.br, "qt_teclas")
        qt_teclas.set_labels("qtd teclas do modulo")
        qt_teclas.set_prompt_text("quantas teclas possue o interruptor? {1 2 3}")

        ac_iluminacao = RuleVariable(self.br, "ac_iluminacao")
        ac_iluminacao.set_labels("acionamento iluminacao")
        ac_iluminacao.set_prompt_text("interruptor aciona mais de uma iluminacao? {sim nao}")
                      
        ac_ponto = RuleVariable(self.br, "ac_ponto")
        ac_ponto.set_labels("ponto iluminacao")
        ac_ponto.set_prompt_text("interrutor aciona mesma iluminacao em pontos distintos? {sim nao}")

        ac_tensao = RuleVariable(self.br, "ac_tensao")
        ac_tensao.set_labels("teste de tensao fase")
        ac_tensao.set_prompt_text("existe tensao na fase do interruptor? {sim nao}")

        cb_conect = RuleVariable(self.br, "cb_conect")
        cb_conect.set_labels("conexão do cabo")
        cb_conect.set_prompt_text("cabos conectados corretamente fase e retorno? {sim nao}")
                   
        c_equals = Condition("=")
        c_not_equals = Condition("!=")
        c_less_than = Condition("<")

        Regra01 = Rule(self.br, "simples", [
            Clause(tp_interruptor, c_equals, "simples"),
            Clause(tr_iluminacao, c_equals, "sim"),
            Clause(qt_teclas, c_equals, "1"),
            Clause(ac_iluminacao, c_equals, "nao"),
            Clause(ac_ponto, c_equals, "nao"),
            Clause(ac_tensao, c_equals, "sim"),
            Clause(cb_conect, c_equals, "sim")
        ], Clause(problema_iluminacao, c_equals, "verificar entrada de retorno e neutro iluminacao\n"))

        Regra02 = Rule(self.br, "simples", [
            Clause(tp_interruptor, c_equals, "simples"),
            Clause(tr_iluminacao, c_equals, "sim"),
            Clause(qt_teclas, c_equals, "1"),
            Clause(ac_iluminacao, c_equals, "sim"),
            Clause(ac_ponto, c_equals, "nao"),
            Clause(ac_tensao, c_equals, "sim"),
            Clause(cb_conect, c_equals, "sim")
        ], Clause(problema_iluminacao, c_equals, "verificar retorno e neutro das lampadas\n"))

        return self.br
    
    #def demo_fc(self, LOG):
        #LOG.append("\n --- Ajustando valores para Tipo de problema eletrico para demo BackwardChain ---")
        #self.br.set_variable_value("iluminacao", None)
        #self.br.set_variable_value("quantas_teclas", "nao")
        #self.br.set_variable_value("acionamento", "nao")
        #self.br.set_variable_value("ligacao", "nao")
        #self.br.set_variable_value("tomada_int", "nao")
        #self.br.display_variables(LOG)
    
    def demo_bc(self, LOG):
        LOG.append("\n --- Ajustando valores para Tipo de problema eletrico para demo BackwardChain ---")
        self.br.set_variable_value("tp_interruptor", None)
        self.br.set_variable_value("tr_iluminacao", None)
        self.br.set_variable_value("qt_teclas", None)
        self.br.set_variable_value("ac_iluminacao", None)
        self.br.set_variable_value("ac_ponto", None)
        self.br.set_variable_value("ac_tensao", None)
        self.br.set_variable_value("cb_conect", None)
        self.br.display_variables(LOG)
