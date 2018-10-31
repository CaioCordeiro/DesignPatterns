class animals():
    class aves():
        class galinha():
            tipo = "Isso é uma galinha"
        class pombo():
            tipo = "Isso é um pombo"
        class pato():
            tipo = "Isso é um pato"
    class mamiferos():
        class cachorro():
            tipo = "Isso é um cachorro"
        class golfinho():
            tipo = "Isso é um golfinho"
        class onitorrinco():
            tipo = "Isso é um golfinho"
  
class fabrica():
    def init(self,tipo):
        self.tipo = tipo

    def fabricar_aves(self):
        if tipo == "galinha":
            return animals.aves.galinha
        elif tipo == "pombo":
            return animals.aves.pombo
        elif tipo == "pato":
            return animals.aves.pato
    def fabricar_mamiferos(self):
        if tipo == "cachorro":
            return animals.mamiferos.cachorro
        elif tipo == "golfinho":
            return animals.mamiferos.golfinho
        elif tipo == "onitorrinco":
            return animals.mamiferos.onitorrinco
lista =[]
while True:
    tipo1 = input("Que tipo de animal voce quer adicionar(mamifero,aves)?")
    if tipo1 == "mamifero":
        tipo = input("Qual animal voce quer adicionar?")
        animal = fabrica.fabricar_mamiferos(tipo)
        lista.append(animal.tipo)
    elif tipo1 == "aves":
        tipo = input("Qual animal voce quer adicionar?")
        animal = fabrica.fabricar_aves(tipo)
        lista.append(animal.tipo)
    else:
        print("Escolha inválida")
        continue
    print(lista)