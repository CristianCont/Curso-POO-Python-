import random
def busqueda_lineal(lista, objetivo,cont=0):
    match= False
    print(f'pasos{cont}')
    for elemento in lista: #O(n)
        cont +=1
        print(f'pasos{cont}')
        if elemento == objetivo:
            match= True
            break
    return match

if __name__== '__main__':
    tamano_de_lista= int(input('de Que tamano sera la lista?'))
    objetivo= int(input('Que numero quieres importar'))
    lista =[random.randint(0,100) for i in range(tamano_de_lista)]
    encontramos= busqueda_lineal(lista,objetivo)
    print(lista)
    print(f'el elemento {objetivo} {"esta" if encontramos else "no esta"} ')