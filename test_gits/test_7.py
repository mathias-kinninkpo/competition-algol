def under(l, a):
    return len([x for x in l if x < a])

def equal(l, a):
    return len([x for x in l if x == a])

def above(l, a):
    return len([x for x in l if x > a])


"""
    under_equal_above_nb : 
    @arr : list[int]
    @return : list - 
"""
def under_equal_above_nb(arr : list[int], val1 : int) -> int:
    
    tab = [0] * 3
    tab[0] = under(arr, val1)
    tab[1] = equal(arr, val1)
    tab[2] = above(arr, val1)
    
    return tab

print(under_equal_above_nb([2,4,6,6,8,10], 6))