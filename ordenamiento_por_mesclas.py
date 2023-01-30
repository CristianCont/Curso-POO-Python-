import random

def ordenamiento_por_meszcla(lista):
    if len(lista)>1:
        medio=len(lista)//2
        izquierda=lista[:medio]
        Derecha=lista[medio:]
        print(izquierda, '-'*5, Derecha)

        #llamada recursiva en cada mitad 
        ordenamiento_por_meszcla(izquierda)
        ordenamiento_por_meszcla(Derecha)

        #iteradores para recorrer las sub listas 
        i=0
        j=0
        #iterador para la lista principal primera lista 
        k=0
        while i< len(izquierda) and j < len(Derecha):
            if izquierda[i]< Derecha[j]:
                lista[k]=izquierda[i]
                i += 1
            else:
                lista[k]=Derecha[j]
                j += 1
            k +=1

        while i <len(izquierda):
            lista[k]=izquierda[i]
            i+=1
            k+=1
        while j <len(Derecha):
            lista[k]=Derecha[j]
            j+=1
            k+=1
        print(f'izquierda{izquierda}, derecha {Derecha}')
        print(lista)
        print('-'*50)
    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)
    print('-'*20)

    lista_ordenada = ordenamiento_por_meszcla(lista)
    print(lista_ordenada)