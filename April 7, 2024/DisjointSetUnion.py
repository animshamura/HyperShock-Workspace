parent = [0,1,3,5,4,6,9,7,4,8]
toptier = ["Google","Microsoft","BJIT","NSI","JICA"]
startup = ["BACCO","Facebook","Arena","Selise","NASA"]
company = toptier + startup
def FindParentCompany(x): 
     if(parent[x]==x): return x
     else: 
         p = FindParentCompany(parent[x])
         parent[x] = p
         return p
     
def ChangeStockHolder(a,b): 
    parent[FindParentCompany(b)] = FindParentCompany(a)

def show():
    for j in range(len(parent)):
        print(f"Parent Company of {company[j]} : {company[parent[j]]}") 
    print()
    print()         
show()
ChangeStockHolder(2,3)   
show()
