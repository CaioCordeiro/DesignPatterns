class animals():
    class aves():
        class galinha():
            nome = "none"
            cor = "none"
        class pombo():
            nome = "none"
            cor = "none"
        class pato():
            nome = "none"
            cor = "none"
    class mamiferos():
        class cachorro():
            nome = "none"
            cor = "none"
        class golfinho():
            nome = "none"
            cor = "none"
        class onitorrinco():
            nome = "none"
            cor = "noe"


def builder(animal,nome,cor):
    x = animals()
    if animal == "galinha":
        x.aves.galinha.nome = nome
        x.aves.galinha.cor = cor
        return x.aves.galinha
    if animal == "pombo":
        x.aves.pombo.nome = nome
        x.aves.pombo.cor = cor
        return  x.aves.pombo
    if animal == "pato":
        x.aves.pato.nome = nome
        x.aves.pato.cor = cor
        return x.aves.pato
    if animal == "cachorro":
        x.mamiferos.cachorro.nome = nome
        x.mamiferos.cachorro.cor = cor
        return  x.mamiferos.cachorro
    if animal== "golfinho":
        x.mamiferos.golfinho.nome = nome
        x.mamiferos.golfinho.cor = cor
        return x.mamiferos.golfinho
    if animal == "onitorrinco":
        x.mamiferos.onitorrinco.nome = nome
        x.mamiferos.onitorrinco.cor = cor
        return x.mamiferos.onitorrinco

def main():
    print("Essas são as opções:")
    print("""       Galinha
             Pombo
             Pato
             Cachorro
             Golfinho
             Onitorrinco""")
    animal = input("Insira o animal: ")
    nome = input("Insira o nome do seu animal: ")
    cor = input("Insira a cor: ")
    pet = builder(animal,nome,cor)
    print(pet)

main()
