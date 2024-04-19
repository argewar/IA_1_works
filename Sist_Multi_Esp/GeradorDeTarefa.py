import abc
import math

class Cliente(object):
    def __init__(self) -> None:
        pass
    def variaveis(self, kWh, preco, pay, pr, ir):
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
    
class Comercial(projeto_):
    def analista_(self, pot_mod, calculo_):
        self.pot_mod = pot_mod
        self.calculo_= calculo_
        return self.calculo_/self.pot_mod
    
cliente = Cliente()
cliente.variaveis(4.29, 0.89, 150, 0.82, 4.29)

analista = Comercial()
calculo = projeto_()
calculado = calculo.calculo(4.54, 4.29, 0.82)
analisado = analista.analista_(550/1000, calculado)
analisado = math.ceil(analisado)

class GeradorDeTarefa(object):
    def __init__(self, quadro_negro):
        self.QuadroNegro = quadro_negro

    def projeto(self):
        p = [calculado]
        return ["potência instalada (kWp): {:.4f}".format(p[0])]
    
    def potencia(self):
        q = [analisado]
        return ["número de módulos: {: }".format(q[0])]
    
    def adicionaTarefa(self):
        self.QuadroNegro.adicionaTarefa('projeto', self.projeto())
        self.QuadroNegro.adicionaTarefa('potencia', self.potencia())
        
