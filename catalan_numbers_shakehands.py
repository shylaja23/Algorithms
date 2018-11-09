def printHands(a): 
    if(len(a) > 0 and len(a)%2 == 0): 
      que = [""]*len(a)
      _printStaircase(a, que,"",0,len(a)/2, 0, 0); 
    return; 
  
def _printStaircase(a, que,res,pos, n,open, close): 
  if(close == n): 
    print(res) 
    return; 
  else: 
    tmp = list(que)
    if(open > close): 
      if(len(que) > 0):
        c = que.pop()
        res = res+c
        res = res+a[pos:pos+1]
        #print("in first else loop", str )
        _printStaircase(a, que,res, pos +1, n,open, close + 1); 
    if(open < n):
      tmp.append(a[pos:pos+1])
      #print ("in last else loop" , str)
      _printStaircase(a, tmp,res, pos + 1, n,open + 1, close); 
  
# Driver Code 
def main():
  a = "abcd"
  printHands(a)
