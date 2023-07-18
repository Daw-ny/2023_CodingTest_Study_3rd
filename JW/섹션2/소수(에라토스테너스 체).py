n = int(input())
array = [True for i in range(n + 1)] 


for i in range(2, int(n**(1/2)) + 1): 
    if array[i] == True: 
        j = 2 
        while i * j <= n:
            array[i * j] = False
            j += 1

print(array.count(True)-2)
