
'''
def get_ugly_number(n):
    return compute(n,1)

    
def compute(n,nxt):
    if(n == 0):
        return nxt
    while(1):
        if((nxt+1)%2 == 0 or (nxt+1)%3 == 0 or (nxt+1)%5 == 0):
            nxt = nxt+1
            break
        nxt = nxt+1
    return compute(n-1,nxt)
'''

def get_ugly(n):
  ugly = [0] *n
  ugly[0] = 1

  i2_next = 2
  i3_next = 3
  i5_next = 5

  i2 = i3 = i5 = 0

  for i in range(1,n):
    ugly[i] = min(i2_next,i3_next,i5_next)

    if(ugly[i] == i2_next):
      i2 +=1
      i2_next = ugly[i]*2
    
    if(ugly[i] == i3_next):
      i3 +=1
      i3_next = ugly[i]*3
    
    if(ugly[i] == i5_next):
      i5 +=1
      i5_next = ugly[i]*5

  return ugly[-1]

