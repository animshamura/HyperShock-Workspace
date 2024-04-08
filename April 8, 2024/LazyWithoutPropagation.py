toggle = [0]*20
def UpdateLazyPropagation(cp,L,R,l,r):
    if(r < L or R < l): return
    if(l <= L and R <= r): 
        toggle[cp] ^= 1
        return 
    mid = (L+R)//2
    UpdateLazyPropagation(cp*2,L,mid,l,r)
    UpdateLazyPropagation(cp*2+1,mid+1,R,l,r)

def QueryLazyPropagation(cp,L,R,pos):
    if(pos < L or R < pos): return 0
    if(L<= pos and pos<=R): return toggle[cp]
    mid = (L+R)//2
    if(pos <= mid ): return QueryLazyPropagation(cp*2,L,mid,pos) ^ toggle[cp]
    else: return QueryLazyPropagation(cp*2+1,mid+1,R,pos) ^ toggle[cp]
    
UpdateLazyPropagation(1,1,5,2,4)
print(toggle)
print(f"Query answer : {QueryLazyPropagation(1,1,6,5)}")
