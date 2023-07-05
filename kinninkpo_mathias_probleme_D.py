if __name__ == '__main__':
    nomBase=input("Entrez le nom de la base de donnée : ")
    #initialisationn du nombre du nom à nregister a zero
    nombre=0
    #la boucle While pour vrifier l'entrer
    while nombre==0:
        nombre=input("Entrez le nombre de personne a enregistrer : ")
        try :
            nombre = int(nombre)
        except:
            print("ERREUR : vous devez entrer un nombre")
            nombre =0
#au fure et a mesure que l'utilisateur entre les noms, on ajoute celon a notre liste creee et initialisee a vide
    liste=[]
    for i in range(1,nombre+1):
         nom = input(f"Entrez le nom de la {i}ème personne ")
         liste.append(nom)
    verification = input("Entrez 'o' pour confimer la creation de la liste ou 'n' pour l'annuler : ")
    #cette boucle while nous permert d'obliger l'utilisateur à entrer 'o' ou 'n'
    while not verification in {'o', 'n'}:
        print("vous devez necesseraiment entrer 'n' ou 'o' ")
        verification = input("Entrez 'o' pour confimer la creation de la liste ou 'n' pour l'annuler : ")
    if verification =="o":
        print("la base de donnée "+nomBase+" a été créé avec succes !")
    else:
        print("la base de donnée " + nomBase + " a été annulé avec succes !")




