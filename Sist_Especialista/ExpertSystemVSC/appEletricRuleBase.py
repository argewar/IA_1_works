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
        problema_eletrico = RuleVariable(self.br, "problema_eletrico")
        problema_eletrico.set_labels("iluminacao tomada comum tomada especifica")
        problema_eletrico.set_prompt_text("qual falha eletrica o comodo está apresentando?{iluminacao tomada comum tomada especifica}")

        quantas_teclas = RuleVariable(self.br, "quantas_teclas")
        quantas_teclas.set_labels("uma tecla duas teclas tres teclas")
        quantas_teclas.set_prompt_text("este interruptor possui mais de uma tecla?{sim nao}")

        acionamento = RuleVariable(self.br, "acionamento")
        acionamento.set_labels("um ponto dois pontos tres pontos")
        acionamento.set_prompt_text("este interruptor aciona a mesma lampada em mais de um local?{sim nao}")

        tomada_int = RuleVariable(self.br, "tomada_int")
        tomada_int.set_labels("interruptor com tomada")
        tomada_int.set_prompt_text("este interruptor possui tomada no mesmo modulo?{sim nao}")

        ligacao = RuleVariable(self.br, "ligacao")
        ligacao.set_labels("liga duas lampadas")
        ligacao.set_prompt_text("liga mais de uma lampada juntas?{sim nao}")

        c_equals = Condition("=")
        c_not_equals = Condition("!=")
        c_less_than = Condition("<")

        int_simples = Rule(self.br, "int_simples", [
            Clause(quantas_teclas, c_equals, "nao"),
            Clause(acionamento, c_equals, "nao"),
            Clause(ligacao, c_equals, "nao"),
            Clause(tomada_int, c_equals, "nao")
        ], Clause(problema_eletrico, c_equals, "Interruptor Simples\n"))

        int_duplo = Rule(self.br, "int_duplo", [
            Clause(quantas_teclas, c_equals, "sim"),
            Clause(acionamento, c_equals, "nao"),
            Clause(ligacao, c_equals, "sim"),
            Clause(tomada_int, c_equals, "nao")
        ], Clause(problema_eletrico, c_equals, "Interruptor Duplo\n"))
        #print("Abrir modulo, verificar Fase e Retorno, checar soquete"))

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
        self.br.set_variable_value("interruptor", None)
        self.br.set_variable_value("quantas_teclas", None)
        self.br.set_variable_value("acionamento", None)
        self.br.set_variable_value("ligacao", None)
        self.br.set_variable_value("tomada_int", None)
        self.br.display_variables(LOG)
