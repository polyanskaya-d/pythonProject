def pith_triplet (arr):
    arr.sort()

    if arr[0]**2 + arr[1]**2 == arr[2]**2:
        return True
    else:
        return False

print (pith_triplet([5,3,4]))
print (pith_triplet([6,8,10]))
print (pith_triplet([100,3,65]))

