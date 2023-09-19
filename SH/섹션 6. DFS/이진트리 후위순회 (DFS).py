# left children -> right children -> parent

def DFS(x) :
    if x > 7 :
        return
    else :
        # left children
        DFS(x*2)
        # right children
        DFS(x*2+1)
        # now
        print(x, end=' ')
        
DFS(1)