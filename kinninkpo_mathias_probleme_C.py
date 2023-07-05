if __name__ == '__main__':
    liste1=[" ","un", "deux","trois","quatre","cinq", "six", "sept", "huit", "neuf"]
    liste2=[" ","onse", "douze", "treize" ,"quatorze" ,"quinze", "seize" ,"dix-set" ,"dix-huit" ,"dix-neuf"]
    liste3=[" " ,"dix", "vingt","trente" ,"quarante", "cinquante" ,"soixante","soixent-dix", "quatre-vingt", "quatre-vingt-dix"]
    nombre=int(input("Entrez le nombre"))
    #enregistrement du nombre chez l'utilisateur
    #nous avons ces variables juste pour savoir le nombre de centaine , de dizaine ou d'unite
    centaine=int(nombre/100)
    dizaine=int((nombre-(centaine*100))/10)
    unite=int((nombre-centaine*100-dizaine*10))
    #nous verifions d'abord la valeur de la centaine pour savoir comment proceder avec le reste
    if centaine == 1:
        if dizaine ==0 and unite== 0:
            print("cent")
        elif dizaine==1 and unite==0 :
            print("cent"+"-"+liste3[1])
        elif dizaine == 1 and unite == 1:
            print("cent"+"-"+liste2[1])
        elif dizaine == 0:
            print("cent"+"-"+liste1[unite])
        elif dizaine in [7,9]:
            if unite == 0:
               print("cent" + "-" + liste3[dizaine])
            else:
                print("cent-"+liste3[dizaine-1]+"-"+liste2[unite])
        else :
            print("cent" + "-" + liste3[dizaine] + "-" + liste1[unite])


    elif centaine == 0:
        if dizaine == 0 and unite == 0:
            print("Zéro")
        elif dizaine == 1 and unite == 0:
             print(liste3[1])
        elif dizaine == 1 and unite == 1:
             print(liste2[1])
        elif dizaine == 0:
                print(liste1[unite])
        elif dizaine in [7, 9]:
             if unite == 0:
                print(liste3[dizaine])
             else:
                print(liste3[dizaine-1] + "-" + liste2[unite])
        else:
            print(liste3[dizaine-1] + "-" + liste1[unite])
    else:
        if dizaine == 0 and unite == 0:
            print(liste1[centaine]+"-cents")
        elif dizaine == 1 and unite == 0:
            print(liste1[centaine]+"-cent-"+liste3[1])
        elif dizaine == 1 and unite == 1:
             print(liste1[centaine]+"-cent-"+liste2[1])
        elif dizaine == 0:
            print(liste1[centaine]+"-cent-"+liste1[unite])
            #verifier si c'est entre 70 ou 90
        elif dizaine in [7, 9]:
             if unite == 0:
                print(liste1[centaine]+"-cent"+liste3[dizaine])
             else:
                print(liste1[centaine]+"-cent-"+liste3[dizaine-1] + "-" + liste2[unite])
        else:
                print(liste1[centaine]+"-cent"+liste3[dizaine] + "-" + liste1[unite])

#la fin des conditions

