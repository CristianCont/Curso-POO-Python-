
def morral(tamaño, pesos, valores, n ):
    
    if n==0 or tamaño==0:
        return 0
    if pesos[n-1]> tamaño:
        return morral(tamaño,pesos,valores,n-1)

    return max(valores[n-1]+morral(tamaño-pesos[n-1],pesos,valores,n-1),
         morral(tamaño,pesos,valores,n-1))




if __name__=='__main__':
    valores = [60,100,120]
    pesos=[10,20,30]
    tamaño=50
    n= len(valores)

    resultado=morral(tamaño,pesos,valores,n)
    print(resultado)