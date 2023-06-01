# Find the max number from 3 values.
# Example: 124, 21, 32. Result = 124.

def find_max(x,y,z):
    print (x, y, z)
    max = x
    if max<y:
        max= y

    if max<z:
        max = z

    return max

#---

my_max = find_max(12,678,81)
print(my_max)