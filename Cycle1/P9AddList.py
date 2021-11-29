l1 = [5, 10, 15, 20, 25, 30]
l2 = [2, 4, 6, 8, 10, 12]
print ( " Python Original list 1: " + str (l1))
print ( "Python Original list 2: " + str (l2))
res = []
for x in range (0, len (l1)):
    res.append( l1[x] + l2[x])
print ( " Addition of the list lt1 and lt2 is: " + str (res))