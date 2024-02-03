if __name__ == '__main__':
#enregistrement de du mot
    nom=input("Entrez votre mot :")
#la creation d'une liste qui contient toute les lettres de l'alphabet
    liste=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    nom=nom.lower()
    trouver= True
#dans cette boucle, nous prenon un a un les elements de la liste et nous verifions si c'est effectivement dans dans le mot entre
#au cas contraire nous sortons de la boucle
    for i in range(len(liste)) :
            if liste[i] not in nom:
                trouver = False
                break;
    if trouver :
        print(" miste")
    else :
        print(" non miste")

