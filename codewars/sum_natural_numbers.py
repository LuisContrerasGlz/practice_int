# Create a program that sums all natural nombers until N using recursion

# 1 + 2 + 3 + 4 ...

def natural_sum(n):
    if n == 1:
        return 1
    else:
        return n + natural_sum(n-1)
    
print(natural_sum(4))