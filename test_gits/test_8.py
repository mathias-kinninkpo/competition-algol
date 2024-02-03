""" la fonction revoie le n-ième nombre de la suite de fibonacci en prenant un entier n en entrée
    en utilisant la technique de memorisation
"""
def fibonacci(n : int):

    a = 0
    b = 1
    for i in range(n):
        a , b = b , a + b
    return a

print(fibonacci(int(input())))

