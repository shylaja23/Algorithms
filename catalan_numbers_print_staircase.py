 
def printStaircase(str, n): 
    if(n > 0): 
        _printStaircase(str, 0,  
                          n, 0, 0); 
    return; 
  
def _printStaircase(str, pos, n,  
                      open, close): 
      
    if(close == n): 
        for i in str: 
            print(i, end = ""); 
        print(); 
        return; 
    else: 
        if(open > close): 
            str[pos] = '-'
            #print("in first else loop", str )
            _printStaircase(str, pos + 1, n,  
                              open, close + 1); 
        if(open < n): 
            str[pos] = '|'
            #print ("in last else loop" , str)
            _printStaircase(str, pos + 1, n,  
                              open + 1, close); 
  
# Driver Code 
def main():
  n = 2
  str = [""] * 2 * n
  printStaircase(str, n)
