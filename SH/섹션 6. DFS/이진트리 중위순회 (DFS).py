# left children -> parent -> right children

def DFS(x) :
    if x > 7 :
        return
    else :
        # left children
        DFS(x*2)
        # now
        print(x, end=' ')
        # right children
        DFS(x*2+1)
        
DFS(1)