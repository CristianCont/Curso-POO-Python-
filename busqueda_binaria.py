#Eficiente 
import random
def Busqueda_Binaria(lista, Comienzo, Final, Objetivo,con):
    con=1+con
    print(f'buscando{Objetivo} entre {lista[Comienzo]} y {lista[Final-1]} cuntos pasos {con}')
    if Comienzo> Final:
        return False
    medio =(Comienzo+Final)//2

    if lista[medio]==objetivo:
        return True
    elif lista[medio]< objetivo:
        return Busqueda_Binaria (lista,medio+1,Final, objetivo,con)
    elif lista[medio]> objetivo:
        return Busqueda_Binaria(lista,Comienzo,medio-1,objetivo,con)

if __name__== '__main__':
    con=0
    tamano_de_lista= int(input('de Que tamano sera la lista?'))
    objetivo= int(input('Que numero quieres importar'))
    lista =sorted([random.randint(0,100) for i in range(tamano_de_lista)])
    encontramos= Busqueda_Binaria(lista,0, len(lista),objetivo,con)
    print(lista)
    print(f'el elemento {objetivo} {"esta" if encontramos else "no esta"} ')