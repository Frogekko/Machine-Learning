def max_gevinst(spill): 
    if not spill: 
        return 0 
    if len(spill) == 1: 
        return spill[0] 
    return max( 
        spill[0] + min(max_gevinst(spill[2:]), max_gevinst(spill[1:-1])), 
        spill[-1] + min(max_gevinst(spill[:-2]), max_gevinst(spill[1:-1])) 
    )
    
print(max_gevinst([2, 7, 3]))
print(max_gevinst([5, 2, 10, 1]))
print(max_gevinst([1, 100, 2, 50]))
print(max_gevinst([]))
print(max_gevinst([8]))