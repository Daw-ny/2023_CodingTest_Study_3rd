# parent -> left children -> right children

def DFS(x) :
    if x > 7 :
        return
    else :
        # now
        print(x, end=' ')
        # left children
        DFS(x*2)
        # right children
        DFS(x*2+1)
        
DFS(1)