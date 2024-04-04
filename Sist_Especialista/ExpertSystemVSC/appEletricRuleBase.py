from esBooleanRuleBase import BooleanRuleBase
from esRuleVariable import RuleVariable
from esCondition import Condition
from esRule import Rule
from esClause import Clause

class RuleBaseVehicle:

    def __init__(self, nome, listaDeObjetivos):
        self.br = BooleanRuleBase(nome)
        self.lista_de_objetivos = listaDeObjetivos

    def get_goal_list(self):
        return self.lista_de_objetivos