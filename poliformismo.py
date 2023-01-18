class Persona:
    def __init__(self,nombre):
        self.nombre=nombre
    
    def Avanza(self):
        print('Ando Caminando Con un fluw violento')
    
class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    def Avanza(self):
        print('estoy pedaliando de mi bicicleta')
def main():
     persona=Persona('juan')
     persona.Avanza()
     ciclista=Ciclista('manuel')
     ciclista.Avanza()
if __name__ == '__main__':
    main()