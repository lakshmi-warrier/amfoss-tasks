# Points - 40

testcases = int(input())

def ninja_sum(n, i):
        NinjaSum=0
        for dig in n:
            NinjaSum += int(dig)
        #print(NinjaSum)
        return NinjaSum
    
for test in range(testcases):
    lst = input().split(" ")
    n = lst[0]
    i = int(lst[1]) #start index
    mnslst = []
    ns0 = 0
    
    for start in range(len(n)-i+1):
        
        a = n[start:start+i]

        ns = ninja_sum(a,i)
        if ns > 0:
            mnslst.append(abs(ns-ns0))
            
        ns0 = ns
    
    if len(mnslst)==0:
        print(-1)
    else:
        print(min(mnslst))
