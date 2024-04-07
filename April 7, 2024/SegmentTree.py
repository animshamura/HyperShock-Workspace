segmentTree = [-1]*15

def BuildSegmentTree(pos,L,R): 
    segmentTree[pos] = int(input("Enter a value : "))
    if(L==R): return 
    mid = (L+R)//2
    BuildSegmentTree(pos*2,L,mid)
    BuildSegmentTree(pos*2+1,mid+1,R)
    
def UpdateSegmentTree(cp,L,R,pos,up):
    if(L==R):
       segmentTree[pos]+=up 
       return 
    mid = (L+R)//2
    if(mid<=pos): UpdateSegmentTree(cp*2,L,mid,pos,up)
    else: UpdateSegmentTree(cp*2+1,mid+1,R,pos,up)
    segmentTree[cp] = segmentTree[cp*2]+segmentTree[cp*2+1]

def QuerySegmentTree(pos,l,r,L,R):
    if(r < L or R < l): return 0
    if(l<= L and r<=R): return segmentTree[pos]
    mid = (L+R)//2
    x = QuerySegmentTree(pos*2,l,r,L,mid)
    y = QuerySegmentTree(pos*2+1,l,r,mid+1,R)
    return x+y
    
print(segmentTree)
BuildSegmentTree(1,1,5)
print(segmentTree)
UpdateSegmentTree(0,0,5,3,6)
print(segmentTree)
print(f"Query answer : {QuerySegmentTree(1,1,6,1,8)}")
