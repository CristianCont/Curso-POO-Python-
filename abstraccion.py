class Lavadora:
    def __init__(self):
        pass
    def lavar(self,temperatura='caliente'):
        self._llenar_tanque_agua(temperatura)
        self._añadir_javon()
        self._lavar()
        self._setrifugar()
    def _llenar_tanque_agua(self,temperatura):
        print(f'llenado el tanque con agua {temperatura}')
    def _añadir_javon(self):
        print('Añadiendo javon')
    def _lavar(self):
        print('Lavando la ropa')
    def _setrifugar(self):
        print('Centrifugando la ropa')

if __name__ == '__main__':
    lavadora1= Lavadora()
    lavadora1.lavar()