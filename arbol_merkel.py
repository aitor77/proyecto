import hashlib, json
from collections import OrderedDict


class ArbolMerkel:

    def __init__(self, lista=None):

        self.lista = lista
        self.diccionario = OrderedDict()

    def crear_arbol(self):

        lista = self.lista
        diccionario = self.diccionario
        aux = []

        for index in range(0, len(lista), 2):
            # elmento mas a la izquierda
            izquierda = lista[index]
            hash_izq = hashlib.sha256(izquierda)
            diccionario[lista[index]] = hash_izq.hexdigest()

            print index

             # elemento a la derecha del que esta el mas a la izquierda
            if index+1 != len(lista):
               izq_derecha = lista[index+1]
               hash_der = hashlib.sha256(izq_derecha)
               diccionario[lista[index + 1]] = hash_der.hexdigest()
               aux.append(hash_izq.hexdigest() + hash_der.hexdigest())

            else:  # si no hay duplicamos la izquierda
                aux.append(hash_izq.hexdigest() + hash_izq.hexdigest())




        # ajustamos la variable y lo volvemos a lanzar hasta llegar a la raiz
        if len(lista) != 1:
            self.lista = aux
            self.diccionario = diccionario

            self.crear_arbol()

    def get_diccionario(self):
        return self.diccionario

    def get_raiz(self):
        ultima = self.diccionario.keys()[-1]
        return self.diccionario[ultima]


if __name__ == "__main__":
    mi_arbol = ArbolMerkel()

    lista = ['h1', 'h2', 'h3', 'h4']

    mi_arbol.lista = lista
    mi_arbol.crear_arbol()
    diccionario = mi_arbol.get_diccionario()

    print "primer ejemplo numero par en la lista"
    print 'Nodo final del arbol : ', mi_arbol.get_raiz()

    print(json.dumps(diccionario, indent=4))
    print "-" * 50

    mi_arbol2 = ArbolMerkel()

    lista2 = ['a', 'b', 'h3', 'h4', 'h5','a']

    mi_arbol2.lista = lista2
    mi_arbol2.crear_arbol()
    diccionario2 = mi_arbol2.get_diccionario()

    print "segundo ejemplo numero impar en la lista"
    print 'Nodo final del arbol : ', mi_arbol2.get_raiz()

    print(json.dumps(diccionario2, indent=4))
    print "-" * 50
