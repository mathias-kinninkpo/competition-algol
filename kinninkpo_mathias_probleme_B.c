#include <stdio.h>
#include <stdlib.h>

int main()
{
    //declaration des variables
    int ligne, colonne, i, j;

    /*demande et recuperation du nombre de ligne et de colonne de la matrice chez l'utilisateur
    nous allons toute fois verifier si le nombre de ligne ou celui de colonne entrez par l'utilisatuer est compris entre 1 et 100 */
    printf("Entrez le nombre de ligne de votre matrice : ");

    scanf("%d",&ligne);
         while (ligne<1 || ligne>100)
         {
             printf("le nombre de ligne de la matrice entree est invalide, ce nombre doit etre compris entre 1 et 100\n ");
             printf("Veillez donc reesayer : ");
             scanf("%d",&ligne);
         }
    printf("Entrez le nombre de colonne de votre matrice : ");
    scanf("%d",&colonne);
        while (colonne<1 || colonne>100)
         {
             printf("le nombre de colonne de la matrice entree est invalide, ce nombre doit etre compris entre 1 et 100\n ");
             printf("Veillez donc reesayer : ");
             scanf("%d",&colonne);
         }

    //dans le but d'eviter le gaspillage de la case memoire, nous allons creer un tableau a la taille du nombre de ligne et de colonne
    int tab[ligne][colonne];
    //nous allons donc a cette etape recuperer les elements de la matrice
    for (i=1; i<=ligne; i++)
    {
        for (j=1; j<=colonne; j++)
        {
            printf("\nEntrez l'element de la %deme ligne et de la %deme colonne : ",i,j);
            scanf("%d",&tab[i][j]);
            while (tab[i][j]<-1000 || tab[i][j]>1000)
             {
                 printf("l'element de la matrice entre est invalide, ce nombre doit etre compris entre -1000 et 1000\n ");
                 printf("Veillez donc reesayer : ");
                 scanf("%d",&tab[j][j]);
             }

        }
    }
    //affichage de la matrice de depart
     printf(" la matrice entree est :\n\n");
     for (i=1; i<=ligne; i++)
    {
        for (j=1; j<=colonne; j++)
        {
            printf("%d\t",tab[i][j]);
        }
        printf("\n");
    }
    //affichage de la transposee de la matrice
    printf(" la transposee de la matrice entree est :\n\n");
     for (i=1; i<=ligne; i++)
    {
        for (j=1; j<=colonne; j++)
        {
            printf("%d\t",tab[j][i]);
        }
        printf("\n");
    }
    return 0;
}
