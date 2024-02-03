"""
    binary_search - une fonction de recherche d'un entier dans un tableau
    @x : int
    @arr : list[int]
    @return bool: renvoie true si n en dans arr , false si non
"""

def binary_search(arr,  x):
    l = 0
    r = len(arr) - 1
    while l <= r:

        mid = l + (r - l) // 2

        if arr[mid] == x:
            return True

        elif arr[mid] < x:
            l = mid + 1

        else:
            r = mid - 1

    return False

