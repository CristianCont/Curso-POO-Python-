class Cordenada:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def Distancia(self,Cordenada):
        x_diff= (self.x - Cordenada.x)**2
        y_diff= (self.y-Cordenada.y)**2

        return(x_diff+y_diff)**0.5


if __name__ == '__main__':
    Cordenada1= Cordenada(3,30)
    cordenada2= Cordenada(4,8)

    print(Cordenada1.Distancia(cordenada2))
    print(isinstance(cordenada2,Cordenada))
