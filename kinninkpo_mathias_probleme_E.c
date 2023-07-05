#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    //le decleration des variablres
    float a, b, c,tab[3],tmp;
    int i,j;
    printf("Entrez la longueur de chaque cote sucessivement et sur la meme ligne : ");
    scanf("%f %f %f",&a,&b,&c);
    //En utilisant le theoreme d'Al-shi selon lequel a^2+b^2=c^2+2cos(a^b),a^2+c^2=b^2+2cos(a^c),b^2+c^2=a^2+2cos(b^c)
    tab[0]=acos(((pow(b,2)+pow(c,2))-pow(a,2))/(2*b*c));
    tab[1]=acos(((pow(c,2)+pow(a,2))-pow(b,2))/(2*c*a));
    tab[2]=acos(((pow(b,2)+pow(a,2))-pow(c,2))/(2*b*a));
    for (i=0; i<=2; i++)
    {
         for (j=i+1; j<=2; j++)
           if (tab[i]>tab[j])
             {
                 tmp = tab[i];
                 tab[i]=tab[j];
                 tab[j]=tmp ;
             }
    }

    printf("la mesure des angles dans l'odre croissant : %1.3f %1.3f %1.3f \n",tab[0],tab[1],tab[2]);


    return 0;
}
