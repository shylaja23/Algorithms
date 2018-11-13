def printHands(a): 
    if(len(a) > 0 and len(a)%2 == 0): 
        op = [""]*(len(a)/2)
        cl = [""]*(len(a)/2)
        _printStaircase(a,0,op,cl,len(a)/2, 0, 0)
    return; 
  
def _printStaircase(a, pos,op,cl, n,open, close): 
    if(close == n): 
        res = ""
        for i in range(0,(len(a)/2)):
            res = res + op[i]+cl[i]
        print(res)
        return
    else: 
        if(open > close): 
            cl[close] = a[pos]
            print("first else loop", op, cl )
            _printStaircase(a, pos +1,op,cl, n,open, close + 1)
    if(open < n):
        op[open] = a[pos]
        print ("last else loop" ,op, cl)
        _printStaircase(a, pos + 1, op,cl,n,open + 1, close)
  
'''
a = "abcd"
printHands(a)
'''
