#banco de dados para sistema multi-especialistas

class Cliente(object):
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
    
cliente = Cliente()
cliente.variaveis(4.29, 0.89, 150, 0.82, 4.29)
csm_diario = cliente.consumo_diario()
cliente_preco = cliente.tarifa()
cliente_pagamento = cliente.pagamento()
cliente_perfomance = cliente.performance()
cliente_irrad = cliente.irrad()
calculo = projeto_()
calculado = calculo.calculo(4.54, 4.29, 0.82)



