class Automovil:
    def __init__(self, modelo,marca,color):
        self.modelo=modelo
        self.marca=marca
        self.color=color
        self._estado='en reposo'
        self._motor=Motor(cilindros=4)
    def Acelerar(self,tipo='Despacio'):
        if tipo =='Rapida':
            self._motor.Inyecta_gasolina(10)
        else:
            self._motor.Inyecta_gasolina(3)
        self._estado='movimiento'



class Motor:
    def __init__(self,cilindros,tipo='Gasolina') :
        self.cilindros=cilindros
        self.tipo=tipo
        self._temperatura=0
    def Inyecta_gasolina(self,cantidad):
        pass    